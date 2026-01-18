from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .cpp_implementation_data_type_subtypes_enum import (
    CppImplementationDataTypeSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CppImplementationDataTypeElementQualifier:
    """
    This element qualifies the typeReference of the
    CppImplementationDataTypeElement to the CppImplementationDataType.

    :ivar inplace: This attribute defines whether the member type of the
        CppImplementationDataTypeElement in C++ is an embedded type
        element inside of the enclosing struct (true) or whether the
        type declaration is defined outside of the struct.
    :ivar type_reference_ref: This reference defines a type reference.
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
        name = "CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT-QUALIFIER"

    inplace: Boolean | None = field(
        default=None,
        metadata={
            "name": "INPLACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    type_reference_ref: (
        CppImplementationDataTypeElementQualifier.TypeReferenceRef | None
    ) = field(
        default=None,
        metadata={
            "name": "TYPE-REFERENCE-REF",
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
    class TypeReferenceRef(Ref):
        dest: CppImplementationDataTypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
