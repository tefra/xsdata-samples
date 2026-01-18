from dataclasses import dataclass, field

from .derived_view_structure import DerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "PathLink_DerivedViewStructure"

    hide_link: bool | None = field(
        default=None,
        metadata={
            "name": "HideLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    hide_destination: bool | None = field(
        default=None,
        metadata={
            "name": "HideDestination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_entrance_separately: bool | None = field(
        default=None,
        metadata={
            "name": "ShowEntranceSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_exit_separately: bool | None = field(
        default=None,
        metadata={
            "name": "ShowExitSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_heading_separately: bool | None = field(
        default=None,
        metadata={
            "name": "ShowHeadingSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
