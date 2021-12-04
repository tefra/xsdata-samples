from dataclasses import dataclass, field
from typing import List, Optional
from .address_ref import AddressRef
from .boarding_position_ref import BoardingPositionRef
from .postal_address_ref import PostalAddressRef
from .quay_ref import QuayRef
from .road_address_ref import RoadAddressRef
from .scheduled_stop_point_view import ScheduledStopPointView
from .tariff_zone_ref import TariffZoneRef
from .topographic_place_view import TopographicPlaceView

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
    postal_address_ref: Optional[PostalAddressRef] = field(
        default=None,
        metadata={
            "name": "PostalAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_address_ref: Optional[RoadAddressRef] = field(
        default=None,
        metadata={
            "name": "RoadAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    tariff_zone_ref: List[TariffZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
