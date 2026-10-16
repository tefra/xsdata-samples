from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReachedFloorAnnouncementEnumeration(StrEnum):
    NONE = "none"
    VISUAL = "visual"
    TACTILE = "tactile"
    AUDIO = "audio"
    VISUAL_AND_AUDIO = "visualAndAudio"
    VISUAL_AND_AUDIO_AND_TACTILE = "visualAndAudioAndTactile"
