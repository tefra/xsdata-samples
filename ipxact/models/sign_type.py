from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class SignType(StrEnum):
    """
    This is an indication of the signedness of the value.
    """

    SIGNED = "signed"
    UNSIGNED = "unsigned"
