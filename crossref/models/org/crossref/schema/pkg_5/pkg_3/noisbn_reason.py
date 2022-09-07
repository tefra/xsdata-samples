from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class NoisbnReason(Enum):
    ARCHIVE_VOLUME = "archive_volume"
    MONOGRAPH = "monograph"
    SIMPLE_SERIES = "simple_series"
