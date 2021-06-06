from dataclasses import dataclass, field
from typing import Optional
from .abstract_required_port_prototype_subtypes_enum import AbstractRequiredPortPrototypeSubtypesEnum
from .client_server_operation_subtypes_enum import ClientServerOperationSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ROperationInAtomicSwcInstanceRef:
    """
    :ivar context_r_port_ref:
    :ivar target_required_operation_ref:
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
        name = "R-OPERATION-IN-ATOMIC-SWC-INSTANCE-REF"

    context_r_port_ref: Optional["ROperationInAtomicSwcInstanceRef.ContextRPortRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-R-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_required_operation_ref: Optional["ROperationInAtomicSwcInstanceRef.TargetRequiredOperationRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-REQUIRED-OPERATION-REF",
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
    class ContextRPortRef(Ref):
        dest: Optional[AbstractRequiredPortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetRequiredOperationRef(Ref):
        dest: Optional[ClientServerOperationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
