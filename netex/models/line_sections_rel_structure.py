from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .line_section_ref import LineSectionRef
from .sections_in_sequence_rel_structure import LineSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineSectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "lineSections_RelStructure"

    line_section_ref_or_line_section: Iterable[
        LineSectionRef | LineSection
    ] = field(
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
        },
    )
