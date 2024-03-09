from dataclasses import dataclass, field
from typing import List, Optional

from .client_server_operation_subtypes_enum import (
    ClientServerOperationSubtypesEnum,
)
from .data_prototype_mapping import DataPrototypeMapping
from .data_transformation_subtypes_enum import DataTransformationSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ClientServerOperationMapping:
    """
    Defines the mapping of two particular ClientServerOperations in context of two
    different ClientServerInterfaces.

    :ivar argument_mappings: Defines the mapping of two particular
        ArgumentDataPrototypes with unequal names or unequal semantic
        (resolution or range) in context of Operations.
    :ivar first_operation_ref: First to-be-mapped ClientServerOperation
        of a ClientServerInterface.
    :ivar first_to_second_data_transformation_ref: This reference
        indicates that a DataTransformation is intended in the context
        of the ClientServerOperationMapping.
    :ivar second_operation_ref: Second to-be-mapped
        ClientServerOperation of a ClientServerInterface.
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
        name = "CLIENT-SERVER-OPERATION-MAPPING"

    argument_mappings: Optional[
        "ClientServerOperationMapping.ArgumentMappings"
    ] = field(
        default=None,
        metadata={
            "name": "ARGUMENT-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    first_operation_ref: Optional[
        "ClientServerOperationMapping.FirstOperationRef"
    ] = field(
        default=None,
        metadata={
            "name": "FIRST-OPERATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    first_to_second_data_transformation_ref: Optional[
        "ClientServerOperationMapping.FirstToSecondDataTransformationRef"
    ] = field(
        default=None,
        metadata={
            "name": "FIRST-TO-SECOND-DATA-TRANSFORMATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_operation_ref: Optional[
        "ClientServerOperationMapping.SecondOperationRef"
    ] = field(
        default=None,
        metadata={
            "name": "SECOND-OPERATION-REF",
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
    class ArgumentMappings:
        data_prototype_mapping: List[DataPrototypeMapping] = field(
            default_factory=list,
            metadata={
                "name": "DATA-PROTOTYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class FirstOperationRef(Ref):
        dest: Optional[ClientServerOperationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class FirstToSecondDataTransformationRef(Ref):
        dest: Optional[DataTransformationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SecondOperationRef(Ref):
        dest: Optional[ClientServerOperationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
