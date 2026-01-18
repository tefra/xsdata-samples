from dataclasses import dataclass, field
from typing import Optional, Union

from .destination_display_ref import DestinationDisplayRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .multilingual_string import MultilingualString
from .place_ref import PlaceRef
from .scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyEndpointStructure:
    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    scheduled_stop_point_ref: FareScheduledStopPointRef | ScheduledStopPointRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    destination_display_ref: DestinationDisplayRef | None = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_ref: PlaceRef | None = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
