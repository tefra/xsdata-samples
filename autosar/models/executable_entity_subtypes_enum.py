from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ExecutableEntitySubtypesEnum(Enum):
    BSW_CALLED_ENTITY = "BSW-CALLED-ENTITY"
    BSW_INTERRUPT_ENTITY = "BSW-INTERRUPT-ENTITY"
    BSW_MODULE_ENTITY = "BSW-MODULE-ENTITY"
    BSW_SCHEDULABLE_ENTITY = "BSW-SCHEDULABLE-ENTITY"
    EXECUTABLE_ENTITY = "EXECUTABLE-ENTITY"
    RUNNABLE_ENTITY = "RUNNABLE-ENTITY"
