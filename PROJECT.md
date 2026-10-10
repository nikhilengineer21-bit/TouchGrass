# 🌿 TouchGrass — AI Outdoor Quest

## Project Overview

**TouchGrass** is a project designed to help people spend less time looking at screens and more time exploring the world around them.

The application will use open-source AI to generate personalized outdoor activities based on a user's available time, interests, and difficulty preference.

For example, a student with 20 minutes free could receive a short outdoor quest involving walking, observing nature, or discovering something new nearby.

### Core Idea

**Get a quest. Put the phone away. Explore the real world.**

### Project Goal

Build a simple, working application that uses open-source AI meaningfully and encourages people to participate in real-world outdoor activities.

### Challenge

Hacktoberfest 2026 — Week 1: Touch Grass

### Current Status

Planning and initial setup.

## 2. MVP Scope and Features

The Minimum Viable Product (MVP) is the first usable version of TouchGrass. It will focus on generating safe, personalized outdoor quests with open-source AI.

### 2.1 AI-Generated Outdoor Quests

The application will generate a short outdoor quest based on the user's choices. Activities should be varied, practical, easy to understand, and suitable for the selected time and difficulty.

### 2.2 Personalized Choices

The user will be able to select:

- Available time: 10, 20, or 30 minutes
- Activity preference: walking, nature observation, photography, or relaxation
- Difficulty: easy or moderate
- Company: alone or with friends

The application will use these choices to personalize the generated quest.

### 2.3 Quest Completion

The user will be able to view the quest steps, check off completed activities, and mark the quest as finished.

The completion process should be simple and should not encourage unnecessary screen time.

### 2.4 Outdoor Safety Tips

The application will provide basic safety reminders, such as:

- Choose a familiar, public, and safe outdoor location.
- Follow local rules and respect nature.
- Do not approach unfamiliar animals or dangerous plants.
- Stay aware of traffic and surroundings.
- Do not share precise location information unnecessarily.

The AI must not be treated as a substitute for personal judgment or local safety guidance.

### 2.5 Local Open-Weight AI

The preferred approach is to use a small open-weight AI model that can run locally on the user's computer.

Before choosing a model, we will test the available hardware, memory usage, response speed, and quality of generated quests.

If local inference proves impractical, we will evaluate another approach that still satisfies the challenge's open-source AI requirements. We will document the actual model, its license, and how it is used.

---

## 3. User Flow

1. The user opens TouchGrass.
2. The user selects the available time, activity preference, difficulty, and company.
3. The user requests a quest.
4. The AI generates a personalized outdoor quest.
5. The application displays the quest and safety reminders.
6. The user leaves the screen and completes the activity outdoors.
7. The user returns to mark the quest as completed.

---

## 4. MVP Boundaries

To finish a reliable first version, the following are outside the initial scope:

- User accounts and authentication
- Social feeds, likes, and comments
- Live GPS tracking
- Maps and automatic route navigation
- Photo recognition or camera-based verification
- Complex databases or cloud infrastructure
- Leaderboards and competitive rankings

These features may be considered later if the core application is working.

---

## 5. Success Criteria

The MVP will be considered successful when:

- A user can choose preferences and generate a quest.
- The generated quest reflects the user's selections.
- The app displays useful outdoor safety reminders.
- A user can complete and mark a quest as finished.
- Open-source AI genuinely contributes to quest generation.
- The project can be demonstrated working.
- The repository explains setup, model usage, limitations, and licensing.
- The final DEV submission includes a demo, repository link, and explanation of why open innovation matters.

## 6. Current Implementation

TouchGrass is a local web application built with HTML, CSS, JavaScript, and Python.

### Technology Stack

- **Frontend:** HTML, CSS, and JavaScript
- **Backend:** Python's built-in HTTP server
- **AI runtime:** Ollama
- **AI model:** Qwen2.5 0.5B
- **Response format:** JSON

### How It Works

1. The user selects a time limit, activity, difficulty, and whether they are alone or with friends.
2. The frontend sends these preferences to the Python backend.
3. The backend requests a quest from the locally running Qwen model through Ollama.
4. The backend checks the response structure and screens for certain unsuitable suggestions.
5. If the response fails validation or AI generation is unavailable, a built-in quest is returned.
6. The user can read the quest, complete the outdoor activity, and mark it as finished.

### Current Limitations

- AI-generated content can still contain unsuitable or impractical suggestions.
- The current validation checks are basic and do not guarantee safety.
- Local AI performance depends on the computer's available resources.
- The current version does not use GPS or track the user's location.
- More testing is needed before considering the application ready for public use.

### Project Goal

TouchGrass uses open AI technology to encourage people to spend less time scrolling and more time exploring the real world.

**Get a quest. Put the phone away. Explore the real world.**