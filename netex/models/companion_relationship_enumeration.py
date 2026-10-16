from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CompanionRelationshipEnumeration(StrEnum):
    ANYONE = "anyone"
    PARENT = "parent"
    GRANDPARENT = "grandparent"
    CHILD = "child"
    GRANDCHILD = "grandchild"
    FAMILY = "family"
    SPOUSE = "spouse"
    PARTNER = "partner"
    DEPENDENT = "dependent"
    COLLEAGUE = "colleague"
    PUPIL = "pupil"
    TEACHER = "teacher"
    CARER = "carer"
