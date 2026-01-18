from __future__ import annotations

from dataclasses import dataclass, field

from .communication_cluster_subtypes_enum import (
    CommunicationClusterSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DiagnosticComControlSubNodeChannel:
    """
    This represents the ability to add further attributes to the definition
    of a specific sub-node channel that is subject to the diagnostic
    service "communication control".

    :ivar sub_node_channel_ref: This represents the affected
        CommunicationClusters in the role subNodeChannel
    :ivar sub_node_number: This represents the applicable subNode
        number. The value corresponds to the request message parameter
        nodeIdentificationNumber of diagnostic service
        CommunicationControl (0x28).
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
        name = "DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL"

    sub_node_channel_ref: (
        None | DiagnosticComControlSubNodeChannel.SubNodeChannelRef
    ) = field(
        default=None,
        metadata={
            "name": "SUB-NODE-CHANNEL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sub_node_number: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SUB-NODE-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass(kw_only=True)
    class SubNodeChannelRef(Ref):
        dest: CommunicationClusterSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
