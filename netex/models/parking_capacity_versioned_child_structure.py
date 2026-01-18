from dataclasses import dataclass, field
from typing import Optional, Union

from .compound_train_ref import CompoundTrainRef
from .entity_in_version_structure import VersionedChildStructure
from .parking_properties_ref import ParkingPropertiesRef
from .parking_properties_ref_structure import ParkingPropertiesRefStructure
from .parking_ref import ParkingRef
from .parking_stay_enumeration import ParkingStayEnumeration
from .parking_user_enumeration import ParkingUserEnumeration
from .parking_vehicle_enumeration import ParkingVehicleEnumeration
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingCapacityVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "ParkingCapacity_VersionedChildStructure"

    parking_ref: ParkingRef | None = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_ref: ParkingPropertiesRefStructure | None = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_properties_ref: ParkingPropertiesRef | None = field(
        default=None,
        metadata={
            "name": "ParkingPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_user_type: ParkingUserEnumeration | None = field(
        default=None,
        metadata={
            "name": "ParkingUserType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_vehicle_type: ParkingVehicleEnumeration | None = field(
        default=None,
        metadata={
            "name": "ParkingVehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_type_ref_or_vehicle_type_ref: SimpleVehicleTypeRef | CompoundTrainRef | TrainRef | VehicleTypeRef | TransportTypeRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    parking_stay_type: ParkingStayEnumeration | None = field(
        default=None,
        metadata={
            "name": "ParkingStayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_spaces: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_spaces_with_recharge_point: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSpacesWithRechargePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
