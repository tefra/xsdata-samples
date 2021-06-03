from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.application_composite_element_data_prototype_subtypes_enum import ApplicationCompositeElementDataPrototypeSubtypesEnum
from autosar.models.autosar_data_prototype_subtypes_enum import AutosarDataPrototypeSubtypesEnum
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ApplicationCompositeElementInPortInterfaceInstanceRef:
    """
    :ivar root_data_prototype_ref: This refers to the dataPrototype
        which is typed by theApplicationDatatype in which which the
        target can be found.
    :ivar context_data_prototype_ref: This represents a context
        ApplicationCompositeDataPrototype
    :ivar target_data_prototype_ref: This represents the referenced
        ApplicationCompositeDataPrototype.
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
        name = "APPLICATION-COMPOSITE-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF"

    root_data_prototype_ref: Optional["ApplicationCompositeElementInPortInterfaceInstanceRef.RootDataPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "ROOT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_data_prototype_ref: List["ApplicationCompositeElementInPortInterfaceInstanceRef.ContextDataPrototypeRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_data_prototype_ref: Optional["ApplicationCompositeElementInPortInterfaceInstanceRef.TargetDataPrototypeRef"] = field(
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
    class RootDataPrototypeRef(Ref):
        dest: Optional[AutosarDataPrototypeSubtypesEnum] = field(
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
        dest: Optional[ApplicationCompositeElementDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
