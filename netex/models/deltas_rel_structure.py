from dataclasses import dataclass, field
from typing import List
from netex.models.delta import Delta

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeltasRelStructure:
    class Meta:
        name = "deltas_RelStructure"

    delta: List[Delta] = field(
        default_factory=list,
        metadata={
            "name": "Delta",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
