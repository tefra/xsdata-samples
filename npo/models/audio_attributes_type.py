from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class AudioAttributesType:
    class Meta:
        name = "audioAttributesType"

    number_of_channels: None | int = field(
        default=None,
        metadata={
            "name": "numberOfChannels",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    audio_coding: None | str = field(
        default=None,
        metadata={
            "name": "audioCoding",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
