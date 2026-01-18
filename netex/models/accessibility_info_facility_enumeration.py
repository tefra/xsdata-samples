from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessibilityInfoFacilityEnumeration(Enum):
    AUDIO_INFORMATION = "audioInformation"
    AUDIO_FOR_HEARING_IMPAIRED = "audioForHearingImpaired"
    VISUAL_DISPLAYS = "visualDisplays"
    DISPLAYS_FOR_VISUALLY_IMPAIRED = "displaysForVisuallyImpaired"
    LARGE_PRINT_TIMETABLES = "largePrintTimetables"
    OTHER = "other"
