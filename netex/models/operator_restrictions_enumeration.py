from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OperatorRestrictionsEnumeration(Enum):
    ANY_TRAIN = "anyTrain"
    RESTRICTED = "restricted"
    SPECIFIED_OPERATOR_ONLY = "specifiedOperatorOnly"
