from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .type_of_info_link_enumeration import TypeOfInfoLinkEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfoLinkStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_of_info_link: Sequence[TypeOfInfoLinkEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "typeOfInfoLink",
            "type": "Attribute",
            "tokens": True,
        },
    )
    target_platform: None | object = field(
        default=None,
        metadata={
            "name": "targetPlatform",
            "type": "Attribute",
        },
    )
