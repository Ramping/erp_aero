from dataclasses import dataclass
from typing import List


@dataclass
class PDFFileData:
    keys: List = None
    reference_file: str = None
    checked_file: List = None
