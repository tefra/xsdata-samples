from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.link_type_enum import LinkTypeEnum

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class LinkType:
    class Meta:
        name = "linkType"

    text: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    page_ref: None | str = field(
        default=None,
        metadata={
            "name": "pageRef",
            "type": "Attribute",
        },
    )
    type_value: None | LinkTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
