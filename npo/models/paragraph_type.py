from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.image_type_2 import ImageType2

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class ParagraphType:
    class Meta:
        name = "paragraphType"

    title: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    body: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    image: None | ImageType2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
