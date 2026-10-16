from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class ArchiveName(StrEnum):
    CLOCKSS = "CLOCKSS"
    LOCKSS = "LOCKSS"
    PORTICO = "Portico"
    KB = "KB"
    INTERNET_ARCHIVE = "Internet Archive"
    DWT = "DWT"
