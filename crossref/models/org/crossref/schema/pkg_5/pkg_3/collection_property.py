from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class CollectionProperty(Enum):
    LIST_BASED = "list-based"
    COUNTRY_BASED = "country-based"
    CRAWLER_BASED = "crawler-based"
    TEXT_MINING = "text-mining"
    UNSPECIFIED = "unspecified"
    SYNDICATION = "syndication"
    LINK_HEADER = "link-header"
