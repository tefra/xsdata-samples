from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AclScopeEnumSimple(Enum):
    """
    :cvar DEPENDANT: This specifies that the AclPermission applies to
        dependant (in particular referenced) operations / objects as
        well. Note that this includes the descendant ones.
    :cvar DESCENDANT: This specifies that the AclPermission applies to
        descendant  operations / objects as well.
    :cvar EXPLICIT: This is indicates that the AclPermission applies to
        explicit objects / operations only.
    """

    DEPENDANT = "DEPENDANT"
    DESCENDANT = "DESCENDANT"
    EXPLICIT = "EXPLICIT"
