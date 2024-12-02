from dataclasses import dataclass, field
from typing import Optional

from .mode_declaration_subtypes_enum import ModeDeclarationSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TriggerIPduSendCondition:
    """The condition defined by this class evaluates to true if one of the
    referenced modeDeclarations (OR associated) is active.

    The condition is used to define when the Pdu is triggered with the
    Com_TriggerIPDUSend API call.

    :ivar mode_declaration_refs: Reference to one modeDeclaration which
        is OR associated in the context of the TriggerIPduSendCondition.
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
        name = "TRIGGER-I-PDU-SEND-CONDITION"

    mode_declaration_refs: Optional[
        "TriggerIPduSendCondition.ModeDeclarationRefs"
    ] = field(
        default=None,
        metadata={
            "name": "MODE-DECLARATION-REFS",
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
    class ModeDeclarationRefs:
        mode_declaration_ref: list[
            "TriggerIPduSendCondition.ModeDeclarationRefs.ModeDeclarationRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DECLARATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ModeDeclarationRef(Ref):
            dest: Optional[ModeDeclarationSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
