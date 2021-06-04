from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.timing_link_ref_by_value import TimingLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingLinkRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "timingLinkRefs_RelStructure"

    timing_link_ref: List[TimingLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_ref_by_value: List[TimingLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "TimingLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
