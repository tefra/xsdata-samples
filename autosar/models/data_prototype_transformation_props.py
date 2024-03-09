from dataclasses import dataclass, field
from typing import Optional
from .data_prototype_in_port_interface_ref import (
    DataPrototypeInPortInterfaceRef,
)
from .data_prototype_with_application_data_type_in_system_ref import (
    DataPrototypeWithApplicationDataTypeInSystemRef,
)
from .implementation_data_type_element_in_port_interface_ref import (
    ImplementationDataTypeElementInPortInterfaceRef,
)
from .implementation_data_type_element_in_system_ref import (
    ImplementationDataTypeElementInSystemRef,
)
from .ref import Ref
from .sw_data_def_props import SwDataDefProps
from .transformation_props_subtypes_enum import TransformationPropsSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataPrototypeTransformationProps:
    """
    DataPrototypeTransformationProps allows to set the attributes for the different
    TransformationTechnologies that are DataPrototype specific.

    :ivar data_protototype_in_port_interface_ref: Reference to a
        DataPrototype that is transported in the serialized ISignal.
    :ivar data_prototype_in_port_interface_ref: Reference to a
        DataPrototype that is transported in the serialized ISignal.
    :ivar data_prototype_ref: Reference to a DataPrototype that is
        transported in the serialized ISignal.
    :ivar network_representation_props: Specification of the actual
        network representation for the referenced primitive
        DataPrototype. If a network representation is provided then the
        baseType shall be used by the Transformer as input for the
        serialization/deserilaization.
    :ivar transformation_props_ref: Collection of AutosarDataPrototype
        related configuration settings for a transformer.
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
        name = "DATA-PROTOTYPE-TRANSFORMATION-PROPS"

    data_protototype_in_port_interface_ref: Optional[
        "DataPrototypeTransformationProps.DataProtototypeInPortInterfaceRef"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-PROTOTOTYPE-IN-PORT-INTERFACE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_prototype_in_port_interface_ref: Optional[
        "DataPrototypeTransformationProps.DataPrototypeInPortInterfaceRef"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_prototype_ref: Optional[
        "DataPrototypeTransformationProps.DataPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_representation_props: Optional[SwDataDefProps] = field(
        default=None,
        metadata={
            "name": "NETWORK-REPRESENTATION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformation_props_ref: Optional[
        "DataPrototypeTransformationProps.TransformationPropsRef"
    ] = field(
        default=None,
        metadata={
            "name": "TRANSFORMATION-PROPS-REF",
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
    class DataProtototypeInPortInterfaceRef:
        data_prototype_in_port_interface_ref: Optional[
            DataPrototypeInPortInterfaceRef
        ] = field(
            default=None,
            metadata={
                "name": "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        implementation_data_type_element_in_port_interface_ref: Optional[
            ImplementationDataTypeElementInPortInterfaceRef
        ] = field(
            default=None,
            metadata={
                "name": "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataPrototypeInPortInterfaceRef:
        data_prototype_in_port_interface_ref: Optional[
            DataPrototypeInPortInterfaceRef
        ] = field(
            default=None,
            metadata={
                "name": "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        implementation_data_type_element_in_port_interface_ref: Optional[
            ImplementationDataTypeElementInPortInterfaceRef
        ] = field(
            default=None,
            metadata={
                "name": "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataPrototypeRef:
        data_prototype_with_application_data_type_in_system_ref: Optional[
            DataPrototypeWithApplicationDataTypeInSystemRef
        ] = field(
            default=None,
            metadata={
                "name": "DATA-PROTOTYPE-WITH-APPLICATION-DATA-TYPE-IN-SYSTEM-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        implementation_data_type_element_in_system_ref: Optional[
            ImplementationDataTypeElementInSystemRef
        ] = field(
            default=None,
            metadata={
                "name": "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-SYSTEM-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TransformationPropsRef(Ref):
        dest: Optional[TransformationPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
