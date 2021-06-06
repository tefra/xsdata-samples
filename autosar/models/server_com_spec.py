from dataclasses import dataclass, field
from typing import List, Optional
from .client_server_operation_subtypes_enum import ClientServerOperationSubtypesEnum
from .end_to_end_transformation_com_spec_props import EndToEndTransformationComSpecProps
from .field_subtypes_enum import FieldSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .user_defined_transformation_com_spec_props import UserDefinedTransformationComSpecProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ServerComSpec:
    """@RESTRICT_TO_STANDARD:CP!
    Communication attributes for a server port (PPortPrototype and ClientServerInterface).
    @END_RESTRICT_TO_STANDARD!
    @RESTRICT_TO_STANDARD:AP!
    Server-specific communication attributes (PPortPrototype typed by ServiceInterface) that are relevant for methods and field getters and setters.
    @END_RESTRICT_TO_STANDARD!

    :ivar getter_ref: The existence of this reference indicates that the
        ServerComSpec refers to the getter of a Field.
    :ivar operation_ref: Operation these communication attributes apply
        to.
    :ivar queue_length: @RESTRICT_TO_STANDARD:CP! Length of call queue
        on the server side. The queue is implemented by the RTE. The
        value shall be greater or equal to 1. Setting the value of
        queueLength to 1 implies that incoming requests are rejected
        while another request that arrived earlier is being processed.
        @END_RESTRICT_TO_STANDARD! @RESTRICT_TO_STANDARD:AP! Length of
        call queue on the server side. @END_RESTRICT_TO_STANDARD!
    :ivar setter_ref: The existence of this reference indicates that the
        ServerComSpec refers to the setter of a Field.
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
        name = "SERVER-COM-SPEC"

    getter_ref: Optional["ServerComSpec.GetterRef"] = field(
        default=None,
        metadata={
            "name": "GETTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    operation_ref: Optional["ServerComSpec.OperationRef"] = field(
        default=None,
        metadata={
            "name": "OPERATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    queue_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "QUEUE-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    setter_ref: Optional["ServerComSpec.SetterRef"] = field(
        default=None,
        metadata={
            "name": "SETTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    transformation_com_spec_propss: Optional["ServerComSpec.TransformationComSpecPropss"] = field(
        default=None,
        metadata={
            "name": "TRANSFORMATION-COM-SPEC-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class GetterRef(Ref):
        dest: Optional[FieldSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class OperationRef(Ref):
        dest: Optional[ClientServerOperationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SetterRef(Ref):
        dest: Optional[FieldSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TransformationComSpecPropss:
        end_to_end_transformation_com_spec_props: List[EndToEndTransformationComSpecProps] = field(
            default_factory=list,
            metadata={
                "name": "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        user_defined_transformation_com_spec_props: List[UserDefinedTransformationComSpecProps] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
