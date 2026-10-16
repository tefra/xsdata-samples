from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class NameNameStyle(StrEnum):
    EASTERN = "eastern"
    GIVEN_ONLY = "given-only"
    ISLENSK = "islensk"
    WESTERN = "western"
