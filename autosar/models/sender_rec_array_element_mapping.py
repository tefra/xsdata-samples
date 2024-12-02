from dataclasses import dataclass, field
from typing import Optional

from .application_record_element_subtypes_enum import (
    ApplicationRecordElementSubtypesEnum,
)
from .implementation_data_type_element_subtypes_enum import (
    ImplementationDataTypeElementSubtypesEnum,
)
from .indexed_array_element import IndexedArrayElement
from .ref import Ref
from .system_signal_subtypes_enum import SystemSignalSubtypesEnum
from .text_table_mapping import TextTableMapping

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SenderRecArrayElementMapping:
    """The SenderRecArrayElement may be a primitive one or a composite one.

    If the element is primitive, it will be mapped to the SystemSignal
    (multiplicity 1). If the VariableDataPrototype that is referenced by
    SenderReceiverToSignalGroupMapping is typed by an
    ApplicationDataType the reference to the ApplicationArrayElement
    shall be used. If the VariableDataPrototype is typed by the
    ImplementationDataType the reference to the
    ImplementationArrayElement shall be used. If the element is
    composite, there will be no mapping to the SystemSignal
    (multiplicity 0). In this case the ArrayElementMapping element will
    aggregate the TypeMapping element. In that way also the composite
    datatypes can be mapped to SystemSignals. Regardless whether
    composite or primitive array element is mapped the indexed element
    always needs to be specified.

    :ivar complex_type_mapping: This aggregation will be used if the
        element is composite.
    :ivar indexed_array_element: Reference to an indexed array element
        in the context of the dataElement or in the context of a
        composite element.
    :ivar system_signal_ref: Reference to the system signal used to
        carry the primitive ApplicationArrayElement.
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
        name = "SENDER-REC-ARRAY-ELEMENT-MAPPING"

    complex_type_mapping: Optional[
        "SenderRecArrayElementMapping.ComplexTypeMapping"
    ] = field(
        default=None,
        metadata={
            "name": "COMPLEX-TYPE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    indexed_array_element: Optional[IndexedArrayElement] = field(
        default=None,
        metadata={
            "name": "INDEXED-ARRAY-ELEMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    system_signal_ref: Optional[
        "SenderRecArrayElementMapping.SystemSignalRef"
    ] = field(
        default=None,
        metadata={
            "name": "SYSTEM-SIGNAL-REF",
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
    class ComplexTypeMapping:
        sender_rec_array_type_mapping: Optional[
            "SenderRecArrayTypeMapping"
        ] = field(
            default=None,
            metadata={
                "name": "SENDER-REC-ARRAY-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sender_rec_record_type_mapping: Optional[
            "SenderRecRecordTypeMapping"
        ] = field(
            default=None,
            metadata={
                "name": "SENDER-REC-RECORD-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SystemSignalRef(Ref):
        dest: Optional[SystemSignalSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class SenderRecArrayTypeMapping:
    """
    If the ApplicationCompositeDataType is an Array, the "ArrayTypeMapping" will be
    used.

    :ivar array_element_mappings: Each ApplicationArrayElement shall be
        mapped on a SystemSignal.
    :ivar sender_to_signal_text_table_mapping: This mapping allows for
        the text-table translation between the sending DataPrototype
        that is defined in the PortPrototype and the physicalProps
        defined for the SystemSignal.
    :ivar signal_to_receiver_text_table_mapping: This mapping allows for
        the text-table translation between the physicalProps defined for
        the SystemSignal and a receiving DataPrototype that is defined
        in the PortPrototype.
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
        name = "SENDER-REC-ARRAY-TYPE-MAPPING"

    array_element_mappings: Optional[
        "SenderRecArrayTypeMapping.ArrayElementMappings"
    ] = field(
        default=None,
        metadata={
            "name": "ARRAY-ELEMENT-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sender_to_signal_text_table_mapping: Optional[TextTableMapping] = field(
        default=None,
        metadata={
            "name": "SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    signal_to_receiver_text_table_mapping: Optional[TextTableMapping] = field(
        default=None,
        metadata={
            "name": "SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING",
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
    class ArrayElementMappings:
        sender_rec_array_element_mapping: list[
            SenderRecArrayElementMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SENDER-REC-ARRAY-ELEMENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )


@dataclass
class SenderRecRecordElementMapping:
    """Mapping of a primitive record element to a SystemSignal.

    If the VariableDataPrototype that is referenced by
    SenderReceiverToSignalGroupMapping is typed by an
    ApplicationDataType the reference applicationRecordElement shall be
    used. If the VariableDataPrototype is typed by the
    ImplementationDataType the reference implementationRecordElement
    shall be used. Either the implementationRecordElement or
    applicationRecordElement reference shall be used. If the element is
    composite, there will be no mapping to the SystemSignal
    (multiplicity 0). In this case the RecordElementMapping element will
    aggregate the complexTypeMapping element. In that way also the
    composite datatypes can be mapped to SystemSignals.

    :ivar application_record_element_ref: Reference to an
        ApplicationRecordElement in the context of the dataElement or in
        the context of a composite element.
    :ivar complex_type_mapping: This aggregation will be used if the
        element is composite.
    :ivar implementation_record_element_ref: Reference to an
        ImplementationRecordElement in the context of the dataElement or
        in the context of a composite element.
    :ivar sender_to_signal_text_table_mapping: This mapping allows for
        the text-table translation between the sending DataPrototype
        that is defined in the PortPrototype and the physicalProps
        defined for the SystemSignal.
    :ivar signal_to_receiver_text_table_mapping: This mapping allows for
        the text-table translation between the physicalProps defined for
        the SystemSignal and a receiving DataPrototype that is defined
        in the PortPrototype.
    :ivar system_signal_ref: Reference to the system signal used to
        carry the primitive ApplicationRecordElement.
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
        name = "SENDER-REC-RECORD-ELEMENT-MAPPING"

    application_record_element_ref: Optional[
        "SenderRecRecordElementMapping.ApplicationRecordElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "APPLICATION-RECORD-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    complex_type_mapping: Optional[
        "SenderRecRecordElementMapping.ComplexTypeMapping"
    ] = field(
        default=None,
        metadata={
            "name": "COMPLEX-TYPE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implementation_record_element_ref: Optional[
        "SenderRecRecordElementMapping.ImplementationRecordElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-RECORD-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sender_to_signal_text_table_mapping: Optional[TextTableMapping] = field(
        default=None,
        metadata={
            "name": "SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    signal_to_receiver_text_table_mapping: Optional[TextTableMapping] = field(
        default=None,
        metadata={
            "name": "SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    system_signal_ref: Optional[
        "SenderRecRecordElementMapping.SystemSignalRef"
    ] = field(
        default=None,
        metadata={
            "name": "SYSTEM-SIGNAL-REF",
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
    class ApplicationRecordElementRef(Ref):
        dest: Optional[ApplicationRecordElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ComplexTypeMapping:
        sender_rec_array_type_mapping: Optional[SenderRecArrayTypeMapping] = (
            field(
                default=None,
                metadata={
                    "name": "SENDER-REC-ARRAY-TYPE-MAPPING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        sender_rec_record_type_mapping: Optional[
            "SenderRecRecordTypeMapping"
        ] = field(
            default=None,
            metadata={
                "name": "SENDER-REC-RECORD-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ImplementationRecordElementRef(Ref):
        dest: Optional[ImplementationDataTypeElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SystemSignalRef(Ref):
        dest: Optional[SystemSignalSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class SenderRecRecordTypeMapping:
    """
    If the ApplicationCompositeDataType is a Record, the "RecordTypeMapping" will
    be used.

    :ivar record_element_mappings: Each ApplicationRecordElement shall
        be mapped on a SystemSignal.
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
        name = "SENDER-REC-RECORD-TYPE-MAPPING"

    record_element_mappings: Optional[
        "SenderRecRecordTypeMapping.RecordElementMappings"
    ] = field(
        default=None,
        metadata={
            "name": "RECORD-ELEMENT-MAPPINGS",
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
    class RecordElementMappings:
        sender_rec_record_element_mapping: list[
            SenderRecRecordElementMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SENDER-REC-RECORD-ELEMENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
