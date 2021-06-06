from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .link_sequence_version_structure import GeneralSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralSectionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "generalSectionsInFrame_RelStructure"

    general_section: List[GeneralSection] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
