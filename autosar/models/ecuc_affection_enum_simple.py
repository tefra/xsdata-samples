from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EcucAffectionEnumSimple(Enum):
    """
    :cvar LT_AFFECTS_PB: A link time parameter affecting one or several
        post-build time parameter(s).
    :cvar NO_AFFECT: no affect on any other parameter.
    :cvar PC_AFFECTS_LT: A pre-compile time parameter affecting one or
        several link time parameter(s).
    :cvar PC_AFFECTS_LT_AND_PB: A pre-compile time parameter affecting
        one or several link time and post-build time parameter(s)).
    :cvar PC_AFFECTS_PB: A pre-compile time parameter affecting one or
        several post build time parameter(s).
    """
    LT_AFFECTS_PB = "LT-AFFECTS-PB"
    NO_AFFECT = "NO-AFFECT"
    PC_AFFECTS_LT = "PC-AFFECTS-LT"
    PC_AFFECTS_LT_AND_PB = "PC-AFFECTS-LT-AND-PB"
    PC_AFFECTS_PB = "PC-AFFECTS-PB"
