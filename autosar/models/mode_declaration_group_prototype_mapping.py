from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .mode_declaration_mapping_set_subtypes_enum import (
    ModeDeclarationMappingSetSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeDeclarationGroupPrototypeMapping:
    """
    Defines the mapping of two particular ModeDeclarationGroupPrototypes
    (in the given context) that are unequally named and/or require a
    reference to a ModeDeclarationMappingSet in order to become compatible
    by definition of ModeDeclarationMappings.

    :ivar first_mode_group_ref: ModeDeclarationGroupPrototype to be
        mapped.
    :ivar mode_declaration_mapping_set_ref: This represents the
        available mappings of ModeDeclarations in the context ot this
        ModeDeclarationGroupPrototype.
    :ivar second_mode_group_ref: ModeDeclarationGroupPrototype to be
        mapped.
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
        name = "MODE-DECLARATION-GROUP-PROTOTYPE-MAPPING"

    first_mode_group_ref: ModeDeclarationGroupPrototypeMapping.FirstModeGroupRef | None = field(
        default=None,
        metadata={
            "name": "FIRST-MODE-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_declaration_mapping_set_ref: ModeDeclarationGroupPrototypeMapping.ModeDeclarationMappingSetRef | None = field(
        default=None,
        metadata={
            "name": "MODE-DECLARATION-MAPPING-SET-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_mode_group_ref: ModeDeclarationGroupPrototypeMapping.SecondModeGroupRef | None = field(
        default=None,
        metadata={
            "name": "SECOND-MODE-GROUP-REF",
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
    class FirstModeGroupRef(Ref):
        dest: ModeDeclarationGroupPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ModeDeclarationMappingSetRef(Ref):
        dest: ModeDeclarationMappingSetSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SecondModeGroupRef(Ref):
        dest: ModeDeclarationGroupPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
