from dataclasses import dataclass, field
from typing import Optional
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
        }
    )
    referrer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[LinkTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
