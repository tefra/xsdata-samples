from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingPaymentModeEnum(Enum):
    """
    Mode of payment for parking.

    :cvar PAY_AND_DISPLAY: Pay at machine and display ticket inside
        vehicle.
    :cvar PAY_MANUAL_AT_EXIT_BOOTH: Pay at the manned exit booth of the
        parking site.
    :cvar PAY_PRIOR_TO_EXIT: Pay at machine on foot prior to returning
        to vehicle and use payment ticket to exit.
    :cvar PAY_BY_PREPAID_TOKEN: Pay by prepaid token that is used at
        exit.
    :cvar PAY_AND_EXIT: Pay directly at the exit with a payment card
        (usually, this payment card must have been used when entering as
        well). In 'AccessEquipmentEnum', there are three more literals
        to indicate, whether an entrance or exit has got this feature.
    :cvar OTHER: Other.
    """

    PAY_AND_DISPLAY = "payAndDisplay"
    PAY_MANUAL_AT_EXIT_BOOTH = "payManualAtExitBooth"
    PAY_PRIOR_TO_EXIT = "payPriorToExit"
    PAY_BY_PREPAID_TOKEN = "payByPrepaidToken"
    PAY_AND_EXIT = "payAndExit"
    OTHER = "other"
