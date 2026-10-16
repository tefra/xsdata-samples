from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/fundref.xsd"


class AssertionProvider(StrEnum):
    PUBLISHER = "publisher"
    CROSSREF = "crossref"
