from dataclasses import dataclass
from typing import List, Optional


@dataclass
class UserSelection:
    selected_source_dir: str
    selected_target_dir: str
    selected_items: Optional[List[str]] = None
