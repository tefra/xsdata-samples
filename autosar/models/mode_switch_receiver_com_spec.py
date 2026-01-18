from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeSwitchReceiverComSpec:
    """
    Communication attributes of RPortPrototypes with respect to mode
    communication.

    :ivar enhanced_mode_api: This controls the creation of the enhanced
        mode API that returns information about the previous mode and
        the next mode. If set to "true" the enhanced mode API is
        supposed to be generated. For more details please refer to the
        SWS_RTE.
    :ivar mode_group_ref: ModeDeclarationGroupPrototype (of the same
        PortInterface) to which these communication attributes apply.
    :ivar supports_asynchronous_mode_switch: This attribute controls the
        behavior of the corresponding RPortPrototype with respect to the
        question whether it can deal with asynchronous mode switch
        requests, i.e. if set to true, the RPortPrototype is able to
        deal with an asynchronous mode switch request.
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
        name = "MODE-SWITCH-RECEIVER-COM-SPEC"

    enhanced_mode_api: Boolean | None = field(
        default=None,
        metadata={
            "name": "ENHANCED-MODE-API",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_group_ref: ModeSwitchReceiverComSpec.ModeGroupRef | None = field(
        default=None,
        metadata={
            "name": "MODE-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    supports_asynchronous_mode_switch: Boolean | None = field(
        default=None,
        metadata={
            "name": "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH",
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
    class ModeGroupRef(Ref):
        dest: ModeDeclarationGroupPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
