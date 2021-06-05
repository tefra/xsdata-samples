from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SynchronizationTypeEnumSimple(Enum):
    """
    :cvar RESPONSE_SYNCHRONIZATION: In case that the Synchronization
        Timing Constraint is specified for event chains, the response
        events of the associated event chains shall occur synchronously
        with respect to the specified tolerance. All associated event
        chains shall have the same stimulus event. In case that the
        Synchronization Timing Constraint is specified for events, the
        associated events shall occur synchronously with respect to the
        specified tolerance. All associated events represent the
        response events of a common stimulus event, even such a stimulus
        event is not known yet or not available in the scope of the
        model.
    :cvar STIMULUS_SYNCHRONIZATION: In case that the Synchronization
        Timing Constraint is specified for event chains, the stimulus
        events of the associated event chains shall occur synchronously
        with respect to the specified tolerance. All associated event
        chains shall have the same response event. In case that the
        Synchronization Timing Constraint is specified for events, the
        associated events shall occur synchronously with respect to the
        specified tolerance. All associated events represent the
        stimulus events of a common response event, even such a response
        event is not known yet or not available in the scope of the
        model.
    """
    RESPONSE_SYNCHRONIZATION = "RESPONSE-SYNCHRONIZATION"
    STIMULUS_SYNCHRONIZATION = "STIMULUS-SYNCHRONIZATION"
