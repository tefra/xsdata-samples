from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class DatasetDatasetType(Enum):
    RECORD = "record"
    COLLECTION = "collection"
    CROSSMARK_POLICY = "crossmark_policy"
    OTHER = "other"
