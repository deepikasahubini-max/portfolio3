# Temple Run Portfolio - Deepika Sahu

A minimalist, game-inspired portfolio website built with Flask and Python, featuring a Groq-powered AI chatbot.

## Features
- **Temple Run Theme**: Parallax backgrounds and pixel-art aesthetic.
- **AI Chatbot**: Integrated Groq API trained on Deepika's resume.
- **Responsive Navigation**: Keyboard arrows or navigation buttons to explore sections.
- **Single Page**: No scrolling, smooth section transitions.

## Deployment to Render
1. Push this project to a GitHub repository.
2. In Render, create a new **Web Service**.
3. Connect your repository.
4. Set **Environment Variables**:
   - `GROQ_API_KEY`: Your Groq API Key.
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `gunicorn app:app`

## Local Setup
1. Clone the repository.
2. Install requirements: `pip install -r requirements.txt`
3. Create a `.env` file with your `GROQ_API_KEY`.
4. Run: `python app.py`
