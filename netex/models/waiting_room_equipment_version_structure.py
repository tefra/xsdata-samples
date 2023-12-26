from dataclasses import dataclass, field
from typing import List, Optional
from .class_of_use_ref import ClassOfUseRef
from .fare_class_enumeration import FareClassEnumeration
from .sanitary_facility_enumeration import SanitaryFacilityEnumeration
from .waiting_equipment_version_structure import (
    WaitingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WaitingRoomEquipmentVersionStructure(WaitingEquipmentVersionStructure):
    class Meta:
        name = "WaitingRoomEquipment_VersionStructure"

    fare_class: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    women_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WomenOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sanitary: List[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Sanitary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
