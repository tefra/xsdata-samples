from dataclasses import dataclass, field
from typing import List, Union
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .timing_link_ref import TimingLinkRef
from .timing_link_ref_by_value import TimingLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingLinkRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "timingLinkRefs_RelStructure"

    timing_link_ref_or_timing_link_ref_by_value: List[
        Union[TimingLinkRef, TimingLinkRefByValue]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRefByValue",
                    "type": TimingLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
