from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventBswModeDeclarationTypeEnumSimple(Enum):
    """
    :cvar MODE_DECLARATION_REQUESTED: A point in time where the
        associated ModeDeclarationGroupPrototype has been requested.
    :cvar MODE_DECLARATION_SWITCH_COMPLETED: A point in time where the
        switch to the associated ModeDeclarationGroupPrototype has been
        completed.
    :cvar MODE_DECLARATION_SWITCH_INITIATED: A point in time where the
        switch to the associated ModeDeclarationGroupPrototype has been
        initiated by the BswM.
    """

    MODE_DECLARATION_REQUESTED = "MODE-DECLARATION-REQUESTED"
    MODE_DECLARATION_SWITCH_COMPLETED = "MODE-DECLARATION-SWITCH-COMPLETED"
    MODE_DECLARATION_SWITCH_INITIATED = "MODE-DECLARATION-SWITCH-INITIATED"
