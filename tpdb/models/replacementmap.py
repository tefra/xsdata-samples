from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.entry import Entry


@dataclass(kw_only=True)
class Replacementmap:
    class Meta:
        name = "replacementmap"

    entry: list[Entry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
