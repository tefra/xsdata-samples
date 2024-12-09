from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class TestableTestConstraint(Enum):
    UNCONSTRAINED = "unconstrained"
    RESTORE = "restore"
    WRITE_AS_READ = "writeAsRead"
    READ_ONLY = "readOnly"
