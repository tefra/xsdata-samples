from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PersistencyRedundancyHandlingScopeEnumSimple(Enum):
    """
    :cvar PERSISTENCY_REDUNDANCY_HANDLING_SCOPE_ELEMENT: The redundancy
        handling shall be applied on element level (key-value pair and
        file).
    :cvar PERSISTENCY_REDUNDANCY_HANDLING_SCOPE_STORAGE: The redundancy
        handling shall be applied on storage (key-value storage and file
        storage) level.
    """

    PERSISTENCY_REDUNDANCY_HANDLING_SCOPE_ELEMENT = (
        "PERSISTENCY-REDUNDANCY-HANDLING-SCOPE-ELEMENT"
    )
    PERSISTENCY_REDUNDANCY_HANDLING_SCOPE_STORAGE = (
        "PERSISTENCY-REDUNDANCY-HANDLING-SCOPE-STORAGE"
    )
