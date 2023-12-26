from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class StorageConditionStatusEnumSimple(Enum):
    """
    :cvar EVENT_STORAGE_DISABLED: Storage of a diagnostic event is
        disabled.
    :cvar EVENT_STORAGE_ENABLED: Storage of a diagnostic event is
        enabled.
    """

    EVENT_STORAGE_DISABLED = "EVENT-STORAGE-DISABLED"
    EVENT_STORAGE_ENABLED = "EVENT-STORAGE-ENABLED"
