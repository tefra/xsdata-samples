from dataclasses import dataclass, field
from typing import Optional
from npo.models.media_type_enum import MediaTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class DescendantRefType:
    class Meta:
        name = "descendantRefType"

    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
