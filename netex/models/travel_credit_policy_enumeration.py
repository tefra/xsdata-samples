from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TravelCreditPolicyEnumeration(StrEnum):
    ALLOW_TRAVEL = "allowTravel"
    BLOCK_ALL_TRAVEL = "blockAllTravel"
    BLOCK_PAY_AS_YOU_GO_TRAVEL = "blockPayAsYouGoTravel"
    OTHER = "other"
