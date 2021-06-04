from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CyclesOnServiceEnumeration(Enum):
    NOT_ALLOWED = "notAllowed"
    ONLY_FOLDING_ALLOWED = "onlyFoldingAllowed"
    ALLOWED_SUBJECT_TO_RESTRICTIONS = "allowedSubjectToRestrictions"
    MUST_BOOK = "mustBook"
    ALLOWED_AT_ALL_TIMES = "allowedAtAllTimes"
