from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class BswEntryKindEnumSimple(StrEnum):
    """
    :cvar ABSTRACT: This BswModuleEntry specifies an abstract signature
        of C-functions. The signature needs to be implemented by
        concrete BswModuleEntrys
    :cvar CONCRETE: This BswModuleEntry specifies a concrete C-function
        with its signature.
    """

    ABSTRACT = "ABSTRACT"
    CONCRETE = "CONCRETE"
