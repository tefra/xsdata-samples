from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_implementation_data_type_subtypes_enum import (
    AbstractImplementationDataTypeSubtypesEnum,
)
from .mode_declaration_group_subtypes_enum import (
    ModeDeclarationGroupSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeRequestTypeMap:
    """
    Specifies a mapping between a ModeDeclarationGroup and an
    ImplementationDataType.

    This ImplementationDataType shall be used to implement the
    ModeDeclarationGroup.

    :ivar implementation_data_type_ref: This is the corresponding
        AbstractImplementationDataType. It shall be modeled along the
        idea of an "unsigned integer-like" data type.
    :ivar mode_group_ref: This is the corresponding
        ModeDeclarationGroup.
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
        name = "MODE-REQUEST-TYPE-MAP"

    implementation_data_type_ref: (
        ModeRequestTypeMap.ImplementationDataTypeRef | None
    ) = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-DATA-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_group_ref: ModeRequestTypeMap.ModeGroupRef | None = field(
        default=None,
        metadata={
            "name": "MODE-GROUP-REF",
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
    class ImplementationDataTypeRef(Ref):
        dest: AbstractImplementationDataTypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ModeGroupRef(Ref):
        dest: ModeDeclarationGroupSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
