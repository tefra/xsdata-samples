from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import VariationPoint
from .atp_feature_subtypes_enum import AtpFeatureSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AnyInstanceRef:
    """Describes a reference to any instance in an AUTOSAR model.

    This is the most generic form of an instance ref. Refer to the
    superclass notes for more details.

    :ivar context_element_ref: This is one step in the navigation path
        specified by the instance ref.
    :ivar target_ref: This is the target of the instance ref.
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
        name = "ANY-INSTANCE-REF"

    context_element_ref: List["AnyInstanceRef.ContextElementRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_ref: Optional["AnyInstanceRef.TargetRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-REF",
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
    class ContextElementRef(Ref):
        dest: Optional[AtpFeatureSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetRef(Ref):
        dest: Optional[AtpFeatureSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
