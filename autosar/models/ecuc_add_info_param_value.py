from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.boolean import Boolean
from autosar.models.ecuc_parameter_def_subtypes_enum import EcucParameterDefSubtypesEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucAddInfoParamValue:
    """
    This parameter corresponds to EcucAddInfoParamDef.

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
        modules which reference these values.  If isAutoValue is not
        present the default is "false".
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar value: Holds the content of the formated text.
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
        name = "ECUC-ADD-INFO-PARAM-VALUE"

    index: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    definition_ref: Optional["EcucAddInfoParamValue.DefinitionRef"] = field(
        default=None,
        metadata={
            "name": "DEFINITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["EcucAddInfoParamValue.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    is_auto_value: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "IS-AUTO-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    value: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "VALUE",
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
    class DefinitionRef(Ref):
        dest: Optional[EcucParameterDefSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
