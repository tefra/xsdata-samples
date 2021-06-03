from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TransferPropertyEnumSimple(Enum):
    """
    :cvar PENDING: If the signal has the TransferProperty pending, then
        the function Com_SendSignal shall not perform a transmission of
        the IPdu associated with the signal.
    :cvar TRIGGERED: The signal in the assigned IPdu is updated and a
        request for the IPdu's transmission is made.
    :cvar TRIGGERED_ON_CHANGE: The signal in the assigned IPdu is
        updated and a request for the IPdus transmission is made only if
        the signal value is different from the already stored signal
        value.
    :cvar TRIGGERED_ON_CHANGE_WITHOUT_REPETITION: The signal in the
        assigned IPdu is updated and a request for the IPdus
        transmission is made only if the signal value is different from
        the already stored signal value.  In the DIRECT/N-TIMES or MIXED
        transmission mode (EventControlledTiming) the IPdu will be
        transmitted just once without a repetition, independent of the
        defined NumberOfRepeats.
    :cvar TRIGGERED_WITHOUT_REPETITION: The signal in the assigned IPdu
        is updated and a request for the IPdu's transmission is made. In
        the DIRECT/N-TIMES or MIXED transmission mode
        (EventControlledTiming) the IPdu will be transmitted just once
        without a repetition, independent of the defined
        NumberOfRepeats.
    """
    PENDING = "PENDING"
    TRIGGERED = "TRIGGERED"
    TRIGGERED_ON_CHANGE = "TRIGGERED-ON-CHANGE"
    TRIGGERED_ON_CHANGE_WITHOUT_REPETITION = "TRIGGERED-ON-CHANGE-WITHOUT-REPETITION"
    TRIGGERED_WITHOUT_REPETITION = "TRIGGERED-WITHOUT-REPETITION"
