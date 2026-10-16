from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SectionTypeEnumeration(StrEnum):
    TRUNK = "trunk"
    BRANCH = "branch"
    EYEL_BRANCH = "eyelBranch"
    END_LOOP = "endLoop"
    OTHER = "other"
