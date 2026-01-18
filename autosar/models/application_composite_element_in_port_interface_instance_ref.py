from __future__ import annotations

from dataclasses import dataclass, field

from .application_composite_element_data_prototype_subtypes_enum import (
    ApplicationCompositeElementDataPrototypeSubtypesEnum,
)
from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
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

    root_data_prototype_ref: (
        None
        | ApplicationCompositeElementInPortInterfaceInstanceRef.RootDataPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "ROOT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_data_prototype_ref: list[
        ApplicationCompositeElementInPortInterfaceInstanceRef.ContextDataPrototypeRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_data_prototype_ref: (
        None
        | ApplicationCompositeElementInPortInterfaceInstanceRef.TargetDataPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-PROTOTYPE-REF",
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
    class RootDataPrototypeRef(Ref):
        dest: AutosarDataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextDataPrototypeRef(Ref):
        dest: ApplicationCompositeElementDataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetDataPrototypeRef(Ref):
        dest: ApplicationCompositeElementDataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
