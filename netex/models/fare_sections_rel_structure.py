from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_section_ref import FareSectionRef
from .link_sequence_version_structure import FareSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareSectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareSections_RelStructure"

    fare_section_ref: List[FareSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_section: List[FareSection] = field(
        default_factory=list,
        metadata={
            "name": "FareSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
