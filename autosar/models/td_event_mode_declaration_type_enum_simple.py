from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventModeDeclarationTypeEnumSimple(Enum):
    """
    :cvar MODE_DECLARATION_SWITCH_COMPLETED: A point in time where the
        switch to the associated ModeDeclarationGroupPrototype has been
        completed.
    :cvar MODE_DECLARATION_SWITCH_INITIATED: A point in time where the
        switch to the associated ModeDeclarationGroupPrototype has been
        initiated.
    """
    MODE_DECLARATION_SWITCH_COMPLETED = "MODE-DECLARATION-SWITCH-COMPLETED"
    MODE_DECLARATION_SWITCH_INITIATED = "MODE-DECLARATION-SWITCH-INITIATED"
