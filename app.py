from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import re
# -------------------------------
# BASIC FLASK APP SETUP
# -------------------------------
app = Flask(__name__)

# -------------------------------
# GEMINI CONFIGURATION
# -------------------------------
# ⚠️ DEMO ONLY: Do NOT use this in production
genai.configure(api_key="AIzaSyARvwC12Zm4SugXIKH1JeHuRfpPimoJUH0")

# Use Gemini 2.5 Flash model
model = genai.GenerativeModel("gemini-2.5-flash")

def format_text(text):
    """
    Converts allowed formatting symbols into HTML.
    Allowed:
    ### Heading
    **bold**
    - bullet points
    """

    # Format headings
    text = re.sub(r'^###\s*(.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)

    # Format bold text
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Handle bullet points
    lines = text.split("\n")
    formatted = []
    in_list = False

    for line in lines:
        if line.strip().startswith("- "):
            if not in_list:
                formatted.append("<ul>")
                in_list = True
            formatted.append(f"<li>{line.strip()[2:]}</li>")
        else:
            if in_list:
                formatted.append("</ul>")
                in_list = False
            if line.strip():
                formatted.append(f"<p>{line}</p>")

    if in_list:
        formatted.append("</ul>")

    return "\n".join(formatted)

# ---------------------------------
# ROUTE: HOME PAGE
# ---------------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# ---------------------------------
# ROUTE: CHAT API
# ---------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please enter a mathematics question."})

    # ---------------------------------
    # STUDYMATE AI PROMPT (AS PROVIDED)
    # ---------------------------------
    prompt = f"""
You are **StudyMate AI**, an academic AI tutor for undergraduate students studying Mathematics.

RULES FOR EVERY RESPONSE:

1. Step-by-Step Explanation or Solution
   - Explain ideas slowly and clearly
   - Assume the student is learning for the first time
   - Do not skip steps

2. Practical Application
   - Explain how this concept is used in academics or daily life

3. Real-World Scenario
   - Give a simple, realistic example related to mathematics

SUBJECT GUIDELINES:
- For Mathematics: explain logic and reasoning before formulas

Avoid advanced or postgraduate-level content.
Use a friendly, academic, and encouraging tone.

Formatting Rules (MANDATORY):
- Use ### only for headings
- Use **text** only for bold emphasis
- Use hyphen (-) only for bullet points
- Do NOT use any other formatting symbols
- Do NOT use dollar signs

Now respond to the following student question:

{user_message}
"""

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        # Apply formatting rules using re
        formatted_html = format_text(raw_text)

        return jsonify({"reply": formatted_html})

    except Exception:
        return jsonify({"reply": "Error generating response. Please try again."})

# ---------------------------------
# RUN SERVER
# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)