from dataclasses import dataclass, field
from typing import Optional
from npo.models.image_type_2 import ImageType2

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class ParagraphType:
    class Meta:
        name = "paragraphType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    body: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    image: Optional[ImageType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
