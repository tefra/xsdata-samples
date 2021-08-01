from dataclasses import dataclass, field
from typing import Optional
from npo.models.twitter_type_type import TwitterTypeType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class TwitterType:
    class Meta:
        name = "twitterType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type: Optional[TwitterTypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
