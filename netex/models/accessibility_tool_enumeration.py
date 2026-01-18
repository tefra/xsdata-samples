from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessibilityToolEnumeration(Enum):
    WHEELCHAIR = "wheelchair"
    WALKINGSTICK = "walkingstick"
    AUDIO_NAVIGATOR = "audioNavigator"
    VISUAL_NAVIGATOR = "visualNavigator"
    PASSENGER_CART = "passengerCart"
    PUSHCHAIR = "pushchair"
    UMBRELLA = "umbrella"
    BUGGY = "buggy"
    OTHER = "other"
