from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ReentrancyLevelEnumSimple(Enum):
    """
    :cvar MULTICORE_REENTRANT: Unlimited concurrent execution of this
        entity is possible, including preemption and parallel execution
        on multi core systems.
    :cvar NON_REENTRANT: Concurrent execution of this entity is not
        possible.
    :cvar SINGLE_CORE_REENTRANT: Pseudo-concurrent execution (i.e.
        preemption) of this entity is possible on single core systems.
    """
    MULTICORE_REENTRANT = "MULTICORE-REENTRANT"
    NON_REENTRANT = "NON-REENTRANT"
    SINGLE_CORE_REENTRANT = "SINGLE-CORE-REENTRANT"
