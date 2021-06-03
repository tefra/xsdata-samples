from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.mode_declaration_group_prototype_subtypes_enum import ModeDeclarationGroupPrototypeSubtypesEnum
from autosar.models.mode_declaration_subtypes_enum import ModeDeclarationSubtypesEnum
from autosar.models.port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.sw_component_prototype_subtypes_enum import SwComponentPrototypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeInSwcInstanceRef:
    """
    Instance reference to be capable of referencing a ModeDeclaration at a
    specific Mode Switch Port of a SW-C.

    :ivar context_component_ref: Specifies the SW component prototype
        representing the context.
    :ivar context_port_ref: Specifies the port prototype representing
        the context.
    :ivar context_mode_declaration_group_prototype_ref: Specifies the
        mode declaration group prototype that manifests the context.
    :ivar target_mode_declaration_ref: Specifies the specific mode
        declaration in the given context.
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
        name = "MODE-IN-SWC-INSTANCE-REF"

    context_component_ref: List["ModeInSwcInstanceRef.ContextComponentRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_port_ref: Optional["ModeInSwcInstanceRef.ContextPortRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_mode_declaration_group_prototype_ref: Optional["ModeInSwcInstanceRef.ContextModeDeclarationGroupPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_mode_declaration_ref: Optional["ModeInSwcInstanceRef.TargetModeDeclarationRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-MODE-DECLARATION-REF",
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
    class ContextModeDeclarationGroupPrototypeRef(Ref):
        dest: Optional[ModeDeclarationGroupPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetModeDeclarationRef(Ref):
        dest: Optional[ModeDeclarationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
