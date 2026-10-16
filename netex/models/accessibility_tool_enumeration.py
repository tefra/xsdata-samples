from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessibilityToolEnumeration(StrEnum):
    WHEELCHAIR = "wheelchair"
    WALKINGSTICK = "walkingstick"
    AUDIO_NAVIGATOR = "audioNavigator"
    VISUAL_NAVIGATOR = "visualNavigator"
    PASSENGER_CART = "passengerCart"
    PUSHCHAIR = "pushchair"
    UMBRELLA = "umbrella"
    BUGGY = "buggy"
    OTHER = "other"
