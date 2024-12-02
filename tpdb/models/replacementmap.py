from dataclasses import dataclass, field

from tpdb.models.entry import Entry


@dataclass
class Replacementmap:
    class Meta:
        name = "replacementmap"

    entry: list[Entry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
