from dataclasses import dataclass, field
from typing import Optional

from .application_array_element_subtypes_enum import (
    ApplicationArrayElementSubtypesEnum,
)
from .implementation_data_type_element_subtypes_enum import (
    ImplementationDataTypeElementSubtypesEnum,
)
from .integer import Integer
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IndexedArrayElement:
    """This element represents exactly one indexed element in the array.

    Either the applicationArrayElement or implementationArrayElement
    reference shall be used.

    :ivar application_array_element_ref: Reference to an
        ApplicationArrayElement in an array.
    :ivar implementation_array_element_ref: Reference to an
        ImplementationDataTypeElement in an array.
    :ivar index: Position of an element in an array. Starting position
        is 0.
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
        name = "INDEXED-ARRAY-ELEMENT"

    application_array_element_ref: Optional[
        "IndexedArrayElement.ApplicationArrayElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "APPLICATION-ARRAY-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implementation_array_element_ref: Optional[
        "IndexedArrayElement.ImplementationArrayElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-ARRAY-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    index: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "INDEX",
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
    class ApplicationArrayElementRef(Ref):
        dest: Optional[ApplicationArrayElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ImplementationArrayElementRef(Ref):
        dest: Optional[ImplementationDataTypeElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
