from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .ref import Ref
from .supervised_entity_checkpoint_needs_subtypes_enum import SupervisedEntityCheckpointNeedsSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SupervisedEntityCheckpointNeedsRefConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar supervised_entity_checkpoint_needs_ref:
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
        name = "SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF-CONDITIONAL"

    supervised_entity_checkpoint_needs_ref: Optional["SupervisedEntityCheckpointNeedsRefConditional.SupervisedEntityCheckpointNeedsRef"] = field(
        default=None,
        metadata={
            "name": "SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF",
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
    class SupervisedEntityCheckpointNeedsRef(Ref):
        dest: Optional[SupervisedEntityCheckpointNeedsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
