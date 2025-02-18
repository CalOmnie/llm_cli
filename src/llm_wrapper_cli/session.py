from pathlib import Path
import tempfile
import json

SESSION_PATH = Path(tempfile.gettempdir()) / "llmc_session.json"


class Session:
    """
    A class to manage chat sessions, load, add and save messages.
    """

    def __init__(self, continue_chat: bool, path: Path = SESSION_PATH):
        """
        Initializes a new session, loading an existing one if continue_chat is True.
        """
        self.session = []
        self.session_path = path
        if continue_chat:
            self.load_session()

    def load_session(self):
        """
        Loads the session from a file if it exists.
        """
        if self.session_path.exists() and self.session_path.is_file():
            with self.session_path.open("rt") as f:
                self.session = json.load(f)

    def add_message(self, role: str, content: str):
        """
        Adds a message to the session.
        """
        self.session.append({"role": role, "content": content})

    def get(self):
        """
        Returns the current session.
        """
        return self.session

    def save(self):
        """
        Saves the current session to a file.
        """
        with self.session_path.open("wt") as f:
            json.dump(self.session, f)
