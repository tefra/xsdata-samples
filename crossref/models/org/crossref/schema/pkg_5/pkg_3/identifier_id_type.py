from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class IdentifierIdType(Enum):
    PII = "pii"
    SICI = "sici"
    DOI = "doi"
    DAI = "dai"
    Z39_23 = "Z39.23"
    ISO_STD_REF = "ISO-std-ref"
    STD_DESIGNATION = "std-designation"
    REPORT_NUMBER = "report-number"
    PMID = "pmid"
    OTHER = "other"
