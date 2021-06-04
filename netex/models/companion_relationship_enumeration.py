from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CompanionRelationshipEnumeration(Enum):
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
