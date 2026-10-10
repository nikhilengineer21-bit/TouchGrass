
const form = document.querySelector("#quest-form");
const result = document.querySelector("#quest-result");
const resultTitle = document.querySelector("#result-title");
const resultDescription = document.querySelector("#result-description");
const resultSteps = document.querySelector("#result-steps");
const resultTime = document.querySelector("#result-time");
const completeButton = document.querySelector("#complete-button");
const completionMessage = document.querySelector("#completion-message");
const newQuestButton = document.querySelector("#new-quest-button");

const generateButton = form.querySelector('button[type="submit"]');
const generateButtonText = generateButton.querySelector("span");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const preferences = {
    time: Number(form.querySelector('input[name="time"]:checked').value),
    activity: form.querySelector('input[name="activity"]:checked').value,
    difficulty: document.querySelector("#difficulty").value,
    company: document.querySelector("#company").value
  };

  generateButton.disabled = true;
  generateButtonText.textContent = "Creating your quest...";
  result.hidden = true;

  try {
    const response = await fetch("/api/quest", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(preferences)
    });

    const quest = await response.json();

    if (!response.ok) {
      throw new Error(quest.error || "Could not generate a quest.");
    }

    resultTitle.textContent = quest.title;
    resultDescription.textContent =
      `${quest.time} minutes for yourself. ${quest.description}`;
    resultTime.textContent = `${quest.time} MIN`;

    resultSteps.replaceChildren();

    quest.steps.forEach((step) => {
      const item = document.createElement("li");
      item.textContent = step;
      resultSteps.appendChild(item);
    });

    let sourceNote = document.querySelector("#ai-source-note");

    if (!sourceNote) {
      sourceNote = document.createElement("p");
      sourceNote.id = "ai-source-note";
      sourceNote.className = "privacy-note";
      result.querySelector(".result-topline").after(sourceNote);
    }

    sourceNote.textContent = quest.source === "ollama"
      ? "Generated locally with Qwen2.5 via Ollama."
      : "Using a built-in quest because the AI response did not pass validation.";

    completionMessage.hidden = true;
    completeButton.hidden = false;
    result.hidden = false;

    result.scrollIntoView({ behavior: "smooth", block: "start" });
  } catch (error) {
    alert(
      "We couldn't reach the TouchGrass server. Please check that server.py is running, then try again."
    );
    console.error(error);
  } finally {
    generateButton.disabled = false;
    generateButtonText.textContent = "Find my outdoor quest";
  }
});

completeButton.addEventListener("click", () => {
  completionMessage.hidden = false;
  completeButton.hidden = true;
});

newQuestButton.addEventListener("click", () => {
  result.hidden = true;
  completionMessage.hidden = true;
  form.scrollIntoView({ behavior: "smooth", block: "center" });
});
