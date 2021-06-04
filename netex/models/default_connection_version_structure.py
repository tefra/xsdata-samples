from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.access_space_ref import AccessSpaceRef
from netex.models.boarding_position_ref import BoardingPositionRef
from netex.models.default_connection_end_structure import DefaultConnectionEndStructure
from netex.models.entrance_ref import EntranceRef
from netex.models.parking_bay_ref import ParkingBayRef
from netex.models.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.models.parking_entrance_ref import ParkingEntranceRef
from netex.models.parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from netex.models.parking_ref import ParkingRef
from netex.models.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from netex.models.point_of_interest_ref import PointOfInterestRef
from netex.models.point_of_interest_space_ref import PointOfInterestSpaceRef
from netex.models.point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from netex.models.quay_ref import QuayRef
from netex.models.service_site_ref import ServiceSiteRef
from netex.models.site_component_ref import SiteComponentRef
from netex.models.site_element_ref import SiteElementRef
from netex.models.site_ref import SiteRef
from netex.models.stop_area_ref import StopAreaRef
from netex.models.stop_place_entrance_ref import StopPlaceEntranceRef
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_place_space_ref import StopPlaceSpaceRef
from netex.models.stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from netex.models.topographic_place_view import TopographicPlaceView
from netex.models.transfer_version_structure import TransferVersionStructure
from netex.models.vehicle_entrance_ref import VehicleEntranceRef
from netex.models.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from netex.models.vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultConnectionVersionStructure(TransferVersionStructure):
    class Meta:
        name = "DefaultConnection_VersionStructure"

    from_value: Optional[DefaultConnectionEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to: Optional[DefaultConnectionEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_view: Optional[TopographicPlaceView] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_area_ref: Optional[StopAreaRef] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_position_ref: List[VehicleStoppingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_stopping_place_ref: List[VehicleStoppingPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    boarding_position_ref: List[BoardingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    access_space_ref: List[AccessSpaceRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    quay_ref: List[QuayRef] = field(
        default_factory=list,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    stop_place_space_ref: List[StopPlaceSpaceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    parking_bay_ref: List[ParkingBayRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    point_of_interest_space_ref: List[PointOfInterestSpaceRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    stop_place_vehicle_entrance_ref: List[StopPlaceVehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    stop_place_entrance_ref: List[StopPlaceEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    parking_entrance_for_vehicles_ref: List[ParkingEntranceForVehiclesRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
            "sequential": True,
        }
    )
    parking_passenger_entrance_ref: List[ParkingPassengerEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPassengerEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
            "sequential": True,
        }
    )
    parking_entrance_ref: List[ParkingEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    point_of_interest_vehicle_entrance_ref: List[PointOfInterestVehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    point_of_interest_entrance_ref: List[PointOfInterestEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    vehicle_entrance_ref: List[VehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    entrance_ref: List[EntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "EntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    site_component_ref: List[SiteComponentRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    stop_place_ref: List[StopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    parking_ref: List[ParkingRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    point_of_interest_ref: List[PointOfInterestRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_site_ref: List[ServiceSiteRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    site_ref: List[SiteRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    site_element_ref: Optional[SiteElementRef] = field(
        default=None,
        metadata={
            "name": "SiteElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
