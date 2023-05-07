from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from .day_type_ref import DayTypeRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .derived_view_structure import DerivedViewStructure
from .destination_display_view import DestinationDisplayView
from .fare_day_type_ref import FareDayTypeRef
from .frequency_structure import FrequencyStructure
from .journey_pattern_ref import JourneyPatternRef
from .multilingual_string import MultilingualString
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_journey_ref_structure import ServiceJourneyRefStructure
from .service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ConnectingJourneyDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "ConnectingJourney_DerivedViewStructure"

    service_journey_ref: Optional[ServiceJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    departure_time_or_frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DepartureTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Frequency",
                    "type": FrequencyStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_view: Optional[DestinationDisplayView] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_day_type_ref: Optional[FareDayTypeRef] = field(
        default=None,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type_ref: Optional[DayTypeRef] = field(
        default=None,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_pattern_ref: Optional[ServiceJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_pattern_ref: Optional[ServicePatternRef] = field(
        default=None,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_journey_pattern_ref: Optional[DeadRunJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connecting_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectingOrder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connecting_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectingVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
