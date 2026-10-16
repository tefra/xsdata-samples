from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class CollectionProperty(StrEnum):
    LIST_BASED = "list-based"
    COUNTRY_BASED = "country-based"
    CRAWLER_BASED = "crawler-based"
    TEXT_MINING = "text-mining"
    UNSPECIFIED = "unspecified"
    SYNDICATION = "syndication"
    LINK_HEADER = "link-header"
