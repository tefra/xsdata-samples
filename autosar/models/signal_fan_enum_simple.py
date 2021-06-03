from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SignalFanEnumSimple(Enum):
    """
    :cvar NFOLD: The connections internally in the
        CompositionSwComponentType via DelegationSwConnectors and
        AssemblySwConnectors are defined in a way that at least one data
        element present in the S/R interface or one
        ClientServerOperation in the C/S interface of the outer
        PortPrototype is involved in a 1:n or n:1 communication pattern.
    :cvar SINGLE: The connections internally in the
        CompositionSwComponentType via DelegationSwConnectors and
        AssemblySwConnectors are defined in a way that each
        VariableDataPrototype  present in the S/R interface or
        ClientServerOperation in the C/S interface of the outer
        PortPrototype is involved in a 1:1 communication pattern only.
    """
    NFOLD = "NFOLD"
    SINGLE = "SINGLE"
