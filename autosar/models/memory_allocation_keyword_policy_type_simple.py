from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class MemoryAllocationKeywordPolicyTypeSimple(Enum):
    """
    :cvar ADDR_METHOD_SHORT_NAME: The MemorySection shortNames of
        referring MemorySections and therefore the belonging Memory
        Allocation Keywords in the code are build with the shortName of
        the SwAddrMethod. This is the default value if the attribute
        does not exist.
    :cvar ADDR_METHOD_SHORT_NAME_AND_ALIGNMENT: The MemorySection
        shortNames of referring MemorySections and therefore the
        belonging Memory Allocation Keywords in the code are build with
        the shortName of the SwAddrMethod and a variable alignment
        postfix. Thereby the alignment postfix needs to be consistent
        with the alignment attribute of the related MemorySection.
    """

    ADDR_METHOD_SHORT_NAME = "ADDR-METHOD-SHORT-NAME"
    ADDR_METHOD_SHORT_NAME_AND_ALIGNMENT = (
        "ADDR-METHOD-SHORT-NAME-AND-ALIGNMENT"
    )
