from dataclasses import dataclass, field
from typing import Optional
from .application_record_element_subtypes_enum import (
    ApplicationRecordElementSubtypesEnum,
)
from .argument_data_prototype_subtypes_enum import (
    ArgumentDataPrototypeSubtypesEnum,
)
from .cpp_implementation_data_type_element_subtypes_enum import (
    CppImplementationDataTypeElementSubtypesEnum,
)
from .implementation_data_type_element_subtypes_enum import (
    ImplementationDataTypeElementSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TlvDataIdDefinition:
    """
    This meta-class represents the ability to define the tlvDataId.

    :ivar id: This attribute represents the definition of the value of
        the TlvDataId
    :ivar tlv_argument_ref: This reference assigns a tlvDataId to a
        given argument of a ClientServerOperation.
    :ivar tlv_implementation_data_type_element_ref: This reference
        associates the definition of a TLV data id with a given
        ImplementationDataTypeElement.
    :ivar tlv_record_element_ref: This reference associates the
        definition of a TLV data id with a given
        ApplicationRecordElement.
    :ivar tlv_sub_element_ref: This reference associates the definition
        of a TLV data id with a given CppImplementationDataTypeElement.
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
        name = "TLV-DATA-ID-DEFINITION"

    id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tlv_argument_ref: Optional["TlvDataIdDefinition.TlvArgumentRef"] = field(
        default=None,
        metadata={
            "name": "TLV-ARGUMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tlv_implementation_data_type_element_ref: Optional[
        "TlvDataIdDefinition.TlvImplementationDataTypeElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "TLV-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tlv_record_element_ref: Optional[
        "TlvDataIdDefinition.TlvRecordElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "TLV-RECORD-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tlv_sub_element_ref: Optional[
        "TlvDataIdDefinition.TlvSubElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "TLV-SUB-ELEMENT-REF",
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
    class TlvArgumentRef(Ref):
        dest: Optional[ArgumentDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TlvImplementationDataTypeElementRef(Ref):
        dest: Optional[ImplementationDataTypeElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TlvRecordElementRef(Ref):
        dest: Optional[ApplicationRecordElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TlvSubElementRef(Ref):
        dest: Optional[CppImplementationDataTypeElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
