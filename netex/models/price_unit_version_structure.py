from dataclasses import dataclass, field
from typing import Optional
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceUnitVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "PriceUnit_VersionStructure"

    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
