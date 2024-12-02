from dataclasses import dataclass, field

from tpdb.models.rule import Rule


@dataclass
class Relrules:
    class Meta:
        name = "relrules"

    rule: list[Rule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
