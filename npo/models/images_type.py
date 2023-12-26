from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.image import Image

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ImagesType:
    class Meta:
        name = "imagesType"

    image: list[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
