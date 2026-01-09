# 📘 Study Mate AI – Hands-on GenAI Workshop

This README contains **step-by-step prompts** to guide participants through a hands-on session on **Generative AI** by building a chatbot called **Study Mate AI**. Each prompt can be copied directly into a GenAI tool (like ChatGPT) during the workshop.

---

## 🧠 Project Overview

**Study Mate AI** is a simple educational chatbot designed to help students with learning, explanations, summaries, and study guidance.

The session is divided into:

1. Backend setup
2. Basic frontend (HTML)
3. Customization
4. Text formatting
5. Hands-on activity

---

## 🔹 Prompt 1: Backend – First Step of the Chatbot

**Goal:** Create the backend logic for Study Mate AI.

### Prompt:

```
Create a basic Flask backend in Python for a simple AI chatbot used in a classroom demonstration.
The backend must use the google.generativeai library with the Gemini 2.5 Flash model.

Requirements:

	Use Flask

	Use render_template() to serve an HTML page from the templates folder
	dont use any env variables 

Sends the input to the Gemini 2.5 Flash model

Limits and refines the AI response to be short and clear

Keep the code minimal, readable, and well commented

This backend is only a learning prototype, not a production system

The generated code should clearly show:

	How Flask receives requests

	How the AI model is called


	How a response is sent back to the frontend
	
also write a basic single html code and the project structure 
```

---

## 🔹 Prompt 2: Basic HTML Frontend

**Goal:** Create a simple web interface to interact with the chatbot.

### Prompt:

```

Include a header with the title “StudyMate AI – Basic Chatbot”

Display the College of Engineering Poonjar logo at the top-right corner using this image URL:
https://cep.ac.in/images/logo.png

Include:

	One text input box for user messages
	One response/output box 
	One Send button

Display the response dynamically in the response box

Keep the layout clean, minimal, and academic

Avoid chat bubbles and complex styling

The final output should be a single HTML file 
```

---

## 🔹 Prompt 3: Customization Prompt

**Goal:** Customize the chatbot’s personality and behavior.

### Prompt:

```
Customize the chatbot "Study Mate AI" with the following behavior:

- Friendly and encouraging tone
- Explains concepts step by step
- Uses simple language for students
- Motivates users when they are stuck
- Can answer questions related to studying, exams, and learning strategies

Update the backend logic Follow these teaching guidelines for this response:

1. Step-by-Step Explanation or Solution
   - Explain ideas slowly and clearly
   - Assume the student is learning for the first time
   - Do not skip reasoning steps
   - For mathematics: explain the logic before introducing formulas

2. Practical Application
   - Briefly explain how this concept or method is used in academics or daily life

3. Real-World Scenario
   - Provide one simple, realistic example related to mathematics

STYLE AND SCOPE:
- Use an encouraging and academic tone

Avoid:
- Chatbot-style conversation fillers
- Direct answer-only responses
- Overly short summaries

Now answer the student’s question clearly:
```

---

## 🔹 Prompt 4: Text Formatting Prompt

**Goal:** Improve readability of chatbot responses.

### Prompt:

```
by using the re module in python and using formatting  tags in html format the text output as follows below 

- ### at the beginning of a line  
  Use this for headings.  
  This represents a large, bold heading.

- **text**  
  Use this for bold and emphasized text.  
  This represents larger and highlighted text.

- Hyphen (-)  
  Use this for bullet points.
- MATHAMTICAL EXPRESSSIONS 
	format expressions like sqrt root power fraction ect....
Before returning the output:
- Ensure symbols ###, ** **, and - are formatted 
- Ensure the text is clean and readable

The output must follow these formatting rules exactly.

get the updated python and html code 

```

---

## 🧪 Activity: Hands-on Task

### 🎯 Objective

Participants will create a **new HTML frontend** and connect it to the existing backend.

# 📌 Activity Criteria 

1. **Institution Branding**
   - The interface must display the official logo of *College of Engineering Poonjar*
   - Logo must be placed in a suitable and respectful position (e.g., header/navigation area)
   - Logo must be clearly visible and not distorted
   - **Logo URL:** `https://cep.ac.in/images/logo.png`
2. **Group Identity**
   - The full names of all group members must be displayed in the **footer section**
3. **Functional Requirement**
   - Frontend must successfully communicate with the existing backend 
4. **Creativity & UX**
   - Students may choose their own colors, layout, and component styles
5. **Backend Communication**\
   The frontend must communicate with the backend using the route:
   ```
   POST → /chat
   ```
   ##

---

## ✅ Outcome of the Session

By the end of this session, participants will:

- Understand how GenAI can be used to build chatbots
- Create a backend and frontend for a chatbot
- Customize AI behavior using prompts
- Connect frontend and backend components

---

🚀 **Happy Learning with Study Mate AI!**

