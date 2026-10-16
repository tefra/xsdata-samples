from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class OtherGuaranteeInfoType1(StrEnum):
    IATA_ARC_NUMBER = "IATA/ARC Number"
    AGENCY_ADDRESS = "Agency Address"
    DEPOSIT_TAKEN = "Deposit Taken"
    OTHERS = "Others"
