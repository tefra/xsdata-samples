from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VmsFaultEnum(Enum):
    """
    Types of variable message sign faults.

    :cvar COMMUNICATIONS_FAILURE: Comunications failure affecting VMS.
    :cvar INCORRECT_MESSAGE_DISPLAYED: Incorrect message is being
        displayed.
    :cvar INCORRECT_PICTOGRAM_DISPLAYED: Incorrect pictogram is being
        displayed.
    :cvar OUT_OF_SERVICE: Not currently in service (e.g. intentionally
        disconnected or switched off during roadworks).
    :cvar POWER_FAILURE: Power to VMS has failed.
    :cvar UNABLE_TO_CLEAR_DOWN: Unable to clear down information
        displayed on VMS.
    :cvar UNKNOWN: Unknown VMS fault.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    COMMUNICATIONS_FAILURE = "communicationsFailure"
    INCORRECT_MESSAGE_DISPLAYED = "incorrectMessageDisplayed"
    INCORRECT_PICTOGRAM_DISPLAYED = "incorrectPictogramDisplayed"
    OUT_OF_SERVICE = "outOfService"
    POWER_FAILURE = "powerFailure"
    UNABLE_TO_CLEAR_DOWN = "unableToClearDown"
    UNKNOWN = "unknown"
    OTHER = "other"
