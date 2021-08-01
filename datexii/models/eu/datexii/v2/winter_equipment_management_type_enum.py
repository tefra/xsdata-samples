from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class WinterEquipmentManagementTypeEnum(Enum):
    """
    Instructions relating to the use of winter equipment.

    :cvar DO_NO_USE_STUD_TYRES: Do not use stud tyres.
    :cvar USE_SNOW_CHAINS: Use snow chains.
    :cvar USE_SNOW_CHAINS_OR_TYRES: Use snow chains or snow tyres.
    :cvar USE_SNOW_TYRES: Use snow tyres.
    :cvar WINTER_EQUIPMENT_ON_BOARD_REQUIRED: The carrying of winter
        equipment (snow chains and/or snow tyres) is required.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    DO_NO_USE_STUD_TYRES = "doNoUseStudTyres"
    USE_SNOW_CHAINS = "useSnowChains"
    USE_SNOW_CHAINS_OR_TYRES = "useSnowChainsOrTyres"
    USE_SNOW_TYRES = "useSnowTyres"
    WINTER_EQUIPMENT_ON_BOARD_REQUIRED = "winterEquipmentOnBoardRequired"
    OTHER = "other"
