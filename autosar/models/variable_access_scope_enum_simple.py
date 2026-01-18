from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class VariableAccessScopeEnumSimple(Enum):
    """
    :cvar COMMUNICATION_INTER_ECU: This case is foreseen to express that
        the corresponding communication shall be considered inter-ECU,
        i.e. it will cross the ECU boundary. This is considered the
        default case.
    :cvar COMMUNICATION_INTRA_PARTITION: This case is foreseen to
        express that the corresponding communication shall '''not'''
        cross the boundary of a partition.
    :cvar INTER_PARTITION_INTRA_ECU: In this case the communication
        shall cross the boundaries of partitions within one ECU but it
        shall not cross the boundaries of the ECU itself.
    """

    COMMUNICATION_INTER_ECU = "COMMUNICATION-INTER-ECU"
    COMMUNICATION_INTRA_PARTITION = "COMMUNICATION-INTRA-PARTITION"
    INTER_PARTITION_INTRA_ECU = "INTER-PARTITION-INTRA-ECU"
