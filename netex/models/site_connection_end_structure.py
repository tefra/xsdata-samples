from dataclasses import dataclass, field
from typing import Optional
from .access_space_ref import AccessSpaceRef
from .all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from .boarding_position_ref import BoardingPositionRef
from .multilingual_string import MultilingualString
from .operator_ref import OperatorRef
from .operator_view import OperatorView
from .parking_area_ref import ParkingAreaRef
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from .parking_entrance_ref import ParkingEntranceRef
from .parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from .parking_ref import ParkingRef
from .point_of_interest_entrance_ref import PointOfInterestEntranceRef
from .point_of_interest_ref import PointOfInterestRef
from .point_of_interest_space_ref import PointOfInterestSpaceRef
from .quay_ref import QuayRef
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .stop_area_ref_structure import StopAreaRefStructure
from .stop_place_entrance_ref import StopPlaceEntranceRef
from .stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteConnectionEndStructure:
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_space_ref: Optional[AccessSpaceRef] = field(
        default=None,
        metadata={
            "name": "AccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_ref: Optional[QuayRef] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_entrance_ref: Optional[StopPlaceEntranceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_ref: Optional[PointOfInterestRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space_ref: Optional[PointOfInterestSpaceRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_entrance_ref: Optional[PointOfInterestEntranceRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_ref: Optional[ParkingRef] = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_area_ref: Optional[ParkingAreaRef] = field(
        default=None,
        metadata={
            "name": "ParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_for_vehicles_ref: Optional[ParkingEntranceForVehiclesRef] = field(
        default=None,
        metadata={
            "name": "ParkingEntranceForVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_passenger_entrance_ref: Optional[ParkingPassengerEntranceRef] = field(
        default=None,
        metadata={
            "name": "ParkingPassengerEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_ref: Optional[ParkingEntranceRef] = field(
        default=None,
        metadata={
            "name": "ParkingEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_view: Optional[OperatorView] = field(
        default=None,
        metadata={
            "name": "OperatorView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
