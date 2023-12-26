from dataclasses import dataclass, field
from datexii.models.eu.datexii.v2.reference import Reference

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingAccessReference(Reference):
    class Meta:
        name = "_ParkingAccessReference"

    target_class: str = field(
        init=False,
        default="ParkingAccess",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        },
    )
