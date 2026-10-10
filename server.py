
import json
import re
import urllib.error
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


HOST = "127.0.0.1"
PORT = 8000
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen2.5:0.5b"

# Reliable fallback quests if AI is unavailable or its response is invalid.
FALLBACK_QUESTS = {
    "walking": {
        "title": "The Little Walking Reset",
        "description": "Take a gentle break and notice your surroundings.",
        "steps": [
            "Walk at a comfortable pace in a familiar public place.",
            "Notice three things around you that you usually overlook.",
            "Pause briefly, then return when you are ready.",
        ],
    },
    "nature": {
        "title": "Nature's Tiny Details",
        "description": "Discover small details in the natural world.",
        "steps": [
            "Find a comfortable spot in a safe public outdoor area.",
            "Notice three natural details, such as leaf shapes or clouds.",
            "Listen quietly to the surrounding sounds before heading back.",
        ],
    },
    "photography": {
        "title": "Everyday Beauty",
        "description": "Look for an interesting detail in your surroundings.",
        "steps": [
            "Choose a familiar outdoor place where photography is permitted.",
            "Notice an interesting pattern, shadow, or natural texture.",
            "Take a photo if you wish, respecting other people's privacy.",
        ],
    },
    "relaxation": {
        "title": "A Moment to Breathe",
        "description": "Give yourself a peaceful break outdoors.",
        "steps": [
            "Find a comfortable, safe place to sit outdoors.",
            "Notice the sounds, colors, and breeze around you.",
            "Take a few comfortable breaths before heading back.",
        ],
    },
}

ALLOWED_ACTIVITIES = set(FALLBACK_QUESTS)
ALLOWED_TIMES = {10, 20, 30}
ALLOWED_DIFFICULTIES = {"easy", "moderate"}
ALLOWED_COMPANY = {"alone", "friends"}

# Basic screening only; this is not a complete safety system.
BLOCKED_TERMS = re.compile(
    r"\b("
    r"campfire|build a fire|start a fire|set up a tent|"
    r"climb a cliff|climb a roof|"
    r"enter private property|"
    r"jump into a river|jump into a lake|"
    r"cross a highway|cross a busy road|"
    r"approach a wild animal"
    r")\b",
    re.IGNORECASE,
)


def generate_with_ollama(preferences):
    """Generate and validate one quest using the local Ollama model."""

    prompt = f"""
You create short, practical outdoor quests.

User preferences:
- Available time: {preferences["time"]} minutes
- Activity: {preferences["activity"]}
- Difficulty: {preferences["difficulty"]}
- Company: {preferences["company"]}

Return ONLY a JSON object with this structure:
{{
  "title": "Short title",
  "description": "One short sentence",
  "steps": [
    "First activity",
    "Second activity",
    "Third activity"
  ]
}}

Rules:
- Exactly three short steps.
- Match the selected activity and available time.
- For friends, suggest an activity they can do together.
- Use a familiar, safe public outdoor place.
- Require no special equipment.
- Do not suggest camping, fire, rivers, dangerous actions,
  private property, approaching wildlife, or road crossings.
- Use simple language and realistic activities.
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.2,
            "num_predict": 220,
        },
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=90) as response:
        data = json.loads(response.read().decode("utf-8"))

    raw_response = data.get("response", "")
    quest = json.loads(raw_response)

    if not isinstance(quest, dict):
        print("[DEBUG] Rejected: response is not a JSON object.")
        return None

    title = quest.get("title")
    description = quest.get("description")
    steps = quest.get("steps")

    if not isinstance(title, str) or not title.strip():
        print("[DEBUG] Rejected: missing title.")
        return None

    if not isinstance(description, str) or not description.strip():
        print("[DEBUG] Rejected: missing description.")
        return None

    if not isinstance(steps, list) or len(steps) != 3:
        print("[DEBUG] Rejected: expected exactly three steps.")
        return None

    if not all(
        isinstance(step, str) and step.strip()
        for step in steps
    ):
        print("[DEBUG] Rejected: invalid step text.")
        return None

    fields = [title, description, *steps]

    if any(len(field.strip()) > 350 for field in fields):
        print("[DEBUG] Rejected: a field is too long.")
        return None

    combined = " ".join(fields)

    if BLOCKED_TERMS.search(combined):
        print("[DEBUG] Rejected: matched a blocked phrase.")
        return None

    return {
        "title": title.strip(),
        "description": description.strip(),
        "steps": [step.strip() for step in steps],
    }


class TouchGrassHandler(SimpleHTTPRequestHandler):

    def send_json(self, status, data):
        encoded = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8",
        )
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(encoded)

    def do_POST(self):
        if self.path != "/api/quest":
            self.send_json(404, {"error": "Endpoint not found."})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))

            if length < 1 or length > 5000:
                self.send_json(
                    400,
                    {"error": "Invalid request size."},
                )
                return

            body = json.loads(
                self.rfile.read(length).decode("utf-8")
            )

            if not isinstance(body, dict):
                self.send_json(400, {"error": "Invalid request."})
                return

            time = body.get("time")
            activity = body.get("activity")
            difficulty = body.get("difficulty")
            company = body.get("company")

            if (
                isinstance(time, bool)
                or not isinstance(time, int)
                or time not in ALLOWED_TIMES
                or activity not in ALLOWED_ACTIVITIES
                or difficulty not in ALLOWED_DIFFICULTIES
                or company not in ALLOWED_COMPANY
            ):
                self.send_json(
                    400,
                    {"error": "Invalid quest preferences."},
                )
                return

            preferences = {
                "time": time,
                "activity": activity,
                "difficulty": difficulty,
                "company": company,
            }

            print(
                f"[TouchGrass] Generating quest: {preferences}"
            )

            try:
                quest = generate_with_ollama(preferences)
            except (
                urllib.error.URLError,
                TimeoutError,
                json.JSONDecodeError,
                KeyError,
                TypeError,
                ValueError,
            ) as error:
                print(f"[DEBUG] Ollama request failed: {error}")
                quest = None

            if quest is None:
                quest = FALLBACK_QUESTS[activity].copy()
                quest["steps"] = list(quest["steps"])
                source = "fallback"
                print("[DEBUG] Using fallback quest.")
            else:
                source = "ollama"
                print("[DEBUG] Validated Ollama quest.")

            quest["time"] = time
            quest["source"] = source

            self.send_json(200, quest)

        except (json.JSONDecodeError, UnicodeDecodeError):
            self.send_json(400, {"error": "Invalid JSON request."})
        except (BrokenPipeError, ConnectionResetError):
            print("[TouchGrass] Client disconnected.")

    def log_message(self, format_string, *args):
        print(f"[TouchGrass] {args[0]}")


if __name__ == "__main__":
    print(f"TouchGrass running at http://{HOST}:{PORT}")
    print(f"Using Ollama model: {MODEL}")

    server = ThreadingHTTPServer((HOST, PORT), TouchGrassHandler)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nTouchGrass server stopped.")
    finally:
        server.server_close()
