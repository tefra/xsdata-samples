from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class SupArrange(StrEnum):
    STACK = "stack"
    STAGGER = "stagger"
