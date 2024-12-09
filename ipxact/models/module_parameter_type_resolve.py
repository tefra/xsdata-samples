from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class ModuleParameterTypeResolve(Enum):
    """Determines how a parameter is resolved.

    User means the value must be obtained from the user. Generated means
    the value will be provided by a generator.

    :cvar IMMEDIATE: Property content cannot be modified through
        configuration.
    :cvar USER: Property content can be modified through configuration.
        Modifications will be saved with the design.
    :cvar GENERATED: Generators may modify this property. Modifications
        get saved with the design.
    """

    IMMEDIATE = "immediate"
    USER = "user"
    GENERATED = "generated"
