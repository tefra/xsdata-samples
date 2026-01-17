from dataclasses import dataclass, field
from typing import Optional

from .implementation_data_type_element_subtypes_enum import (
    ImplementationDataTypeElementSubtypesEnum,
)
from .parameter_data_prototype_subtypes_enum import (
    ParameterDataPrototypeSubtypesEnum,
)
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ArParameterInImplementationDataInstanceRef:
    """
    This class represents the ability to navigate into an element inside of
    an ParameterDataPrototype typed by an ImplementationDatatype.

    Note that it shall not be used if the target is the
    ParameterDataPrototype itself (e.g. if the target is a primitive data
    type). Note that this class follows the pattern of an InstanceRef but
    is not implemented based on the abstract classes because the
    ImplementationDataType isn't either, especially because
    ImplementationDataTypeElement (intentionally) isn't derived from
    AtpPrototype.

    :ivar context_data_prototype_refs: This is a context in case there
        are subelements with explicit types. The reference has to be
        ordered to properly reflect the nested structure.
    :ivar port_prototype_ref: This reference points to the PortPrototype
        providing/receiving the root of the parameter.
    :ivar root_parameter_data_prototype_ref: This refers to the
        ParameterDataPrototype typed by the implementationDataType in
        which the target can be found.
    :ivar target_data_prototype_ref: This reference points to the target
        ImplementationDataTypeElement.
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
        name = "AR-PARAMETER-IN-IMPLEMENTATION-DATA-INSTANCE-REF"

    context_data_prototype_refs: Optional[
        "ArParameterInImplementationDataInstanceRef.ContextDataPrototypeRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_prototype_ref: Optional[
        "ArParameterInImplementationDataInstanceRef.PortPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_parameter_data_prototype_ref: Optional[
        "ArParameterInImplementationDataInstanceRef.RootParameterDataPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "ROOT-PARAMETER-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_data_prototype_ref: Optional[
        "ArParameterInImplementationDataInstanceRef.TargetDataPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-PROTOTYPE-REF",
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
    class ContextDataPrototypeRefs:
        context_data_prototype_ref: list[
            "ArParameterInImplementationDataInstanceRef.ContextDataPrototypeRefs.ContextDataPrototypeRef"
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
            dest: Optional[ImplementationDataTypeElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class PortPrototypeRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RootParameterDataPrototypeRef(Ref):
        dest: Optional[ParameterDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetDataPrototypeRef(Ref):
        dest: Optional[ImplementationDataTypeElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
