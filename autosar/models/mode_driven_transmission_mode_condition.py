from dataclasses import dataclass, field
from typing import List, Optional

from .mode_declaration_subtypes_enum import ModeDeclarationSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeDrivenTransmissionModeCondition:
    """The condition defined by this class evaluates to true if one of the
    referenced modeDeclarations (OR associated) is active.

    All referenced modeDeclarations shall be from the same
    ModeDeclarationGroup. The condition is used to define which
    TransmissionMode shall be activated using Com_SwitchIpduTxMode.

    :ivar mode_declaration_refs: Reference to one modeDeclaration which
        is OR associated in the context of the
        ModeDrivenTransmissionModeCondition.
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
        name = "MODE-DRIVEN-TRANSMISSION-MODE-CONDITION"

    mode_declaration_refs: Optional[
        "ModeDrivenTransmissionModeCondition.ModeDeclarationRefs"
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
        mode_declaration_ref: List[
            "ModeDrivenTransmissionModeCondition.ModeDeclarationRefs.ModeDeclarationRef"
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
