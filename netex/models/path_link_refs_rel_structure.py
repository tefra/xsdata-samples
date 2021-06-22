from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .path_link_ref import PathLinkRef
from .path_link_ref_by_value import PathLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "pathLinkRefs_RelStructure"

    path_link_ref_or_path_link_ref_by_value: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRefByValue",
                    "type": PathLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
