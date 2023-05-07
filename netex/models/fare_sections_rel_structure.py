from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_section_ref import FareSectionRef
from .section_in_sequence_versioned_child_structure import FareSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareSectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareSections_RelStructure"

    fare_section_ref_or_fare_section: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareSectionRef",
                    "type": FareSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareSection",
                    "type": FareSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
