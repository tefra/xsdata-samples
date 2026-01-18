from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class BswInterruptCategorySimple(Enum):
    """
    :cvar CAT_1: Cat1 interrupt routines are not controlled by the OS
        and are only allowed to make a very limited selection of OS
        calls to enable and disable all interrupts. The
        BswInterruptEntity  is implemented by the interrupt service
        routine, which is directly called from the interrupt vector (not
        via the OS).
    :cvar CAT_2: Cat2 interrupt routines are controlled by the OS and
        they are allowed to make OS calls. The BswInterruptEntity  is
        implemented by the interrupt handler, which is called from the
        OS.
    """

    CAT_1 = "CAT-1"
    CAT_2 = "CAT-2"
