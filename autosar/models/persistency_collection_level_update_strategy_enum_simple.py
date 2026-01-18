from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PersistencyCollectionLevelUpdateStrategyEnumSimple(Enum):
    """
    :cvar DELETE: The update strategy is to delete all values on the
        level of the respective collection.
    :cvar KEEP_EXISTING: The update strategy is to keep the existing
        values on the level of the respective collection.
    """

    DELETE = "DELETE"
    KEEP_EXISTING = "KEEP-EXISTING"
