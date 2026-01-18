from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoftwareClusterDiagnosticAddressSemanticsEnumSimple(Enum):
    """
    :cvar FUNCTIONAL_ADDRESS: This address represents a functional
        address.
    :cvar PHYSICAL_ADDRESS: This address represents a physical address.
    """

    FUNCTIONAL_ADDRESS = "FUNCTIONAL-ADDRESS"
    PHYSICAL_ADDRESS = "PHYSICAL-ADDRESS"
