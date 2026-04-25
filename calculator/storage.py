import json
import os
from .models import HistoryEntry


class FileStorage:
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            self._write([])

    def save(self, entry: HistoryEntry) -> None:
        entries = self._read()
        entries.append(vars(entry))
        tmp = self.filepath + ".tmp"
        with open(tmp, "w") as f:
            json.dump(entries, f, indent=2)
        os.replace(tmp, self.filepath)

    def load_all(self) -> list[HistoryEntry]:
        data = self._read()
        return [
            HistoryEntry(
                id=d.get("id", ""),
                a=d.get("a", 0.0),
                b=d.get("b", 0.0),
                operation=d.get("operation", ""),
                result=d.get("result", 0.0),
                duration_ms=d.get("duration_ms", 0.0),
                timestamp=d.get("timestamp", ""),
            )
            for d in data
        ]

    def clear(self) -> None:
        self._write([])

    def _read(self) -> list[dict]:
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _write(self, data: list[dict]) -> None:
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)
