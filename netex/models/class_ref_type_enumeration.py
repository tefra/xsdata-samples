from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ClassRefTypeEnumeration(Enum):
    MEMBERS = "members"
    MEMBER_REFERENCES = "memberReferences"
    ALL = "all"
