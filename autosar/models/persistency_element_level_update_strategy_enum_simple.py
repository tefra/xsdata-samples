from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PersistencyElementLevelUpdateStrategyEnumSimple(Enum):
    """
    :cvar DELETE: The update strategy is to delete the value of the
        respective data item.
    :cvar KEEP_EXISTING: The update strategy is to keep the existing
        value of the respective data item.
    :cvar OVERWRITE: The update strategy is to overwrite the respective
        data item.
    """
    DELETE = "DELETE"
    KEEP_EXISTING = "KEEP-EXISTING"
    OVERWRITE = "OVERWRITE"
