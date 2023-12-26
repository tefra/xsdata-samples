from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VehicleEquipmentEnum(Enum):
    """
    Types of vehicle equipment in use or on board.

    :cvar NOT_USING_SNOW_CHAINS: Vehicle not using snow chains.
    :cvar NOT_USING_SNOW_CHAINS_OR_TYRES: Vehicle not using either snow
        tyres or snow chains.
    :cvar SNOW_CHAINS_IN_USE: Vehicle using snow chains.
    :cvar SNOW_TYRES_IN_USE: Vehicle using snow tyres.
    :cvar SNOW_CHAINS_OR_TYRES_IN_USE: Vehicle using snow tyres or snow
        chains.
    :cvar WITHOUT_SNOW_TYRES_OR_CHAINS_ON_BOARD: Vehicle which is not
        carrying on board snow tyres or chains.
    """

    NOT_USING_SNOW_CHAINS = "notUsingSnowChains"
    NOT_USING_SNOW_CHAINS_OR_TYRES = "notUsingSnowChainsOrTyres"
    SNOW_CHAINS_IN_USE = "snowChainsInUse"
    SNOW_TYRES_IN_USE = "snowTyresInUse"
    SNOW_CHAINS_OR_TYRES_IN_USE = "snowChainsOrTyresInUse"
    WITHOUT_SNOW_TYRES_OR_CHAINS_ON_BOARD = "withoutSnowTyresOrChainsOnBoard"
