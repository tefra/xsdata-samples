from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class NilReasonEnumerationValue(StrEnum):
    INAPPLICABLE = "inapplicable"
    MISSING = "missing"
    TEMPLATE = "template"
    UNKNOWN = "unknown"
    WITHHELD = "withheld"
