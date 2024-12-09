from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class BankAlignmentType(Enum):
    """
    'serial' or 'parallel' bank alignment.
    """

    SERIAL = "serial"
    PARALLEL = "parallel"
