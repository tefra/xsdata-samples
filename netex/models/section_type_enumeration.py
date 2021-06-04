from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SectionTypeEnumeration(Enum):
    TRUNK = "trunk"
    BRANCH = "branch"
    EYEL_BRANCH = "eyelBranch"
    END_LOOP = "endLoop"
    OTHER = "other"
