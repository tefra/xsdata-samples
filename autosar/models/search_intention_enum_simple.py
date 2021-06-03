from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SearchIntentionEnumSimple(Enum):
    """
    :cvar SEARCH_FOR_ALL: This value represents the intention to search
        for all instances of the given service
    :cvar SEARCH_FOR_ID: This value represents the intention to search
        for a dedicated instance of the given service.
    """
    SEARCH_FOR_ALL = "SEARCH-FOR-ALL"
    SEARCH_FOR_ID = "SEARCH-FOR-ID"
