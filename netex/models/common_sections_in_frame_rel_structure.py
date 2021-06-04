from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.link_sequence_version_structure import CommonSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonSectionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "commonSectionsInFrame_RelStructure"

    common_section: List[CommonSection] = field(
        default_factory=list,
        metadata={
            "name": "CommonSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
