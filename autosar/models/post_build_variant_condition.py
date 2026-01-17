from dataclasses import dataclass, field
from typing import Optional

from .integer_value_variation_point import IntegerValueVariationPoint
from .post_build_variant_criterion_subtypes_enum import (
    PostBuildVariantCriterionSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PostBuildVariantCondition:
    """
    This class specifies the value which shall be assigned to a particular
    variant criterion in order to bind the variation point.

    If multiple criterion/value pairs are specified, they shall all match
    to bind the variation point. In other words binding can be represented
    by (criterion1 == value1) &amp;&amp; (condition2 == value2) ...

    :ivar matching_criterion_ref: This is the criterion which needs to
        match the value in order to make the PostbuildVariantCondition
        to be true.
    :ivar value: This is the particular value of the post-build variant
        criterion.
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
        name = "POST-BUILD-VARIANT-CONDITION"

    matching_criterion_ref: Optional[
        "PostBuildVariantCondition.MatchingCriterionRef"
    ] = field(
        default=None,
        metadata={
            "name": "MATCHING-CRITERION-REF",
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
    class MatchingCriterionRef(Ref):
        dest: Optional[PostBuildVariantCriterionSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
