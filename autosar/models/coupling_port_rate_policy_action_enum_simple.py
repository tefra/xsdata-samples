from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CouplingPortRatePolicyActionEnumSimple(Enum):
    """
    :cvar BLOCK_SOURCE: If the rate policy is violated the CouplingPort
        this CouplingPortRatePolicy is defined on shall block all frames
        from the MAC-Address the violation was caused by.
    :cvar DROP_FRAME: If the rate policy is violated the frame shall be
        dropped.
    """

    BLOCK_SOURCE = "BLOCK-SOURCE"
    DROP_FRAME = "DROP-FRAME"
