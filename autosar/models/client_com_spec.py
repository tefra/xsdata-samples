from dataclasses import dataclass, field
from typing import Optional

from .client_intent_enum import ClientIntentEnum
from .client_server_operation_subtypes_enum import (
    ClientServerOperationSubtypesEnum,
)
from .end_to_end_transformation_com_spec_props import (
    EndToEndTransformationComSpecProps,
)
from .field_subtypes_enum import FieldSubtypesEnum
from .ref import Ref
from .time_value import TimeValue
from .user_defined_transformation_com_spec_props import (
    UserDefinedTransformationComSpecProps,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ClientComSpec:
    """@RESTRICT_TO_STANDARD:CP!
    Client-specific communication attributes (RPortPrototype typed by ClientServerInterface).
    @END_RESTRICT_TO_STANDARD!
    @RESTRICT_TO_STANDARD:AP!
    Client-specific communication attributes (RPortPrototype typed by ServiceInterface) that are relevant for methods and field getters and setters.
    @END_RESTRICT_TO_STANDARD!

    :ivar client_intent: This attribute represents the expressed intent
        of the sender. The sender may decide to claim that existing
        resources of a ServiceInterface are expressly not used by this
        specific sender. The conceptual background of this claim may be
        driven by security, safety, etc."
    :ivar end_to_end_call_response_timeout: This attribute defines the
        maximum time interval in which the application shall expect the
        servers's response (time between the sending of the call
        invocation until the arrival of the server's response).
    :ivar getter_ref: The existence of this reference indicates that the
        ClientComSpec refers to the getter of a Field.
    :ivar operation_ref: This represents the corresponding
        ClientServerOperation.
    :ivar setter_ref: The existence of this reference indicates that the
        ClientComSpec refers to the setter of a Field.
    :ivar transformation_com_spec_propss: This references the
        TransformationComSpecProps which define port-specific
        configuration for data transformation.
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
        name = "CLIENT-COM-SPEC"

    client_intent: Optional[ClientIntentEnum] = field(
        default=None,
        metadata={
            "name": "CLIENT-INTENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    end_to_end_call_response_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "END-TO-END-CALL-RESPONSE-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    getter_ref: Optional["ClientComSpec.GetterRef"] = field(
        default=None,
        metadata={
            "name": "GETTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    operation_ref: Optional["ClientComSpec.OperationRef"] = field(
        default=None,
        metadata={
            "name": "OPERATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    setter_ref: Optional["ClientComSpec.SetterRef"] = field(
        default=None,
        metadata={
            "name": "SETTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformation_com_spec_propss: Optional[
        "ClientComSpec.TransformationComSpecPropss"
    ] = field(
        default=None,
        metadata={
            "name": "TRANSFORMATION-COM-SPEC-PROPSS",
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
    class GetterRef(Ref):
        dest: Optional[FieldSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class OperationRef(Ref):
        dest: Optional[ClientServerOperationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SetterRef(Ref):
        dest: Optional[FieldSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TransformationComSpecPropss:
        end_to_end_transformation_com_spec_props: list[
            EndToEndTransformationComSpecProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_transformation_com_spec_props: list[
            UserDefinedTransformationComSpecProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
