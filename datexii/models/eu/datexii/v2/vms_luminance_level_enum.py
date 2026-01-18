from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VmsLuminanceLevelEnum(Enum):
    """
    Levels of luminance applicable to VMS.

    :cvar SWITCHED_OFF: Luminance level is zero as light source is
        switched off.
    :cvar TESTING: Luminance is set at testing level.
    :cvar NIGHT: Luminance is set at level defined for night time.
    :cvar OVERCAST: Luminance is set at level defined for overcast or
        dull day time conditions.
    :cvar BROAD_DAYLIGHT: Luminance is set at level defined for normal
        broad day light conditions.
    :cvar SUN_IN_EYES: Luminance is set at level defined for conditions
        where drivers will have sun in their eyes.
    :cvar SUN_ON_BACK: Luminance is set at level defined for conditions
        where drivers will have sun behind them.
    :cvar FOGGY_DAY: Luminance is set at level defined for foggy day
        time conditions.
    :cvar FOGGY_NIGHT: Luminance is set at level defined for foggy night
        time conditions.
    """

    SWITCHED_OFF = "switchedOff"
    TESTING = "testing"
    NIGHT = "night"
    OVERCAST = "overcast"
    BROAD_DAYLIGHT = "broadDaylight"
    SUN_IN_EYES = "sunInEyes"
    SUN_ON_BACK = "sunOnBack"
    FOGGY_DAY = "foggyDay"
    FOGGY_NIGHT = "foggyNight"
