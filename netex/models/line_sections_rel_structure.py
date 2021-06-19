from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .line_section_ref import LineSectionRef
from .link_sequence_version_structure import LineSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineSectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "lineSections_RelStructure"

    line_section_ref_or_line_section: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LineSectionRef",
                    "type": LineSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineSection",
                    "type": LineSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
