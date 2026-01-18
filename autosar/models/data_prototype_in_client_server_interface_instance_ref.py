from __future__ import annotations

from dataclasses import dataclass, field

from .application_composite_element_data_prototype_subtypes_enum import (
    ApplicationCompositeElementDataPrototypeSubtypesEnum,
)
from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .data_prototype_subtypes_enum import DataPrototypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataPrototypeInClientServerInterfaceInstanceRef:
    """
    :ivar root_data_prototype_in_cs_ref:
    :ivar context_data_prototype_in_cs_ref:
    :ivar target_data_prototype_in_cs_ref:
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
        name = "DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-INSTANCE-REF"

    root_data_prototype_in_cs_ref: (
        None
        | DataPrototypeInClientServerInterfaceInstanceRef.RootDataPrototypeInCsRef
    ) = field(
        default=None,
        metadata={
            "name": "ROOT-DATA-PROTOTYPE-IN-CS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_data_prototype_in_cs_ref: list[
        DataPrototypeInClientServerInterfaceInstanceRef.ContextDataPrototypeInCsRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-IN-CS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_data_prototype_in_cs_ref: (
        None
        | DataPrototypeInClientServerInterfaceInstanceRef.TargetDataPrototypeInCsRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-PROTOTYPE-IN-CS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class RootDataPrototypeInCsRef(Ref):
        dest: None | AutosarDataPrototypeSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextDataPrototypeInCsRef(Ref):
        dest: None | ApplicationCompositeElementDataPrototypeSubtypesEnum = (
            field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
        )

    @dataclass
    class TargetDataPrototypeInCsRef(Ref):
        dest: None | DataPrototypeSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
