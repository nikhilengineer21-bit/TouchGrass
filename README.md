# 🌿 TouchGrass — AI Outdoor Quest

**Get a quest. Put the phone away. Explore the real world.**

TouchGrass is a small web application that uses locally running AI to generate personalized outdoor quests. It aims to help people take a break from screens and reconnect with the world around them.

## 🏆 Built for Hacktoberfest 2026

TouchGrass was created for the DEV Community's **Hacktoberfest 2026 Open-Source AI Challenge — Week 1: Touch Grass**.

The project explores how accessible, locally run AI can encourage people to take screen breaks and spend more time outdoors.

This is an early open-source prototype built to learn, experiment, and improve through collaboration. Participation in the challenge does not imply endorsement by the Hacktoberfest organizers.

## ✨ Features

- Personalized quests based on available time, activity, difficulty, and company
- AI-generated outdoor activities using a locally running Qwen model
- Local inference through Ollama
- Built-in fallback quests when AI generation fails validation
- Simple quest completion flow
- No user account or GPS tracking required
- A responsive web interface for desktop and mobile screens

## 🛠️ Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python
- **Local AI runtime:** [Ollama](https://ollama.com/)
- **AI model:** [Qwen2.5 0.5B](https://ollama.com/library/qwen2.5:0.5b)

## 🚀 Run Locally

### Requirements

Before running TouchGrass, make sure you have:

- Python 3
- [Ollama installed](https://ollama.com/download)
- The `qwen2.5:0.5b` model downloaded

### 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/nikhilengineer21-bit/TouchGrass.git
cd TouchGrass
```

### 2. Download the AI model

```bash
ollama pull qwen2.5:0.5b
```

This downloads the model to your computer. You only need to do this once unless you remove the model.

### 3. Start Ollama

Make sure Ollama is running.

On Linux systems that use systemd, you can start and enable the service with:

```bash
sudo systemctl enable --now ollama
```

On other operating systems, follow the relevant Ollama instructions.

### 4. Start TouchGrass

From the project directory, run:

```bash
python3 server.py
```

Keep this terminal open while using the application.

### 5. Open the application

Visit:

**http://127.0.0.1:8000**

The app should now be available in your browser.

If the AI model is unavailable or its response fails the application's validation, TouchGrass can return a built-in fallback quest instead.

## 🌱 How It Works

1. Choose your available time and activity preferences.
2. Select your preferred difficulty and whether you are going alone or with friends.
3. Request an outdoor quest.
4. The Python backend sends a prompt to the local Qwen model through Ollama.
5. The backend checks the generated response.
6. If generation fails or the response does not pass validation, a built-in quest is returned.
7. Put your phone away, head outdoors, and mark the quest complete when you return.

## 🔓 Why Open Innovation Matters

Open-source software and openly available AI models allow developers to experiment, learn, and build useful applications without depending entirely on proprietary AI services.

Running inference locally can reduce dependence on remote APIs and avoid sending quest preferences to a third-party inference service. It also gives developers an opportunity to learn how AI models can be integrated into real applications.

TouchGrass is a small experiment in using accessible AI tools to encourage healthier, real-world habits.

## ⚠️ Safety, Privacy, and Limitations

TouchGrass is an experimental prototype, not a safety-critical outdoor navigation tool.

- AI-generated activities may contain unsuitable or impractical suggestions.
- Basic response validation does not guarantee that a quest is safe or appropriate.
- Review every quest before following it. Choose familiar public locations, follow local rules, and use your own judgment.
- The app does not verify weather, terrain, local hazards, or outdoor conditions.
- The app does not provide navigation or guarantee that a location is safe.
- Local AI generation depends on Ollama and the required model being available.
- A built-in fallback can be used when AI generation fails validation.

## 🔒 Privacy

The application is designed to generate quests locally through Ollama. It does not require a user account or GPS tracking.

When running locally, quest generation can take place on your own computer rather than relying on a remote AI inference API. This does not mean that every possible deployment or future version will have identical privacy properties.

## 📌 Project Status

**Status: Early prototype**

TouchGrass is an ongoing learning and open-source project. Potential future improvements include:

- Stronger validation of AI-generated quests
- Improved accessibility and responsive design
- More varied built-in quests
- Better error handling and testing
- Clearer deployment instructions
- Contributions from other developers

These are planned improvements, not features that are already guaranteed to be implemented.

## 🤝 Contributing

Contributions, bug reports, documentation improvements, and suggestions are welcome.

If you would like to contribute:

1. Explore the existing code and README.
2. Identify a bug or a useful improvement.
3. Open an issue to discuss significant changes.
4. Create a branch for your changes.
5. Test your changes before opening a pull request.

Please keep contributions focused, explain what you changed, and avoid introducing unnecessary complexity.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🌍 Project Links

- **GitHub repository:** [TouchGrass — AI Outdoor Quest](https://github.com/nikhilengineer21-bit/TouchGrass)
- **Hacktoberfest Week 1 challenge:** [Touch Grass — DEV Community](https://dev.to/challenges/hacktoberfest-week1-2026-10-05)

