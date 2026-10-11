"""The brain of Jarvis. Used by the desktop app (main.py) and the web app (app.py)."""
import datetime
import re
from urllib.parse import quote_plus

try:
    from zoneinfo import ZoneInfo
except ImportError:  # very old Python
    ZoneInfo = None

SITES = {
    
    "youtube": ("YouTube", "https://www.youtube.com"),
    
}


def _now(tz_name):
    """Current time in the user's time zone (the server may be in another country)."""
    if tz_name and ZoneInfo:
        try:
            return datetime.datetime.now(ZoneInfo(tz_name))
        except Exception:
            pass
    return datetime.datetime.now()


def _result(reply, url=None, quit_=False):
    return {"reply": reply, "url": url, "quit": quit_}


def process(command, tz_name=None):
    """Turn a command text into {'reply': str, 'url': str|None, 'quit': bool}."""
    command = (command or "").lower().strip()
    if not command:
        return _result("I did not hear anything.")

    for key, (name, url) in SITES.items():
        if f"open {key}" in command:
            return _result(f"Opening {name}", url)

    if command.startswith("search for "):
        query = command[len("search for "):].strip()
        if query:
            return _result(f"Searching for {query}",
                           f"https://www.google.com/search?q={quote_plus(query)}")

    if re.search(r"\btime\b", command):
        return _result("The time is " + _now(tz_name).strftime("%I:%M %p").lstrip("0"))

    if re.search(r"\b(date|today)\b", command):
        return _result("Today is " + _now(tz_name).strftime("%A, %d %B %Y"))

    if re.search(r"\b(stop|exit|bye)\b", command):
        return _result("Goodbye sir", quit_=True)

    return _result("Sorry, I do not know that command yet.")
