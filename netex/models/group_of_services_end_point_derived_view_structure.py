from dataclasses import dataclass, field
from typing import Optional
from netex.models.derived_view_structure import DerivedViewStructure
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.multilingual_string import MultilingualString
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.topographic_place_view import TopographicPlaceView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfServicesEndPointDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "GroupOfServicesEndPoint_DerivedViewStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref: Optional[FareScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
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
