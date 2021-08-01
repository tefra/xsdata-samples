from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class AudioAttributesType:
    class Meta:
        name = "audioAttributesType"

    number_of_channels: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfChannels",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    audio_coding: Optional[str] = field(
        default=None,
        metadata={
            "name": "audioCoding",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
