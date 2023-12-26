from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EthernetCouplingPortSchedulerEnumSimple(Enum):
    """
    :cvar DEFICIT_ROUND_ROBIN: Schedule algorithm "deficit round robin"
    :cvar STRICT_PRIORITY: Schedule algorithm "strict priority"
    :cvar WEIGHTED_ROUND_ROBIN: Schedule algorithm "weighted round
        robin"
    """

    DEFICIT_ROUND_ROBIN = "DEFICIT-ROUND-ROBIN"
    STRICT_PRIORITY = "STRICT-PRIORITY"
    WEIGHTED_ROUND_ROBIN = "WEIGHTED-ROUND-ROBIN"
