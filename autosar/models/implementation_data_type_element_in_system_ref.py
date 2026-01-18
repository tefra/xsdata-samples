from __future__ import annotations

from dataclasses import dataclass, field

from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .implementation_data_type_element_subtypes_enum import (
    ImplementationDataTypeElementSubtypesEnum,
)
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)
from .system_subtypes_enum import SystemSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ImplementationDataTypeElementInSystemRef:
    """
    This meta-class represents the ability to refer to the internal
    structure of an AutosarDataPrototype which is typed by an
    ImplementationDatatype in the context of a CompositionSwComponentType.

    In other words, this meta-class shall not be used to model a reference
    to the AutosarDataPrototype as a target itself, even if the
    AutosarDataPrototype is typed by an ImplementationDataType and even if
    that ImplementationDataType represents a composite data type.

    :ivar tag_id: This attribute represents the ability to specify a
        tag-id for the serialization of a specific DataPrototype in the
        context of a (potentially deeply-nested) composite  data
        structure.
    :ivar base_ref: System that defines the context in which the
        ImplementationDataTypeElement is defined.
    :ivar context_swc_prototype_refs: This is the Software Component
        Prototype providing/receiving the referenced DataPrototype.
    :ivar context_port_prototype_ref: This is the port
        providing/receiving the referenced DataPrototype.
    :ivar root_data_prototype_ref: This refers to the
        AutosarDataPrototype which is typed by the
        ImplementationDatatype. The targetDataPrototype and all defined
        contextDataPrototypes can be found within this
        rootDataPrototype.
    :ivar context_implementation_data_element_refs: This is a context in
        case there are subelements with explicit types. The reference
        has to be ordered to properly reflect the nested structure.
    :ivar target_implementation_data_type_element_ref: This is a target
        ImplementationDataTypeElement in case that the rootDataPrototype
        is composite and the target of
        ImplementationCompositeDataTypeSubElementInSwcRef is a
        subElement of the rootDataPrototype.
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
        name = "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-SYSTEM-REF"

    tag_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TAG-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    base_ref: None | ImplementationDataTypeElementInSystemRef.BaseRef = field(
        default=None,
        metadata={
            "name": "BASE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_swc_prototype_refs: (
        None | ImplementationDataTypeElementInSystemRef.ContextSwcPrototypeRefs
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-SWC-PROTOTYPE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_port_prototype_ref: (
        None | ImplementationDataTypeElementInSystemRef.ContextPortPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_data_prototype_ref: (
        None | ImplementationDataTypeElementInSystemRef.RootDataPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "ROOT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_implementation_data_element_refs: (
        None
        | ImplementationDataTypeElementInSystemRef.ContextImplementationDataElementRefs
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_implementation_data_type_element_ref: (
        None
        | ImplementationDataTypeElementInSystemRef.TargetImplementationDataTypeElementRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF",
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

    @dataclass(kw_only=True)
    class BaseRef(Ref):
        dest: SystemSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextSwcPrototypeRefs:
        context_swc_prototype_ref: list[
            ImplementationDataTypeElementInSystemRef.ContextSwcPrototypeRefs.ContextSwcPrototypeRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTEXT-SWC-PROTOTYPE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class ContextSwcPrototypeRef(Ref):
            dest: SwComponentPrototypeSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class ContextPortPrototypeRef(Ref):
        dest: PortPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class RootDataPrototypeRef(Ref):
        dest: AutosarDataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextImplementationDataElementRefs:
        context_implementation_data_element_ref: list[
            ImplementationDataTypeElementInSystemRef.ContextImplementationDataElementRefs.ContextImplementationDataElementRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class ContextImplementationDataElementRef(Ref):
            dest: ImplementationDataTypeElementSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class TargetImplementationDataTypeElementRef(Ref):
        dest: ImplementationDataTypeElementSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
