from __future__ import annotations

from dataclasses import dataclass, field

from .application_composite_element_data_prototype_subtypes_enum import (
    ApplicationCompositeElementDataPrototypeSubtypesEnum,
)
from .autosar_data_prototype_subtypes_enum import (
    AutosarDataPrototypeSubtypesEnum,
)
from .data_prototype_subtypes_enum import DataPrototypeSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DataPrototypeInPortInterfaceRef:
    """
    This class represents a RootDataPrototype that is typed by an
    ApplicationDataType or ImplementationDataType or a DataTypeElement that
    is aggregated within a composite application data type (record or
    array).

    :ivar tag_id: This attribute represents the ability to specify a
        tag-id for the serialization of a specific DataPrototype in the
        context of a (potentially deeply-nested) composite  data
        structure.
    :ivar data_prototype_iref: This element defines a reference to a
        DataPrototype in the context of a PortInterface.
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
        name = "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF"

    tag_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TAG-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_prototype_iref: (
        None | DataPrototypeInPortInterfaceRef.DataPrototypeIref
    ) = field(
        default=None,
        metadata={
            "name": "DATA-PROTOTYPE-IREF",
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
    class DataPrototypeIref:
        root_data_prototype_in_cs_ref: (
            None
            | DataPrototypeInPortInterfaceRef.DataPrototypeIref.RootDataPrototypeInCsRef
        ) = field(
            default=None,
            metadata={
                "name": "ROOT-DATA-PROTOTYPE-IN-CS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        context_data_prototype_in_cs_ref: list[
            DataPrototypeInPortInterfaceRef.DataPrototypeIref.ContextDataPrototypeInCsRef
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
            | DataPrototypeInPortInterfaceRef.DataPrototypeIref.TargetDataPrototypeInCsRef
        ) = field(
            default=None,
            metadata={
                "name": "TARGET-DATA-PROTOTYPE-IN-CS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        root_data_prototype_in_sr_ref: (
            None
            | DataPrototypeInPortInterfaceRef.DataPrototypeIref.RootDataPrototypeInSrRef
        ) = field(
            default=None,
            metadata={
                "name": "ROOT-DATA-PROTOTYPE-IN-SR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        context_data_prototype_in_sr_ref: list[
            DataPrototypeInPortInterfaceRef.DataPrototypeIref.ContextDataPrototypeInSrRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTEXT-DATA-PROTOTYPE-IN-SR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        target_data_prototype_in_sr_ref: (
            None
            | DataPrototypeInPortInterfaceRef.DataPrototypeIref.TargetDataPrototypeInSrRef
        ) = field(
            default=None,
            metadata={
                "name": "TARGET-DATA-PROTOTYPE-IN-SR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        root_data_prototype_ref: (
            None
            | DataPrototypeInPortInterfaceRef.DataPrototypeIref.RootDataPrototypeRef
        ) = field(
            default=None,
            metadata={
                "name": "ROOT-DATA-PROTOTYPE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        context_data_prototype_ref: list[
            DataPrototypeInPortInterfaceRef.DataPrototypeIref.ContextDataPrototypeRef
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
            | DataPrototypeInPortInterfaceRef.DataPrototypeIref.TargetDataPrototypeRef
        ) = field(
            default=None,
            metadata={
                "name": "TARGET-DATA-PROTOTYPE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class RootDataPrototypeInCsRef(Ref):
            dest: AutosarDataPrototypeSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class ContextDataPrototypeInCsRef(Ref):
            dest: ApplicationCompositeElementDataPrototypeSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class TargetDataPrototypeInCsRef(Ref):
            dest: DataPrototypeSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class RootDataPrototypeInSrRef(Ref):
            dest: AutosarDataPrototypeSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class ContextDataPrototypeInSrRef(Ref):
            dest: ApplicationCompositeElementDataPrototypeSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class TargetDataPrototypeInSrRef(Ref):
            dest: DataPrototypeSubtypesEnum = field(
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
            dest: DataPrototypeSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
