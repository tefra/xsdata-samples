from __future__ import annotations

from dataclasses import dataclass, field

from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .cpp_implementation_data_type_context_target_subtypes_enum import (
    CppImplementationDataTypeContextTargetSubtypesEnum,
)
from .port_interface_subtypes_enum import PortInterfaceSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PortInterfaceElementInImplementationDatatypeRef:
    """
    This meta-class represents the ability to refer to the internal
    structure of an AutosarDataPrototype which is typed by an
    implementationDatatype in the context of a PortInterface.

    In other words, this meta-class shall not be used to model a reference
    to the '''AutosarDataPrototype as a target itself''', '''even''' if the
    AutosarDataPrototype is typed by an ImplementationDataType '''and
    even''' if that ImplementationDataType represents a composite data
    type.

    :ivar context_data_prototype_refs: This is a context in case there
        are subelements with explicit types. The reference has to be
        ordered to properly reflect the nested structure.
    :ivar port_interface_ref: This is the PortInterface that contains
        the rootDataPrototype.
    :ivar root_data_prototype_ref: This rootDataPrototype defines the
        AutosarDataPrototype in which the target can be found.
    :ivar target_data_prototype_ref: This is the target reference to a
        subElement that is defined inside of the rootDataPrototype.
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
        name = "PORT-INTERFACE-ELEMENT-IN-IMPLEMENTATION-DATATYPE-REF"

    context_data_prototype_refs: (
        PortInterfaceElementInImplementationDatatypeRef.ContextDataPrototypeRefs
        | None
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_interface_ref: (
        PortInterfaceElementInImplementationDatatypeRef.PortInterfaceRef | None
    ) = field(
        default=None,
        metadata={
            "name": "PORT-INTERFACE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_data_prototype_ref: (
        PortInterfaceElementInImplementationDatatypeRef.RootDataPrototypeRef
        | None
    ) = field(
        default=None,
        metadata={
            "name": "ROOT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_data_prototype_ref: (
        PortInterfaceElementInImplementationDatatypeRef.TargetDataPrototypeRef
        | None
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class ContextDataPrototypeRefs:
        context_data_prototype_ref: list[
            PortInterfaceElementInImplementationDatatypeRef.ContextDataPrototypeRefs.ContextDataPrototypeRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTEXT-DATA-PROTOTYPE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ContextDataPrototypeRef(Ref):
            dest: CppImplementationDataTypeContextTargetSubtypesEnum | None = (
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
    class PortInterfaceRef(Ref):
        dest: PortInterfaceSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RootDataPrototypeRef(Ref):
        dest: AutosarDataPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetDataPrototypeRef(Ref):
        dest: CppImplementationDataTypeContextTargetSubtypesEnum | None = (
            field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
        )
