from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AutoCollectEnumSimple(Enum):
    """
    :cvar REF_ALL: All objects being referenced (recursively) from the
        objects mentioned directly in the collection are also considered
        as part of the collection.
    :cvar REF_NON_STANDARD: This indicates that non standard objects
        ([TPS_GST_00088]) referenced (recursively) by the objects
        mentioned directly in the collection are also considered to be
        part of the collection.
    :cvar REF_NONE: This indicates that only those objects mentioned
        directly in the collection are part of the collection. No other
        objects are considered further.
    """

    REF_ALL = "REF-ALL"
    REF_NON_STANDARD = "REF-NON-STANDARD"
    REF_NONE = "REF-NONE"
