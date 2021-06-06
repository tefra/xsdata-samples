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

    line_section_ref: List[LineSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LineSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_section: List[LineSection] = field(
        default_factory=list,
        metadata={
            "name": "LineSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
