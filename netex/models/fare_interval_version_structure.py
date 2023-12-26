from dataclasses import dataclass, field
from typing import Optional
from .cell_versioned_child_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareIntervalVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "FareInterval_VersionStructure"

    name_of_class_of_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClassOfUnit",
            "type": "Attribute",
        },
    )
