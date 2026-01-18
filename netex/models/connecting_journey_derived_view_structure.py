from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class ConnectingJourneyDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "ConnectingJourney_DerivedViewStructure"

    service_journey_ref: ServiceJourneyRefStructure = field(
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    departure_time_or_frequency: None | XmlTime | FrequencyStructure = field(
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
        },
    )
    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_view: None | DestinationDisplayView = field(
        default=None,
        metadata={
            "name": "DestinationDisplayView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_type_ref: None | FareDayTypeRef | DayTypeRef = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    journey_pattern_ref: (
        None
        | ServiceJourneyPatternRef
        | ServicePatternRef
        | DeadRunJourneyPatternRef
        | JourneyPatternRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    connecting_order: None | int = field(
        default=None,
        metadata={
            "name": "ConnectingOrder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connecting_visit_number: None | int = field(
        default=None,
        metadata={
            "name": "ConnectingVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
