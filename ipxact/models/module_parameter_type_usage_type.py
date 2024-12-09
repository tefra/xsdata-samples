from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class ModuleParameterTypeUsageType(Enum):
    NONTYPED = "nontyped"
    TYPED = "typed"
    RUNTIME = "runtime"
