from dataclasses import dataclass, field
from typing import List
from .access_space import AccessSpace
from .access_zone import AccessZone
from .addressable_place import AddressablePlace
from .administrative_zone_version_structure import (
    AdministrativeZone1,
    TransportAdministrativeZone,
)
from .boarding_position import BoardingPosition
from .cell_versioned_child_structure import (
    FareTableInContext,
    FareTable1,
    PriceGroup1,
)
from .containment_aggregation_structure import ContainmentAggregationStructure
from .country import Country
from .crew_base import CrewBase
from .entrance import Entrance
from .equipment_place import EquipmentPlace
from .fare_zone import FareZone
from .flexible_area import FlexibleArea
from .flexible_quay import FlexibleQuay
from .flexible_stop_place import FlexibleStopPlace
from .garage import Garage
from .general_group_of_entities import GeneralGroupOfEntities
from .general_zone import GeneralZone
from .group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from .group_of_distribution_channels import GroupOfDistributionChannels
from .group_of_lines import GroupOfLines
from .group_of_link_sequences import GroupOfLinkSequences
from .group_of_links import GroupOfLinks
from .group_of_operators import GroupOfOperators
from .group_of_places import GroupOfPlaces
from .group_of_points import GroupOfPoints
from .group_of_services import GroupOfServices
from .group_of_timing_links import GroupOfTimingLinks
from .hail_and_ride_area import HailAndRideArea
from .headway_journey_group import HeadwayJourneyGroup
from .layer import Layer
from .network import Network
from .parking import Parking
from .parking_area import ParkingArea
from .parking_bay import ParkingBay
from .parking_component import ParkingComponent
from .parking_entrance_for_vehicles import ParkingEntranceForVehicles
from .parking_passenger_entrance import ParkingPassengerEntrance
from .point_of_interest import PointOfInterest
from .point_of_interest_entrance import PointOfInterestEntrance
from .point_of_interest_space import PointOfInterestSpace
from .point_of_interest_vehicle_entrance import PointOfInterestVehicleEntrance
from .postal_address import PostalAddress
from .quay import Quay
from .rhythmical_journey_group import RhythmicalJourneyGroup
from .road_address import RoadAddress
from .routing_constraint_zone import RoutingConstraintZone
from .service_site import ServiceSite
from .standard_fare_table import StandardFareTable
from .stop_area import StopArea
from .stop_place import StopPlace
from .stop_place_entrance import StopPlaceEntrance
from .stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from .tariff_zone_1 import TariffZone1
from .topographic_place import TopographicPlace
from .vehicle_stopping_place import VehicleStoppingPlace
from .vehicle_stopping_position import VehicleStoppingPosition
from .zone import Zone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfEntitiesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupOfEntitiesInFrame_RelStructure"

    group_of_distribution_channels: List[GroupOfDistributionChannels] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distance_matrix_elements: List[GroupOfDistanceMatrixElements] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_group: List[PriceGroup1] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_fare_table: List[StandardFareTable] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table_in_context: List[FareTableInContext] = field(
        default_factory=list,
        metadata={
            "name": "FareTableInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table: List[FareTable1] = field(
        default_factory=list,
        metadata={
            "name": "FareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_services: List[GroupOfServices] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rhythmical_journey_group: List[RhythmicalJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "RhythmicalJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headway_journey_group: List[HeadwayJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "HeadwayJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network: List[Network] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_lines: List[GroupOfLines] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crew_base: List[CrewBase] = field(
        default_factory=list,
        metadata={
            "name": "CrewBase",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timing_links: List[GroupOfTimingLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_operators: List[GroupOfOperators] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_places: List[GroupOfPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_link_sequences: List[GroupOfLinkSequences] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinkSequences",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing_constraint_zone: List[RoutingConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_area: List[StopArea] = field(
        default_factory=list,
        metadata={
            "name": "StopArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_zone: List[AccessZone] = field(
        default_factory=list,
        metadata={
            "name": "AccessZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hail_and_ride_area: List[HailAndRideArea] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_area: List[FlexibleArea] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_quay: List[FlexibleQuay] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleQuay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_stop_place: List[FlexibleStopPlace] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_place: List[VehicleStoppingPlace] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position: List[BoardingPosition] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_space: List[AccessSpace] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay: List[Quay] = field(
        default_factory=list,
        metadata={
            "name": "Quay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space: List[PointOfInterestSpace] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_bay: List[ParkingBay] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_area: List[ParkingArea] = field(
        default_factory=list,
        metadata={
            "name": "ParkingArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_component: List[ParkingComponent] = field(
        default_factory=list,
        metadata={
            "name": "ParkingComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_position: List[VehicleStoppingPosition] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_vehicle_entrance: List[PointOfInterestVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_entrance: List[PointOfInterestEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_passenger_entrance: List[ParkingPassengerEntrance] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPassengerEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_for_vehicles: List[ParkingEntranceForVehicles] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_vehicle_entrance: List[StopPlaceVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_entrance: List[StopPlaceEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance: List[Entrance] = field(
        default_factory=list,
        metadata={
            "name": "Entrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest: List[PointOfInterest] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking: List[Parking] = field(
        default_factory=list,
        metadata={
            "name": "Parking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place: List[StopPlace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_site: List[ServiceSite] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSite",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage: List[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_place: List[EquipmentPlace] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country: List[Country] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    addressable_place: List[AddressablePlace] = field(
        default_factory=list,
        metadata={
            "name": "AddressablePlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_address: List[PostalAddress] = field(
        default_factory=list,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_address: List[RoadAddress] = field(
        default_factory=list,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_administrative_zone: List[TransportAdministrativeZone] = field(
        default_factory=list,
        metadata={
            "name": "TransportAdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    administrative_zone: List[AdministrativeZone1] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_zone: List[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone: List[TariffZone1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_zone: List[GeneralZone] = field(
        default_factory=list,
        metadata={
            "name": "GeneralZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "name": "Zone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_links: List[GroupOfLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_points: List[GroupOfPoints] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layer: List[Layer] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_group_of_entities: List[GeneralGroupOfEntities] = field(
        default_factory=list,
        metadata={
            "name": "GeneralGroupOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
