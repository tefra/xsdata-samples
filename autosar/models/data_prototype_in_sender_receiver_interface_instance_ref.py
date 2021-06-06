from dataclasses import dataclass, field
from typing import List, Optional
from .application_composite_element_data_prototype_subtypes_enum import ApplicationCompositeElementDataPrototypeSubtypesEnum
from .autosar_data_prototype_subtypes_enum import AutosarDataPrototypeSubtypesEnum
from .data_prototype_subtypes_enum import DataPrototypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataPrototypeInSenderReceiverInterfaceInstanceRef:
    """
    :ivar root_data_prototype_in_sr_ref:
    :ivar context_data_prototype_in_sr_ref:
    :ivar target_data_prototype_in_sr_ref:
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
        name = "DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-INSTANCE-REF"

    root_data_prototype_in_sr_ref: Optional["DataPrototypeInSenderReceiverInterfaceInstanceRef.RootDataPrototypeInSrRef"] = field(
        default=None,
        metadata={
            "name": "ROOT-DATA-PROTOTYPE-IN-SR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_data_prototype_in_sr_ref: List["DataPrototypeInSenderReceiverInterfaceInstanceRef.ContextDataPrototypeInSrRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-IN-SR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_data_prototype_in_sr_ref: Optional["DataPrototypeInSenderReceiverInterfaceInstanceRef.TargetDataPrototypeInSrRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-PROTOTYPE-IN-SR-REF",
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
    class RootDataPrototypeInSrRef(Ref):
        dest: Optional[AutosarDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextDataPrototypeInSrRef(Ref):
        dest: Optional[ApplicationCompositeElementDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetDataPrototypeInSrRef(Ref):
        dest: Optional[DataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
