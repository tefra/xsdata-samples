from dataclasses import dataclass, field
from typing import Optional
from netex.models.location_structure_2 import LocationStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BoundingBoxStructure2:
    class Meta:
        name = "BoundingBoxStructure"

    upper_left: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    lower_right: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
