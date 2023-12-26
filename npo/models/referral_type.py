from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.link_type_enum import LinkTypeEnum

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class ReferralType:
    class Meta:
        name = "referralType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    referrer: None | str = field(
        default=None,
        metadata={
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
