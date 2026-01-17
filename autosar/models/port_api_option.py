from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .communication_buffer_locking import CommunicationBufferLocking
from .data_transformation_error_handling_enum import (
    DataTransformationErrorHandlingEnum,
)
from .data_transformation_status_forwarding_enum import (
    DataTransformationStatusForwardingEnum,
)
from .port_defined_argument_value import PortDefinedArgumentValue
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PortApiOption:
    """
    Options how to generate the signatures of calls for an
    AtomicSwComponentType in order to communicate over a PortPrototype (for
    calls into a RunnableEntity as well as for calls from a RunnableEntity
    to the PortPrototype).

    :ivar enable_take_address: If set to true, the software-component is
        able to use the API reference for deriving a pointer to an
        object.
    :ivar error_handling: This specifies whether a RunnableEntity
        accessing a PortPrototype that is referenced by this
        PortAPIOption shall specifically handle transformer errors or
        not.
    :ivar indirect_api: If set to true this attribute specifies an
        "indirect API" to be generated for the associated port which
        means that the software-component is able to access the actions
        on a port via a pointer to an object representing a port. This
        allows e.g. iterating over ports in a loop. This option has no
        effect for PPortPrototypes of client/server interfaces.
    :ivar port_arg_values: An argument value defined by this port.
    :ivar port_ref: The option is valid for generated functions related
        to communication over this port
    :ivar supported_features: This collection specifies which features
        are supported by the RunnableEntitys which access a
        PortPrototype that it referenced by this PortAPIOption.
    :ivar transformer_status_forwarding: This specifies whether a
        RunnableEntity accessing a PortPrototype that is referenced by
        this PortAPIOption shall be able to forward a status to the
        transformer chain.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "PORT-API-OPTION"

    enable_take_address: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ENABLE-TAKE-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    error_handling: Optional[DataTransformationErrorHandlingEnum] = field(
        default=None,
        metadata={
            "name": "ERROR-HANDLING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    indirect_api: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "INDIRECT-API",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_arg_values: Optional["PortApiOption.PortArgValues"] = field(
        default=None,
        metadata={
            "name": "PORT-ARG-VALUES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_ref: Optional["PortApiOption.PortRef"] = field(
        default=None,
        metadata={
            "name": "PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    supported_features: Optional["PortApiOption.SupportedFeatures"] = field(
        default=None,
        metadata={
            "name": "SUPPORTED-FEATURES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformer_status_forwarding: Optional[
        DataTransformationStatusForwardingEnum
    ] = field(
        default=None,
        metadata={
            "name": "TRANSFORMER-STATUS-FORWARDING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class PortArgValues:
        port_defined_argument_value: list[PortDefinedArgumentValue] = field(
            default_factory=list,
            metadata={
                "name": "PORT-DEFINED-ARGUMENT-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PortRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SupportedFeatures:
        communication_buffer_locking: list[CommunicationBufferLocking] = field(
            default_factory=list,
            metadata={
                "name": "COMMUNICATION-BUFFER-LOCKING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
