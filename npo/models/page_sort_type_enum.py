from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:api:2013"


class PageSortTypeEnum(Enum):
    SORT_DATE = "sortDate"
    LAST_MODIFIED = "lastModified"
    LAST_PUBLISHED = "lastPublished"
    CREATION_DATE = "creationDate"
