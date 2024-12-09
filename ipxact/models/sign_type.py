from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class SignType(Enum):
    """
    This is an indication of the signedness of the value.
    """

    SIGNED = "signed"
    UNSIGNED = "unsigned"
