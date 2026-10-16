from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class AggregationType(StrEnum):
    SET = "set"
    BAG = "bag"
    SEQUENCE = "sequence"
    ARRAY = "array"
    RECORD = "record"
    TABLE = "table"
