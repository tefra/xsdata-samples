from dataclasses import dataclass, field
from typing import Optional
from npo.models.audio_attributes_type import AudioAttributesType
from npo.models.av_file_format_enum import AvFileFormatEnum
from npo.models.video_attributes_type import VideoAttributesType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class AvAttributesType:
    class Meta:
        name = "avAttributesType"

    bitrate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    byte_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "byteSize",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    av_file_format: Optional[AvFileFormatEnum] = field(
        default=None,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    video_attributes: Optional[VideoAttributesType] = field(
        default=None,
        metadata={
            "name": "videoAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    audio_attributes: Optional[AudioAttributesType] = field(
        default=None,
        metadata={
            "name": "audioAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
