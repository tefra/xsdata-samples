from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class MappingScopeEnumSimple(Enum):
    """
    :cvar MAPPING_SCOPE_CORE: The mapping constraint applies to
        different Cores.
    :cvar MAPPING_SCOPE_ECU: The mapping constraint applies to different
        Ecus.
    :cvar MAPPING_SCOPE_PARTITION: The mapping constraint applies to
        different Partitions.
    """
    MAPPING_SCOPE_CORE = "MAPPING-SCOPE-CORE"
    MAPPING_SCOPE_ECU = "MAPPING-SCOPE-ECU"
    MAPPING_SCOPE_PARTITION = "MAPPING-SCOPE-PARTITION"
