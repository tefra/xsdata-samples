from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EventGroupControlTypeEnumSimple(Enum):
    """
    :cvar ACTIVATION_AND_TRIGGER_UNICAST: Activate the data path for
        unicast events and triggered unicast events that are sent out
        after a client got subscribed.
    :cvar ACTIVATION_MULTICAST: Activate the data path for multicast
        events of an EventGroup.
    :cvar ACTIVATION_UNICAST: Activate the data path for unicast events
        of an EventGroup.
    :cvar TRIGGER_UNICAST: Activate the data path for triggered unicast
        events that are sent out after a client got subscribed.
    """

    ACTIVATION_AND_TRIGGER_UNICAST = "ACTIVATION-AND-TRIGGER-UNICAST"
    ACTIVATION_MULTICAST = "ACTIVATION-MULTICAST"
    ACTIVATION_UNICAST = "ACTIVATION-UNICAST"
    TRIGGER_UNICAST = "TRIGGER-UNICAST"
