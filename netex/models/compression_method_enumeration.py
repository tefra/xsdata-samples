from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CompressionMethodEnumeration(StrEnum):
    GZIP = "gzip"
    NONE = "none"
    OTHER = "other"
