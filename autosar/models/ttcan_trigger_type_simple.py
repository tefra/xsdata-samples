from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TtcanTriggerTypeSimple(Enum):
    """
    :cvar RX_TRIGGER: Check for message reception
    :cvar TX_REF_TRIGGER: Send reference message in periodic case
    :cvar TX_REF_TRIGGER_GAP: Send reference message in event-
        synchronised case
    :cvar TX_TRIGGER_MERGED: Send message in a merged arbitration window
    :cvar TX_TRIGGER_SINGLE: Send message in an exclusive time window
    :cvar WATCH_TRIGGER: Check for missing reference message in periodic
        case
    :cvar WATCH_TRIGGER_GAP: Check for missing reference message in
        event-synchronised case
    """

    RX_TRIGGER = "RX-TRIGGER"
    TX_REF_TRIGGER = "TX-REF-TRIGGER"
    TX_REF_TRIGGER_GAP = "TX-REF-TRIGGER-GAP"
    TX_TRIGGER_MERGED = "TX-TRIGGER-MERGED"
    TX_TRIGGER_SINGLE = "TX-TRIGGER-SINGLE"
    WATCH_TRIGGER = "WATCH-TRIGGER"
    WATCH_TRIGGER_GAP = "WATCH-TRIGGER-GAP"
