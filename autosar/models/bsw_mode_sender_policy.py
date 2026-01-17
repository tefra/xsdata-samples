from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .bsw_mode_switch_ack_request import BswModeSwitchAckRequest
from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswModeSenderPolicy:
    """
    Specifies the details for the sending of a mode switch for the referred
    mode group.

    :ivar ack_request: Request for acknowledgement
    :ivar enhanced_mode_api: This controls the creation of the enhanced
        mode API that returns information about the previous mode and
        the next mode. If set to TRUE the enhanced mode API is supposed
        to be generated. For more details please refer to the SWS_RTE.
    :ivar provided_mode_group_ref: The provided mode group for which the
        policy is specified.
    :ivar queue_length: Length of call queue on the sender side. The
        queue is implemented by the RTE resp.BswScheduler. The value
        shall be greater or equal to 0. Setting the value of queueLength
        to 0 implies non-queued communication.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "BSW-MODE-SENDER-POLICY"

    ack_request: Optional[BswModeSwitchAckRequest] = field(
        default=None,
        metadata={
            "name": "ACK-REQUEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    enhanced_mode_api: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ENHANCED-MODE-API",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    provided_mode_group_ref: Optional[
        "BswModeSenderPolicy.ProvidedModeGroupRef"
    ] = field(
        default=None,
        metadata={
            "name": "PROVIDED-MODE-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    queue_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "QUEUE-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class ProvidedModeGroupRef(Ref):
        dest: Optional[ModeDeclarationGroupPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
