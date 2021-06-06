from dataclasses import dataclass, field
from typing import Optional
from .link_sequence_version_structure import JourneyPatternVersionStructure
from .service_journey_pattern_type_enumeration import ServiceJourneyPatternTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    class Meta:
        name = "ServiceJourneyPattern_VersionStructure"

    service_journey_pattern_type: Optional[ServiceJourneyPatternTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
