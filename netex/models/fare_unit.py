from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_unit_version_structure import FareUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareUnit(FareUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        }
    )
