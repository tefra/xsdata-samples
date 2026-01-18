from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowResourceAliasNameEnumSimple(Enum):
    """
    :cvar NO_SHOW_ALIAS_NAME: This indicates that alias names of the
        referenced object shall '''not''' be rendered at the place of
        the reference.
    :cvar SHOW_ALIAS_NAME: This indicates that the alias names of the
        referenced object shall be rendered at the place of the
        reference.
    """

    NO_SHOW_ALIAS_NAME = "NO-SHOW-ALIAS-NAME"
    SHOW_ALIAS_NAME = "SHOW-ALIAS-NAME"
