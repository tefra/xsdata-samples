from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class ItemCrawler(StrEnum):
    GOOGLE = "google"
    MSN = "msn"
    SCIRUS = "scirus"
    YAHOO = "yahoo"
    I_PARADIGMS = "iParadigms"
