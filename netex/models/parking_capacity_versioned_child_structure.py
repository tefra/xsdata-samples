from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .parking_properties_ref import ParkingPropertiesRef
from .parking_properties_ref_structure import ParkingPropertiesRefStructure
from .parking_ref import ParkingRef
from .parking_stay_enumeration import ParkingStayEnumeration
from .parking_user_enumeration import ParkingUserEnumeration
from .parking_vehicle_enumeration import ParkingVehicleEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingCapacityVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "ParkingCapacity_VersionedChildStructure"

    parking_ref: Optional[ParkingRef] = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_ref: Optional[ParkingPropertiesRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_properties_ref: Optional[ParkingPropertiesRef] = field(
        default=None,
        metadata={
            "name": "ParkingPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_user_type: Optional[ParkingUserEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingUserType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_vehicle_type: Optional[ParkingVehicleEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingVehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_stay_type: Optional[ParkingStayEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingStayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_spaces_with_recharge_point: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSpacesWithRechargePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
