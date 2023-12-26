from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.aspect_ratio_enum import AspectRatioEnum
from npo.models.color_type import ColorType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class VideoAttributesType:
    class Meta:
        name = "videoAttributesType"

    color: None | ColorType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    video_coding: None | str = field(
        default=None,
        metadata={
            "name": "videoCoding",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    aspect_ratio: None | AspectRatioEnum = field(
        default=None,
        metadata={
            "name": "aspectRatio",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    height: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    heigth: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "doc": "This obviously is a typo.",
        },
    )
    width: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
