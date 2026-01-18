from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventBswInternalBehaviorTypeEnumSimple(Enum):
    """
    :cvar BSW_MODULE_ENTITY_ACTIVATED: A point in time where the
        associated BswModuleEntity has been activated, which means that
        it has entered the state "to be started".
    :cvar BSW_MODULE_ENTITY_STARTED: A point in time where the
        associated BswModuleEntity has entered the state "started" after
        its activation.
    :cvar BSW_MODULE_ENTITY_TERMINATED: A point in time where the
        associated BswModuleEntity has terminated and entered the state
        "suspended"
    """

    BSW_MODULE_ENTITY_ACTIVATED = "BSW-MODULE-ENTITY-ACTIVATED"
    BSW_MODULE_ENTITY_STARTED = "BSW-MODULE-ENTITY-STARTED"
    BSW_MODULE_ENTITY_TERMINATED = "BSW-MODULE-ENTITY-TERMINATED"
