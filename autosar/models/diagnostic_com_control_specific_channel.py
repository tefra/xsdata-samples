from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .communication_cluster_subtypes_enum import (
    CommunicationClusterSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticComControlSpecificChannel:
    """
    This represents the ability to add further attributes to the definition
    of a specific channel that is subject to the diagnostic service
    "communication control".

    :ivar specific_channel_ref: This represents the affected
        CommunicationClusters in the role specificChannel
    :ivar subnet_number: This represents the applicable subnet number
        (which is an arbitrary number ranging from 1..14)
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL"

    specific_channel_ref: DiagnosticComControlSpecificChannel.SpecificChannelRef | None = field(
        default=None,
        metadata={
            "name": "SPECIFIC-CHANNEL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    subnet_number: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SUBNET-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class SpecificChannelRef(Ref):
        dest: CommunicationClusterSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
