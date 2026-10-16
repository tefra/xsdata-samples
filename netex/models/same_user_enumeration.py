from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameUserEnumeration(StrEnum):
    SAME_PERSON = "samePerson"
    DIFFERENT_PERSON = "differentPerson"
    ANY_ONE = "anyOne"
    SPECIFIC = "specific"
