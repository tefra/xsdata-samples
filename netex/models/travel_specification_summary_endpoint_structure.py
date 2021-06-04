from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.address_ref import AddressRef
from netex.models.boarding_position_ref import BoardingPositionRef
from netex.models.postal_address_ref import PostalAddressRef
from netex.models.quay_ref import QuayRef
from netex.models.road_address_ref import RoadAddressRef
from netex.models.scheduled_stop_point_view import ScheduledStopPointView
from netex.models.tariff_zone_ref_2 import TariffZoneRef2
from netex.models.topographic_place_view import TopographicPlaceView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationSummaryEndpointStructure:
    topographic_place_view: Optional[TopographicPlaceView] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_address_ref: List[PostalAddressRef] = field(
        default_factory=list,
        metadata={
            "name": "PostalAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    road_address_ref: List[RoadAddressRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    address_ref: Optional[AddressRef] = field(
        default=None,
        metadata={
            "name": "AddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_view: Optional[ScheduledStopPointView] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointView",
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
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone_ref: List[TariffZoneRef2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
