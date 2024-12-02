from dataclasses import dataclass, field
from typing import Optional

from .application_record_element_subtypes_enum import (
    ApplicationRecordElementSubtypesEnum,
)
from .argument_data_prototype_subtypes_enum import (
    ArgumentDataPrototypeSubtypesEnum,
)
from .implementation_data_type_element_subtypes_enum import (
    ImplementationDataTypeElementSubtypesEnum,
)
from .indexed_array_element import IndexedArrayElement
from .ref import Ref
from .system_signal_subtypes_enum import SystemSignalSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ClientServerArrayElementMapping:
    """The ApplicationArrayElement may be a primitive one or a composite one.

    If the element is primitive, it will be mapped to the "SystemSignal"
    (multiplicity 1). If the ArgumentDataPrototype that is referenced by
    ClientServerCompositeTypeMapping is typed by an ApplicationDataType
    the reference to the ApplicationArrayElement shall be used. If the
    VariableDataPrototype is typed by the ImplementationDataType the
    reference to the ImplementationArrayElement shall be used. If the
    element is composite, there will be no mapping to the "SystemSignal"
    (multiplicity 0). In this case the "ArrayElementMapping" Element
    will aggregate the "TypeMapping" Element. In that way also the
    composite datatypes can be mapped to SystemSignals. Regardless
    whether composite or primitive array element is mapped the indexed
    array element always needs to be specified.

    :ivar complex_type_mapping: This aggregation will be used if the
        element is  composite.
    :ivar indexed_array_element: Reference to an indexed array element
        in the context of the mappedOperation or in the context of a
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
        name = "CLIENT-SERVER-ARRAY-ELEMENT-MAPPING"

    complex_type_mapping: Optional[
        "ClientServerArrayElementMapping.ComplexTypeMapping"
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
        "ClientServerArrayElementMapping.SystemSignalRef"
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
        client_server_array_type_mapping: Optional[
            "ClientServerArrayTypeMapping"
        ] = field(
            default=None,
            metadata={
                "name": "CLIENT-SERVER-ARRAY-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        client_server_record_type_mapping: Optional[
            "ClientServerRecordTypeMapping"
        ] = field(
            default=None,
            metadata={
                "name": "CLIENT-SERVER-RECORD-TYPE-MAPPING",
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
class ClientServerArrayTypeMapping:
    """
    If the ApplicationCompositeDataType is an Array, the "ArrayTypeMapping" will be
    used.

    :ivar argument_ref: Reference to an argument in the context of the
        mappedOperation. Only ClientServerCompositeTypeMapping elements
        that are directly aggregated by the
        ClientServerToSignalGroupMapping shall contain this reference.
    :ivar array_element_mappings: Each ApplicationArrayElement must be
        mapped on a SystemSignal.
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
        name = "CLIENT-SERVER-ARRAY-TYPE-MAPPING"

    argument_ref: Optional["ClientServerArrayTypeMapping.ArgumentRef"] = field(
        default=None,
        metadata={
            "name": "ARGUMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    array_element_mappings: Optional[
        "ClientServerArrayTypeMapping.ArrayElementMappings"
    ] = field(
        default=None,
        metadata={
            "name": "ARRAY-ELEMENT-MAPPINGS",
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
    class ArgumentRef(Ref):
        dest: Optional[ArgumentDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ArrayElementMappings:
        client_server_array_element_mapping: list[
            ClientServerArrayElementMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-ARRAY-ELEMENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )


@dataclass
class ClientServerRecordElementMapping:
    """Mapping of a primitive record element to a SystemSignal.

    If the ArgumentDataPrototype that is referenced by
    ClientServerCompositeTypeMapping is typed by an ApplicationDataType
    the reference to the ApplicationRecordElement shall be used. If the
    VariableDataPrototype is typed by the ImplementationDataType the
    reference to the ImplementationRecordElement shall be used. If the
    element is composite, there will be no mapping (multiplicity 0). In
    this case the "RecordElementMapping" Element will aggregate the
    "TypeMapping" Element. In that way also the composite datatypes can
    be mapped to SystemSignals. Regardless whether composite or
    primitive record element is mapped the record element always needs
    to be specified.

    :ivar application_record_element_ref: Reference to a
        applicationRecordElement in the context of the mappedOperation
        or in the context of a composite element. This reference shall
        only be used if the ArgumentDataPrototype that is referenced by
        the ClientServerCompositeTypeMapping is typed by an
        ApplicationDataType.
    :ivar complex_type_mapping: This aggregation will be used if the
        element is  composite.
    :ivar implementation_record_element_ref: Reference to a
        ImplementationRecordElement in the context of the
        mappedOperation or in the context of a composite element. This
        reference shall only be used if the ArgumentDataPrototype that
        is referenced by the ClientServerCompositeTypeMapping is typed
        by an ImplementationDataType.
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
        name = "CLIENT-SERVER-RECORD-ELEMENT-MAPPING"

    application_record_element_ref: Optional[
        "ClientServerRecordElementMapping.ApplicationRecordElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "APPLICATION-RECORD-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    complex_type_mapping: Optional[
        "ClientServerRecordElementMapping.ComplexTypeMapping"
    ] = field(
        default=None,
        metadata={
            "name": "COMPLEX-TYPE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implementation_record_element_ref: Optional[
        "ClientServerRecordElementMapping.ImplementationRecordElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-RECORD-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    system_signal_ref: Optional[
        "ClientServerRecordElementMapping.SystemSignalRef"
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
        client_server_array_type_mapping: Optional[
            ClientServerArrayTypeMapping
        ] = field(
            default=None,
            metadata={
                "name": "CLIENT-SERVER-ARRAY-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        client_server_record_type_mapping: Optional[
            "ClientServerRecordTypeMapping"
        ] = field(
            default=None,
            metadata={
                "name": "CLIENT-SERVER-RECORD-TYPE-MAPPING",
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
class ClientServerRecordTypeMapping:
    """
    If the ApplicationCompositeDataType is a Record, the "RecordTypeMapping" will
    be used.

    :ivar argument_ref: Reference to an argument in the context of the
        mappedOperation. Only ClientServerCompositeTypeMapping elements
        that are directly aggregated by the
        ClientServerToSignalGroupMapping shall contain this reference.
    :ivar record_element_mappings: Each ApplicationRecordElement must be
        mapped on a SystemSignal.
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
        name = "CLIENT-SERVER-RECORD-TYPE-MAPPING"

    argument_ref: Optional["ClientServerRecordTypeMapping.ArgumentRef"] = (
        field(
            default=None,
            metadata={
                "name": "ARGUMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    record_element_mappings: Optional[
        "ClientServerRecordTypeMapping.RecordElementMappings"
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
    class ArgumentRef(Ref):
        dest: Optional[ArgumentDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RecordElementMappings:
        client_server_record_element_mapping: list[
            ClientServerRecordElementMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-RECORD-ELEMENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
