from collections.abc import Iterable
from dataclasses import dataclass, field

from .delta_value import DeltaValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeltaValuesRelStructure:
    class Meta:
        name = "deltaValues_RelStructure"

    delta_value: Iterable[DeltaValue] = field(
        default_factory=list,
        metadata={
            "name": "DeltaValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
