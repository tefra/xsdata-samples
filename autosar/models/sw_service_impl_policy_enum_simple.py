from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SwServiceImplPolicyEnumSimple(Enum):
    """
    :cvar INLINE: inline service definition.
    :cvar INLINE_CONDITIONAL: The service (in AUTOSAR: BswModuleEntry)
        is implemented in a way that it either resolves to an inline
        function or to a standard function depending on conditions set
        at a later point in time. This could be handled by using the
        AUTOSAR compiler abstraction macros (INLINE, LOCAL_INLINE)
        and/or by further compiler switches depending on ECU
        configuration values.
    :cvar MACRO: macro service definition.
    :cvar STANDARD: Standard service and default value, if nothing is
        defined.
    """

    INLINE = "INLINE"
    INLINE_CONDITIONAL = "INLINE-CONDITIONAL"
    MACRO = "MACRO"
    STANDARD = "STANDARD"
