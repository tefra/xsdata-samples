from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class ItemCrawler(Enum):
    GOOGLE = "google"
    MSN = "msn"
    SCIRUS = "scirus"
    YAHOO = "yahoo"
    I_PARADIGMS = "iParadigms"
