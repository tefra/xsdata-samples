from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupSizeChangesEnumeration(StrEnum):
    NO_CHANGES = "noChanges"
    FREE = "free"
    CHARGE = "charge"
    PURCHASE_WINDOW_STEPPED_CHARGE = "purchaseWindowSteppedCharge"
    NUMBER_OF_PASSENGERS_STEPPED_CHARGE = "numberOfPassengersSteppedCharge"
