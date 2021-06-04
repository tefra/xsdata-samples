from dataclasses import dataclass, field
from typing import Optional
from netex.models.link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.path_heading_enumeration import PathHeadingEnumeration
from netex.models.path_link_ref import PathLinkRef
from netex.models.path_link_view import PathLinkView
from netex.models.transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkInSequenceVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "PathLinkInSequence_VersionedChildStructure"

    path_link_ref: Optional[PathLinkRef] = field(
        default=None,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    heading: Optional[PathHeadingEnumeration] = field(
        default=None,
        metadata={
            "name": "Heading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    instruction: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Instruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    views: Optional["PathLinkInSequenceVersionedChildStructure.Views"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class Views:
        path_link_view: Optional[PathLinkView] = field(
            default=None,
            metadata={
                "name": "PathLinkView",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
