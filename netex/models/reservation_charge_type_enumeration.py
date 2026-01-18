from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReservationChargeTypeEnumeration(Enum):
    NO_FEE = "noFee"
    FEE = "fee"
    SINGLE_FEE_FOR_RETURN_TRIP = "singleFeeForReturnTrip"
    FEE_FOR_EACH_DIRECTION = "feeForEachDirection"
    FEE_FOR_EACH_LEG = "feeForEachLeg"
