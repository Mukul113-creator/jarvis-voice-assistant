# Jarvis Voice Assistant

Talk to your browser and your computer. Jarvis turns speech into text, reads text aloud,
and runs voice commands through a small Python server.

Two ways to use it:
- **Web app** (Flask + HTML): speech to text, text to speech, and voice commands in the browser.
- **Desktop app** (`main.py`): listens through your microphone and speaks replies.

## Features
- Voice to text in English, Hindi and other Indian languages (Chrome or Edge)
- Text to voice with voice, speed and pitch controls
- "Jarvis mode": every phrase you say is sent to the Python API as a command
- Commands: open Google/YouTube/GitHub, search for ..., time, date, stop
- Copy and download your text as .txt

## Project structure
```
app.py                    Flask server (page + /api/command)
jarvis_core.py            Command logic shared by web and desktop apps
main.py                   Desktop version (microphone + speaker)
static/index.html         Web frontend (HTML, CSS, JavaScript)
requirements.txt          Web app libraries (also used for deployment)
requirements-desktop.txt  Extra libraries for main.py
```

## Run the web app
```
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 in Chrome or Edge, allow the microphone, and press the mic.

## Run the desktop app
```
pip install -r requirements-desktop.txt
python main.py
```

## Deploy free on Render
1. Push this project to GitHub.
2. On render.com, click New, then Web Service, and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Choose the Free instance type and click Create Web Service.

Free services sleep after 15 minutes without visitors, so the first request after a
break can take up to about 30 seconds.

## Voice commands
| Say | Result |
|---|---|
| open YouTube | Opens YouTube |
| search for python tutorials | Searches Google |
| what is the time | Tells the time in your time zone |
| what is the date | Tells today's date |
| stop / bye | Stops Jarvis |

## Future improvements
- Wake word ("Hey Jarvis")
- Weather and news commands
- Answer questions with an AI model
- Hindi voice commands in the Python logic
