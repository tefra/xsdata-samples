from dataclasses import dataclass, field
from typing import Optional

from .mode_declaration_subtypes_enum import ModeDeclarationSubtypesEnum
from .mode_error_reaction_policy_enum import ModeErrorReactionPolicyEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeErrorBehavior:
    """
    This represents the ability to define the error behavior in the context
    of mode handling.

    :ivar default_mode_ref: This represents the ModeDeclaration that is
        considered the error mode in the context of the enclosing
        ModeDeclarationGroup.
    :ivar error_reaction_policy: This represents the ability to define
        the policy in terms of which default model shall apply in case
        an error occurs.
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
        name = "MODE-ERROR-BEHAVIOR"

    default_mode_ref: Optional["ModeErrorBehavior.DefaultModeRef"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-MODE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    error_reaction_policy: Optional[ModeErrorReactionPolicyEnum] = field(
        default=None,
        metadata={
            "name": "ERROR-REACTION-POLICY",
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
    class DefaultModeRef(Ref):
        dest: Optional[ModeDeclarationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
