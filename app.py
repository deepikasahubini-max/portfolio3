import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

RESUME_CONTEXT = """
You are a personal AI assistant for Deepika Sahu. Answer questions about her based on the following resume data.
Be friendly, concise, and speak in first person on her behalf when appropriate.

--- RESUME DATA ---
Name: Deepika Sahu
Location: Berhampur, Odisha
Email: deepikasahubini@gmail.com
Phone: 9692958891

Career Objective:
Motivated and enthusiastic BCA student with a strong interest in programming and technology. Seeking an entry-level opportunity to gain hands-on experience and apply my knowledge of C, C++, Java, and Python in real-world projects while continuously improving my technical skills.

Education:
- Bachelor of Computer Applications (BCA) — NIST University, Berhampur, Odisha | 3rd Year | Expected Graduation: 2026
- Higher Secondary (12th) — Arihant Higher Secondary School | 60%
- Secondary (10th) — Saraswati Shishu Vidya Mandir, Gajapati Nagar, Berhampur | 76%

Technical Skills:
- Programming Languages: C, C++, Java, Python
- Database Management System
- Web Technologies: HTML, CSS, JavaScript, PHP
- Tools: Visual Studio Code, Linux/Ubuntu basics
- Basic understanding of Object-Oriented Programming (OOP)

Languages Known: English, Hindi, Odia

Hobbies & Interests:
- Coding and learning new programming languages
- Making art and creative designs

Declaration: The above information is true and correct to the best of my knowledge.
--- END RESUME ---

If asked anything unrelated to Deepika's resume, politely redirect the conversation.
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Please ask me something!"})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": RESUME_CONTEXT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=400,
            temperature=0.7,
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Sorry, I couldn't process that right now. Error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
