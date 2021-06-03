from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.operation_in_system_instance_ref import OperationInSystemInstanceRef
from autosar.models.swc_to_swc_operation_arguments_direction_enum import SwcToSwcOperationArgumentsDirectionEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcToSwcOperationArguments:
    """The SwcToSwcOperationArguments describes the information (client server
    operation arguments, plus the operation identification, if required) that
    are exchanged between two SW Components from exactly one client to one
    server, or from one server back to one client.

    The direction attribute defines which direction is described. If
    direction == IN, all arguments sent from the client to the server
    are described by the SwcToSwcOperationArguments, in direction ==
    OUT, it's the arguments sent back from server to client.

    :ivar direction: Direction addressed by this
        SwcToSwcClientServerOperation element.
    :ivar operation_irefs: Reference to the operation at the client and
        at the server side whose arguments are described by
        SwcToSwcOperationArguments. The two ports referenced shall be
        connected by a connector in the software component description.
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
        name = "SWC-TO-SWC-OPERATION-ARGUMENTS"

    direction: Optional[SwcToSwcOperationArgumentsDirectionEnum] = field(
        default=None,
        metadata={
            "name": "DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    operation_irefs: Optional["SwcToSwcOperationArguments.OperationIrefs"] = field(
        default=None,
        metadata={
            "name": "OPERATION-IREFS",
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
    class OperationIrefs:
        operation_iref: List[OperationInSystemInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "OPERATION-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 2,
            }
        )
