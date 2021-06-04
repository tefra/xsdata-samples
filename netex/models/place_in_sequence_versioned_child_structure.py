from dataclasses import dataclass, field
from typing import Optional
from netex.models.path_links_in_sequence_rel_structure import PathLinksInSequenceRelStructure
from netex.models.place_ref_structure import PlaceRefStructure
from netex.models.point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceInSequenceVersionedChildStructure(PointInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "PlaceInSequence_VersionedChildStructure"

    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    branch_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchLevel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onward_links: Optional[PathLinksInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "onwardLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
