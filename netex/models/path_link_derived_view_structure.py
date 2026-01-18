from __future__ import annotations

from dataclasses import dataclass, field

from .derived_view_structure import DerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "PathLink_DerivedViewStructure"

    hide_link: None | bool = field(
        default=None,
        metadata={
            "name": "HideLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    hide_destination: None | bool = field(
        default=None,
        metadata={
            "name": "HideDestination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_entrance_separately: None | bool = field(
        default=None,
        metadata={
            "name": "ShowEntranceSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_exit_separately: None | bool = field(
        default=None,
        metadata={
            "name": "ShowExitSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_heading_separately: None | bool = field(
        default=None,
        metadata={
            "name": "ShowHeadingSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
