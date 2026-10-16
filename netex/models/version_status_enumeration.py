from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VersionStatusEnumeration(StrEnum):
    DRAFT = "draft"
    PROPOSED = "proposed"
    VERSIONED = "versioned"
    DEPRECATED = "deprecated"
    OTHER = "other"
