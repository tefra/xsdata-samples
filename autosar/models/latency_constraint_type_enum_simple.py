from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class LatencyConstraintTypeEnumSimple(Enum):
    """
    :cvar AGE: In this case, the latency constraint is seen from the
        perspective of the response event of the associated event chain.
        Given a certain response event, the age interval of the latest
        stimulus is constrained.
    :cvar REACTION: In this case, the latency constraint is seen from
        the perspective of the stimulus event of the associated event
        chain. Given a certain stimulus event, the reaction interval of
        the first response is constrained.
    """

    AGE = "AGE"
    REACTION = "REACTION"
