from dataclasses import dataclass, field
from typing import List, Optional
from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .implementation_data_type_element_subtypes_enum import (
    ImplementationDataTypeElementSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ImplementationDataTypeElementInPortInterfaceRef:
    """This meta-class represents the ability to refer to the internal structure of
    an AutosarDataPrototype which is typed by an ImplementationDatatype in the
    context of a PortInterface.

    In other words, this meta-class shall not be used to model a
    reference to the AutosarDataPrototype as a target itself, even if
    the AutosarDataPrototype is typed by an ImplementationDataType and
    even if that ImplementationDataType represents a composite data
    type.

    :ivar tag_id: This attribute represents the ability to specify a
        tag-id for the serialization of a specific DataPrototype in the
        context of a (potentially deeply-nested) composite  data
        structure.
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
        is composite and the target is a subElement of the
        rootDataPrototype.
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
        name = "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF"

    tag_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TAG-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_data_prototype_ref: Optional[
        "ImplementationDataTypeElementInPortInterfaceRef.RootDataPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "ROOT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_implementation_data_element_refs: Optional[
        "ImplementationDataTypeElementInPortInterfaceRef.ContextImplementationDataElementRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_implementation_data_type_element_ref: Optional[
        "ImplementationDataTypeElementInPortInterfaceRef.TargetImplementationDataTypeElementRef"
    ] = field(
        default=None,
        metadata={
            "name": "TARGET-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF",
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
    class RootDataPrototypeRef(Ref):
        dest: Optional[AutosarDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextImplementationDataElementRefs:
        context_implementation_data_element_ref: List[
            "ImplementationDataTypeElementInPortInterfaceRef.ContextImplementationDataElementRefs.ContextImplementationDataElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTEXT-IMPLEMENTATION-DATA-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ContextImplementationDataElementRef(Ref):
            dest: Optional[ImplementationDataTypeElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class TargetImplementationDataTypeElementRef(Ref):
        dest: Optional[ImplementationDataTypeElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
