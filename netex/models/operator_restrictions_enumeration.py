from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OperatorRestrictionsEnumeration(StrEnum):
    ANY_TRAIN = "anyTrain"
    RESTRICTED = "restricted"
    SPECIFIED_OPERATOR_ONLY = "specifiedOperatorOnly"
