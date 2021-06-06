from dataclasses import dataclass, field
from typing import List, Optional
from .parameter_data_prototype_subtypes_enum import ParameterDataPrototypeSubtypesEnum
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref
from .root_sw_composition_prototype_subtypes_enum import RootSwCompositionPrototypeSubtypesEnum
from .sw_component_prototype_subtypes_enum import SwComponentPrototypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ParameterDataPrototypeInSystemInstanceRef:
    """
    :ivar context_composition_ref:
    :ivar context_component_ref:
    :ivar context_port_ref:
    :ivar target_parameter_data_prototype_ref:
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
        name = "PARAMETER-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF"

    context_composition_ref: Optional["ParameterDataPrototypeInSystemInstanceRef.ContextCompositionRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_component_ref: List["ParameterDataPrototypeInSystemInstanceRef.ContextComponentRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_port_ref: Optional["ParameterDataPrototypeInSystemInstanceRef.ContextPortRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_parameter_data_prototype_ref: Optional["ParameterDataPrototypeInSystemInstanceRef.TargetParameterDataPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-PARAMETER-DATA-PROTOTYPE-REF",
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
    class ContextCompositionRef(Ref):
        dest: Optional[RootSwCompositionPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextComponentRef(Ref):
        dest: Optional[SwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextPortRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetParameterDataPrototypeRef(Ref):
        dest: Optional[ParameterDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
