from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TerminationBehaviorEnumSimple(Enum):
    """
    :cvar PROCESS_IS_NOT_SELF_TERMINATING: The Process terminates only
        on request from Execution Management.
    :cvar PROCESS_IS_SELF_TERMINATING: The Process is allowed to
        terminate without request from Execution Management.
    """
    PROCESS_IS_NOT_SELF_TERMINATING = "PROCESS-IS-NOT-SELF-TERMINATING"
    PROCESS_IS_SELF_TERMINATING = "PROCESS-IS-SELF-TERMINATING"
