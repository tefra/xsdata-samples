from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RefundPolicyEnumeration(Enum):
    ANY = "any"
    ILLNESS = "illness"
    DEATH = "death"
    MATERNITY = "maternity"
    REDUNDANCY = "redundancy"
    CHANGE_OF_EMPLOYMENT = "changeOfEmployment"
    CHANGE_OF_RESIDENCE = "changeOfResidence"
    NONE_VALUE = "none"
    OTHER = "other"
