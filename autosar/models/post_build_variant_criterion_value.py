from dataclasses import dataclass, field
from typing import Optional

from .admin_data import Annotation
from .integer_value_variation_point import IntegerValueVariationPoint
from .post_build_variant_criterion_subtypes_enum import (
    PostBuildVariantCriterionSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PostBuildVariantCriterionValue:
    """This class specifies the value which shall be assigned to a particular
    variant criterion in order to bind the variation point.

    If multiple criterion/value pairs are specified, they all shall
    match to bind the variation point.

    :ivar variant_criterion_ref: This association selects the variant
        criterion whose value is specified.
    :ivar value: This is the particular value of the post-build variant
        criterion.
    :ivar annotations: This provides the ability to add information why
        the value is set like it is.
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
        name = "POST-BUILD-VARIANT-CRITERION-VALUE"

    variant_criterion_ref: Optional[
        "PostBuildVariantCriterionValue.VariantCriterionRef"
    ] = field(
        default=None,
        metadata={
            "name": "VARIANT-CRITERION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    value: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["PostBuildVariantCriterionValue.Annotations"] = (
        field(
            default=None,
            metadata={
                "name": "ANNOTATIONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class VariantCriterionRef(Ref):
        dest: Optional[PostBuildVariantCriterionSubtypesEnum] = field(
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
