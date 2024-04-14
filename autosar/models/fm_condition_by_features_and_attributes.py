from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional

from .fm_attribute_def_subtypes_enum import FmAttributeDefSubtypesEnum
from .fm_feature_subtypes_enum import FmFeatureSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FmConditionByFeaturesAndAttributes:
    """
    A boolean expression that has the syntax of the AUTOSAR formula language but
    uses only references to features or feature attributes (not system constants)
    as operands.

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
    :ivar content:
    """

    class Meta:
        name = "FM-CONDITION-BY-FEATURES-AND-ATTRIBUTES"

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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ATTRIBUTE-REF",
                    "type": ForwardRef(
                        "FmConditionByFeaturesAndAttributes.AttributeRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "FEATURE-REF",
                    "type": ForwardRef(
                        "FmConditionByFeaturesAndAttributes.FeatureRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
        },
    )

    @dataclass
    class AttributeRef(Ref):
        dest: Optional[FmAttributeDefSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class FeatureRef(Ref):
        dest: Optional[FmFeatureSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
