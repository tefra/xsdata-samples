from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class BswEntryRelationshipEnumSimple(Enum):
    """
    :cvar DERIVED_FROM: Describes that the BswModuleEntry referenced as
        "to" needs to have the same signature as the "abstract"
        BswModuleEntry referenced as "from".
    """
    DERIVED_FROM = "DERIVED-FROM"
