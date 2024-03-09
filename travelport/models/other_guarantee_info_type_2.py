from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class OtherGuaranteeInfoType2(Enum):
    IATA_ARC_NUMBER = "IATA/ARC Number"
    AGENCY_ADDRESS = "Agency Address"
    DEPOSIT_TAKEN = "Deposit Taken"
    OTHERS = "Others"
