from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ClassRefTypeEnumeration(StrEnum):
    MEMBERS = "members"
    MEMBER_REFERENCES = "memberReferences"
    ALL = "all"
