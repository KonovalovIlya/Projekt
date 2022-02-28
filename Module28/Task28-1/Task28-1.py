from typing import TextIO


class File:
    def __init__(self, file_name : str, mode : str) -> None:
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self) -> TextIO:
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return True

