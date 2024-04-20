from dataclasses import dataclass, field
from typing import List

from tpdb.models.entry import Entry


@dataclass
class Replacementmap:
    class Meta:
        name = "replacementmap"

    entry: List[Entry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
