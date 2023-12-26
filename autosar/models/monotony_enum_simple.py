from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class MonotonyEnumSimple(Enum):
    """
    :cvar DECREASING: This indicates that the related curve needs to be
        monotony decreasing.
    :cvar INCREASING: This indicates that the related curve needs to be
        monotony increasing.
    :cvar MONOTONOUS: This indicates that the values shall be
        monotonously decreasing or increasing, depending on the trend
        set by the first values of the series.
    :cvar NO_MONOTONY: This indicates that the related curve needs not
        to be monotony.
    :cvar STRICT_MONOTONOUS: This indicates that the values shall be
        strict monotonously decreasing or increasing, depending on the
        trend set by the first values of the series.
    :cvar STRICTLY_DECREASING: This indicates that the related curve
        needs to be strictly monotony decreasing.
    :cvar STRICTLY_INCREASING: This indicates that the related curve
        needs to be strictly monotony increasing.
    """

    DECREASING = "DECREASING"
    INCREASING = "INCREASING"
    MONOTONOUS = "MONOTONOUS"
    NO_MONOTONY = "NO-MONOTONY"
    STRICT_MONOTONOUS = "STRICT-MONOTONOUS"
    STRICTLY_DECREASING = "STRICTLY-DECREASING"
    STRICTLY_INCREASING = "STRICTLY-INCREASING"
