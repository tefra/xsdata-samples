from dataclasses import dataclass, field
from typing import List
from netex.models.entrance_ref import EntranceRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.models.parking_entrance_ref import ParkingEntranceRef
from netex.models.parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from netex.models.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from netex.models.point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from netex.models.stop_place_entrance_ref import StopPlaceEntranceRef
from netex.models.stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from netex.models.vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntranceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "entranceRefs_RelStructure"

    stop_place_vehicle_entrance_ref: List[StopPlaceVehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_entrance_ref: List[StopPlaceEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_entrance_for_vehicles_ref: List[ParkingEntranceForVehiclesRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_passenger_entrance_ref: List[ParkingPassengerEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPassengerEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_entrance_ref: List[ParkingEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_vehicle_entrance_ref: List[PointOfInterestVehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_entrance_ref: List[PointOfInterestEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_entrance_ref: List[VehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entrance_ref: List[EntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "EntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
