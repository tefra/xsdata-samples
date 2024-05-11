from dataclasses import dataclass, field
from typing import Optional

from .accessibility_assessment import AccessibilityAssessment
from .beacon_direction_enumeration import BeaconDirectionEnumeration
from .beacon_protocol_enumeration import BeaconProtocolEnumeration
from .beacon_type_enumeration import BeaconTypeEnumeration
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerBeaconEquipmentVersionStructure(
    PassengerEquipmentVersionStructure
):
    class Meta:
        name = "PassengerBeaconEquipment_VersionStructure"

    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    beacon_type: Optional[BeaconTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "BeaconType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    beacon_direction: Optional[BeaconDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "BeaconDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    beacon_protocol: Optional[BeaconProtocolEnumeration] = field(
        default=None,
        metadata={
            "name": "BeaconProtocol",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    beacon_backend_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "BeaconBackendUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
