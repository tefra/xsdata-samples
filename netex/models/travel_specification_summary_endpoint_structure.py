from dataclasses import dataclass, field
from typing import List, Optional, Union

from .address_ref import AddressRef
from .boarding_position_ref import BoardingPositionRef
from .parking_ref import ParkingRef
from .point_of_interest_ref import PointOfInterestRef
from .postal_address_ref import PostalAddressRef
from .quay_ref import QuayRef
from .road_address_ref import RoadAddressRef
from .scheduled_stop_point_view import ScheduledStopPointView
from .service_site_ref import ServiceSiteRef
from .site_ref import SiteRef
from .stop_place_ref import StopPlaceRef
from .tariff_zone_ref_1 import TariffZoneRef1
from .taxi_rank_ref import TaxiRankRef
from .taxi_stand_ref import TaxiStandRef
from .topographic_place_view import TopographicPlaceView
from .vehicle_meeting_point_ref import VehicleMeetingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationSummaryEndpointStructure:
    topographic_place_view: Optional[TopographicPlaceView] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_ref_or_site_ref: Optional[
        Union[
            TaxiRankRef,
            StopPlaceRef,
            ParkingRef,
            PointOfInterestRef,
            ServiceSiteRef,
            SiteRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    address_ref: Optional[
        Union[PostalAddressRef, RoadAddressRef, AddressRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddressRef",
                    "type": PostalAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddressRef",
                    "type": RoadAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressRef",
                    "type": AddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    scheduled_stop_point_view: Optional[ScheduledStopPointView] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_meeting_point_ref: Optional[VehicleMeetingPointRef] = field(
        default=None,
        metadata={
            "name": "VehicleMeetingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_ref: Optional[Union[TaxiStandRef, QuayRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_zone_ref: List[TariffZoneRef1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
