from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PenaltyPolicyTypeEnumeration(Enum):
    NO_TICKET = "noTicket"
    NO_CHECKIN = "noCheckin"
    NO_CHECK_OUT = "noCheckOut"
    NO_VALIDATION = "noValidation"
    OTHER = "other"
