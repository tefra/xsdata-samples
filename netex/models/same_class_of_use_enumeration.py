from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameClassOfUseEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    SAME_OR_EQUIVALENT = "sameOrEquivalent"
    DIFFERENT = "different"
