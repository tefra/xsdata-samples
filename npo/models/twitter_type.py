from __future__ import annotations

from dataclasses import dataclass, field

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
        },
    )
    type_value: None | TwitterTypeType = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
