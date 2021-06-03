from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import (
    Annotation,
    VariationPoint,
)
from autosar.models.hw_attribute_def_subtypes_enum import HwAttributeDefSubtypesEnum
from autosar.models.numerical_value_variation_point import NumericalValueVariationPoint
from autosar.models.ref import Ref
from autosar.models.verbatim_string import VerbatimString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class HwAttributeValue:
    """This metaclass represents the ability to assign a hardware attribute
    value.

    Note that v and vt are mutually exclusive.

    :ivar annotation: Optional annotation that can be added to each
        HwAttributeValue.
    :ivar hw_attribute_def_ref: This association represents the
        definition of the particular hardware attribute value.
    :ivar v: This represents a numerical hardware attribute value.
    :ivar vt: This represents a textual hardware attribute value.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "HW-ATTRIBUTE-VALUE"

    annotation: Optional[Annotation] = field(
        default=None,
        metadata={
            "name": "ANNOTATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    hw_attribute_def_ref: Optional["HwAttributeValue.HwAttributeDefRef"] = field(
        default=None,
        metadata={
            "name": "HW-ATTRIBUTE-DEF-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    v: Optional[NumericalValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "V",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    vt: Optional[VerbatimString] = field(
        default=None,
        metadata={
            "name": "VT",
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
    class HwAttributeDefRef(Ref):
        dest: Optional[HwAttributeDefSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
