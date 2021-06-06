from dataclasses import dataclass, field
from typing import List, Optional
from .application_composite_element_data_prototype_subtypes_enum import ApplicationCompositeElementDataPrototypeSubtypesEnum
from .data_prototype_subtypes_enum import DataPrototypeSubtypesEnum
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ParameterInAtomicSwcTypeInstanceRef:
    """
    This class implements an instance reference which can be applied for
    variables as well as for parameters.

    :ivar port_prototype_ref: This is the port providing the variable or
        the entry point to the variable structure.
    :ivar root_parameter_data_prototype_ref: This represents the entry
        point for references into a CompositeDataType.
    :ivar context_data_prototype_ref: This ist the context in a
        compositeDataType.
    :ivar target_data_prototype_ref: This is the target of the instance
        ref
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
        name = "PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"

    port_prototype_ref: Optional["ParameterInAtomicSwcTypeInstanceRef.PortPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    root_parameter_data_prototype_ref: Optional["ParameterInAtomicSwcTypeInstanceRef.RootParameterDataPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "ROOT-PARAMETER-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_data_prototype_ref: List["ParameterInAtomicSwcTypeInstanceRef.ContextDataPrototypeRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_data_prototype_ref: Optional["ParameterInAtomicSwcTypeInstanceRef.TargetDataPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-PROTOTYPE-REF",
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
    class PortPrototypeRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class RootParameterDataPrototypeRef(Ref):
        dest: Optional[DataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextDataPrototypeRef(Ref):
        dest: Optional[ApplicationCompositeElementDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetDataPrototypeRef(Ref):
        dest: Optional[DataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
