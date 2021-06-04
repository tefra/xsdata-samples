from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TravelCreditPolicyEnumeration(Enum):
    ALLOW_TRAVEL = "allowTravel"
    BLOCK_ALL_TRAVEL = "blockAllTravel"
    BLOCK_PAY_AS_YOU_GO_TRAVEL = "blockPayAsYouGoTravel"
    OTHER = "other"
