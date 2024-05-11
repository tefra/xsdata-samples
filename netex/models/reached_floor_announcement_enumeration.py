from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReachedFloorAnnouncementEnumeration(Enum):
    NONE = "none"
    VISUAL = "visual"
    TACTILE = "tactile"
    AUDIO = "audio"
    VISUAL_AND_AUDIO = "visualAndAudio"
    VISUAL_AND_AUDIO_AND_TACTILE = "visualAndAudioAndTactile"
