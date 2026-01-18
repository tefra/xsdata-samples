from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OperatorActionStatusEnum(Enum):
    """
    List of statuses associated with operator actions.

    :cvar REQUESTED: A request, either internal or external, has been
        received to implement an action. It has neither been approved
        nor has any activity yet been undertaken to implement the
        action.
    :cvar APPROVED: The action has been approved by the recipient of the
        request but activity to implement the action has not yet
        commenced.
    :cvar BEING_IMPLEMENTED: The action is in the process of being
        implemented.
    :cvar IMPLEMENTED: The action is fully implemented.
    :cvar REJECTED: The action has been rejected by the recipient of the
        request and hence is not implemented.
    :cvar TERMINATION_REQUESTED: A request, either internal or external,
        has been received to terminate the action, but activity to
        terminate the action has not yet commenced.
    :cvar BEING_TERMINATED: The action is in the process of being
        terminated either because the action has reached the end of its
        validity period or because new circumstances have arisen and its
        termination has been requested, e.g. because of a traffic jam on
        the alternative route.
    """

    REQUESTED = "requested"
    APPROVED = "approved"
    BEING_IMPLEMENTED = "beingImplemented"
    IMPLEMENTED = "implemented"
    REJECTED = "rejected"
    TERMINATION_REQUESTED = "terminationRequested"
    BEING_TERMINATED = "beingTerminated"
