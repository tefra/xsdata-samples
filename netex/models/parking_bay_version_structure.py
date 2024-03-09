from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDuration

from .bay_geometry_enumeration import BayGeometryEnumeration
from .compound_train_ref import CompoundTrainRef
from .parking_area_ref import ParkingAreaRef
from .parking_component_version_structure import (
    ParkingComponentVersionStructure,
)
from .parking_stay_enumeration import ParkingStayEnumeration
from .parking_user_enumeration import ParkingUserEnumeration
from .parking_vehicle_enumeration import ParkingVehicleEnumeration
from .parking_visibility_enumeration import ParkingVisibilityEnumeration
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .taxi_parking_area_ref import TaxiParkingAreaRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from .vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBayVersionStructure(ParkingComponentVersionStructure):
    class Meta:
        name = "ParkingBay_VersionStructure"

    parking_area_ref: Optional[
        Union[
            VehiclePoolingParkingAreaRef,
            VehicleSharingParkingAreaRef,
            TaxiParkingAreaRef,
            ParkingAreaRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingAreaRef",
                    "type": VehicleSharingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingAreaRef",
                    "type": TaxiParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    parking_user_types: List[ParkingUserEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingUserTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
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
    transport_type_ref_or_vehicle_type_ref: Optional[
        Union[
            SimpleVehicleTypeRef,
            CompoundTrainRef,
            TrainRef,
            VehicleTypeRef,
            TransportTypeRef,
        ]
    ] = field(
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
    parking_stay_list: List[ParkingStayEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingStayList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    maximum_stay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    secure_parking: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SecureParking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bay_geometry: Optional[BayGeometryEnumeration] = field(
        default=None,
        metadata={
            "name": "BayGeometry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_visibility: Optional[ParkingVisibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingVisibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recharging_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RechargingAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
