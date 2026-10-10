# 🌿 TouchGrass — AI Outdoor Quest

**Get a quest. Put the phone away. Explore the real world.**

TouchGrass is a small web application that uses locally running AI to generate personalized outdoor quests. It aims to help people take a break from screens and reconnect with the world around them.

## ✨ Features

- Personalized quests based on available time, activity, difficulty, and company
- AI-generated outdoor activities using a local Qwen model
- Local inference through Ollama
- Built-in fallback quests when AI generation fails validation
- Simple quest completion flow
- No GPS tracking or account required

## 🛠️ Technology Stack

- HTML
- CSS
- JavaScript
- Python
- [Ollama](https://ollama.com/)
- Qwen2.5 0.5B

## 🚀 Run Locally

### Requirements

- Python 3
- Ollama
- The `qwen2.5:0.5b` model

### 1. Download the model

Open a terminal and run:

```bash
ollama pull qwen2.5:0.5b
```

### 2. Start Ollama

Make sure the Ollama service is running. On systems using systemd, you can run:

```bash
sudo systemctl enable --now ollama
```

### 3. Start TouchGrass

Open a terminal inside the project directory and run:

```bash
python3 server.py
```

### 4. Open the website

Visit:

http://127.0.0.1:8000

Keep the Python server running while using the application.

## 🌱 How It Works

1. Choose your available time and activity preferences.
2. Request an outdoor quest.
3. The Python backend sends a prompt to the local Qwen model through Ollama.
4. The backend checks the generated response.
5. If generation fails or the response does not pass validation, a built-in quest is returned.
6. Head outdoors and mark the quest complete when you return.

## 🔓 Why Open Innovation Matters

Open models and tools make it possible for developers to experiment, learn, and build applications without relying entirely on a proprietary AI service. Running inference locally can also reduce dependence on remote APIs and avoid sending quest preferences to a third-party inference service.

TouchGrass is a small example of how accessible AI tools can support healthier, real-world habits.

## ⚠️ Safety and Limitations

AI-generated activities may still contain unsuitable suggestions. Basic validation is not a guarantee of safety. Choose familiar public locations, follow local rules, remain aware of your surroundings, and use your own judgment.

The application does not provide navigation, verify outdoor conditions, or guarantee that a location is safe.

## 📌 Project Status

Early prototype. More testing, improved validation, documentation, and accessibility work are planned.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
