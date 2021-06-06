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

    path_link_ref: List[PathLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_link_ref_by_value: List[PathLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
