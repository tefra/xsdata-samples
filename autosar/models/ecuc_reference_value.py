from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    Annotation,
    VariationPoint,
)
from .ecuc_abstract_reference_def_subtypes_enum import (
    EcucAbstractReferenceDefSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref
from .referrable_subtypes_enum import ReferrableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class EcucReferenceValue:
    """
    Used to represent a configuration value that has a parameter definition
    of type EcucAbstractReferenceDef (used for all of its specializations
    excluding EcucInstanceReferenceDef).

    :ivar index: Used to support the specification of ordering of
        parameter values.
    :ivar definition_ref: Reference to the definition of this
        EcucAbstractReferenceValue subclasses in the ECU Configuration
        Parameter Definition.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar value_ref: Specifies the destination of the reference.
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
        name = "ECUC-REFERENCE-VALUE"

    index: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    definition_ref: None | EcucReferenceValue.DefinitionRef = field(
        default=None,
        metadata={
            "name": "DEFINITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: None | EcucReferenceValue.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    value_ref: None | EcucReferenceValue.ValueRef = field(
        default=None,
        metadata={
            "name": "VALUE-REF",
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
    class DefinitionRef(Ref):
        dest: EcucAbstractReferenceDefSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ValueRef(Ref):
        dest: ReferrableSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
