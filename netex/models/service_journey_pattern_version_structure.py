from __future__ import annotations

from dataclasses import dataclass, field

from .sections_in_sequence_rel_structure import JourneyPatternVersionStructure
from .service_journey_pattern_type_enumeration import (
    ServiceJourneyPatternTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    class Meta:
        name = "ServiceJourneyPattern_VersionStructure"

    service_journey_pattern_type: (
        None | ServiceJourneyPatternTypeEnumeration
    ) = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
