from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RamBlockStatusControlEnumSimple(Enum):
    """
    :cvar API: The ramBlock status is controlled via service interface
        by usage of the SetRamBlockStatus operation.
    :cvar NV_RAM_MANAGER: The ramBlock status is controlled exclusively
        by the Nv Ram Manager.
    """
    API = "API"
    NV_RAM_MANAGER = "NV-RAM-MANAGER"
