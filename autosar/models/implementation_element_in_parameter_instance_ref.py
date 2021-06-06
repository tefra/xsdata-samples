from dataclasses import dataclass, field
from typing import Optional
from .implementation_data_type_element_subtypes_enum import ImplementationDataTypeElementSubtypesEnum
from .parameter_data_prototype_subtypes_enum import ParameterDataPrototypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ImplementationElementInParameterInstanceRef:
    """Describes a reference to a particular ImplementationDataTypeElement
    instance in the context of a given ParameterDataPrototype.

    Thus it refers to a particular element in the implementation
    description of a software data structure. Use Case: The RTE
    generator publishes its generated structure of calibration
    parameters in its BSW module description using the "constantMemory"
    role of ParameterDataPrototypes. Each ParameterDataPrototype
    describes a group of single calibration parameters. In order to
    point to these single parameters, this "instance ref" is needed.
    Note that this class follows the pattern of an InstanceRef but is
    not implemented based on the abstract classes because the
    ImplementationDataType isn't either, especially because
    ImplementationDataTypeElement isn't derived from AtpPrototype.

    :ivar context_ref: The context for the referred element.
    :ivar target_ref: The referred data element.
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
        name = "IMPLEMENTATION-ELEMENT-IN-PARAMETER-INSTANCE-REF"

    context_ref: Optional["ImplementationElementInParameterInstanceRef.ContextRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_ref: Optional["ImplementationElementInParameterInstanceRef.TargetRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-REF",
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
    class ContextRef(Ref):
        dest: Optional[ParameterDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetRef(Ref):
        dest: Optional[ImplementationDataTypeElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
