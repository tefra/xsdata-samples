from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    Annotation,
    VariationPoint,
)
from .boolean import Boolean
from .ecuc_parameter_def_subtypes_enum import EcucParameterDefSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .verbatim_string import VerbatimString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucTextualParamValue:
    """
    Holding a value which is not subject to variation.

    :ivar index: Used to support the specification of ordering of
        parameter values.
    :ivar definition_ref: Reference to the definition of this
        EcucParameterValue subclasses in the ECU Configuration Parameter
        Definition.
    :ivar annotations: Possibility to provide additional notes while
        defining the ECU Configuration Parameter Values. These are not
        intended as documentation but are mere design notes.
    :ivar is_auto_value: If withAuto is set to "true" for this parameter
        definition the isAutoValue can be set to "true". If isAutoValue
        is set to "true" the actual value will not be considered during
        ECU Configuration but will be (re-)calculated by the code
        generator and stored in the value attribute afterwards. These
        implicit updated values might require a re-generation of other
        modules which reference these values. If isAutoValue is not
        present the default is "false".
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar value: Value of the parameter, not subject to variant
        handling.
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
        name = "ECUC-TEXTUAL-PARAM-VALUE"

    index: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    definition_ref: Optional["EcucTextualParamValue.DefinitionRef"] = field(
        default=None,
        metadata={
            "name": "DEFINITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["EcucTextualParamValue.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_auto_value: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "IS-AUTO-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    value: Optional[VerbatimString] = field(
        default=None,
        metadata={
            "name": "VALUE",
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
    class DefinitionRef(Ref):
        dest: Optional[EcucParameterDefSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
