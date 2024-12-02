from dataclasses import dataclass, field
from typing import Optional

from .identifier import Identifier
from .mode_declaration_group_subtypes_enum import (
    ModeDeclarationGroupSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IncludedModeDeclarationGroupSet:
    """
    An IncludedModeDeclarationGroupSet declares that a set of ModeDeclarationGroups
    used by the software component for its implementation and consequently these
    ModeDeclarationGroups become part of the contract.

    :ivar mode_declaration_group_refs: This represents the referenced
        ModeDeclarationGroup.
    :ivar prefix: The prefix shall be used by the RTE generator as a
        prefix for the creation of symbols related to the referenced
        ModeDeclarationGroups, e.g
        RTE_TRANSITION_&lt;ModeDeclarationGroup&gt;.
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
        name = "INCLUDED-MODE-DECLARATION-GROUP-SET"

    mode_declaration_group_refs: Optional[
        "IncludedModeDeclarationGroupSet.ModeDeclarationGroupRefs"
    ] = field(
        default=None,
        metadata={
            "name": "MODE-DECLARATION-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    prefix: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "PREFIX",
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
    class ModeDeclarationGroupRefs:
        mode_declaration_group_ref: list[
            "IncludedModeDeclarationGroupSet.ModeDeclarationGroupRefs.ModeDeclarationGroupRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DECLARATION-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ModeDeclarationGroupRef(Ref):
            dest: Optional[ModeDeclarationGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
