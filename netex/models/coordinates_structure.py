from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CoordinatesStructure:
    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
