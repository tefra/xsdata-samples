from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventSwcInternalBehaviorTypeEnumSimple(Enum):
    """
    :cvar RUNNABLE_ENTITY_ACTIVATED: A point in time where the
        associated RunnableEntity has been activated, which means that
        it has entered the state "to be started".
    :cvar RUNNABLE_ENTITY_STARTED: A point in time where the associated
        RunnableEntity has entered the state "started" after its
        activation.
    :cvar RUNNABLE_ENTITY_TERMINATED: A point in time where the
        associated RunnableEntity has terminated and entered the state
        "suspended".
    :cvar RUNNABLE_ENTITY_VARIABLE_ACCESS: A point in time where the
        associated variable is accessed.
    """

    RUNNABLE_ENTITY_ACTIVATED = "RUNNABLE-ENTITY-ACTIVATED"
    RUNNABLE_ENTITY_STARTED = "RUNNABLE-ENTITY-STARTED"
    RUNNABLE_ENTITY_TERMINATED = "RUNNABLE-ENTITY-TERMINATED"
    RUNNABLE_ENTITY_VARIABLE_ACCESS = "RUNNABLE-ENTITY-VARIABLE-ACCESS"
