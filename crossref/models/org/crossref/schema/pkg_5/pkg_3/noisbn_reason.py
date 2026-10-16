from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class NoisbnReason(StrEnum):
    ARCHIVE_VOLUME = "archive_volume"
    MONOGRAPH = "monograph"
    SIMPLE_SERIES = "simple_series"
