from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .boolean import Boolean
from .bsw_internal_triggering_point_subtypes_enum import BswInternalTriggeringPointSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswInternalTriggeringPointPolicy:
    """
    The internal triggering point for which the BSW Scheduler using this
    policy.

    :ivar enable_take_address: If set to true, the BSW Module is able to
        use the API reference for deriving a pointer to an object
    :ivar bsw_internal_triggering_point_ref: The
        BswInternalTriggeringPoint for which the BSW Scheduler using
        this policy.
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
        name = "BSW-INTERNAL-TRIGGERING-POINT-POLICY"

    enable_take_address: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ENABLE-TAKE-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    bsw_internal_triggering_point_ref: Optional["BswInternalTriggeringPointPolicy.BswInternalTriggeringPointRef"] = field(
        default=None,
        metadata={
            "name": "BSW-INTERNAL-TRIGGERING-POINT-REF",
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
    class BswInternalTriggeringPointRef(Ref):
        dest: Optional[BswInternalTriggeringPointSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
