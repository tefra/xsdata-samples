from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.audio_attributes_type import AudioAttributesType
from npo.models.av_file_format_enum import AvFileFormatEnum
from npo.models.video_attributes_type import VideoAttributesType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class AvAttributesType:
    class Meta:
        name = "avAttributesType"

    bitrate: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    byte_size: None | int = field(
        default=None,
        metadata={
            "name": "byteSize",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    av_file_format: None | AvFileFormatEnum = field(
        default=None,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    video_attributes: None | VideoAttributesType = field(
        default=None,
        metadata={
            "name": "videoAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    audio_attributes: None | AudioAttributesType = field(
        default=None,
        metadata={
            "name": "audioAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
