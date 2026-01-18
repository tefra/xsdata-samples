from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SetOperatorEnumeration(Enum):
    ONE_OF_ANY_ONE_SET = "oneOfAnyOneSet"
    ONE_OF_EACH_SET = "oneOfEachSet"
    SOME_OF_ANY_SET = "someOfAnySet"
    ALL_OF_ONE_SET = "allOfOneSet"
    ALL_OF_ALL_SETS = "allOfAllSets"
