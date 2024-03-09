from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .p_trigger_in_atomic_swc_type_instance_ref import (
    PTriggerInAtomicSwcTypeInstanceRef,
)
from .ref import Ref
from .trigger_subtypes_enum import TriggerSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcBswSynchronizedTrigger:
    """
    Synchronizes a Trigger provided by a component via a port with a Trigger
    provided by a BSW module or cluster.

    :ivar bsw_trigger_ref: The BSW Trigger.
    :ivar swc_trigger_iref: The SWC Trigger provided by a particular
        port.
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
        name = "SWC-BSW-SYNCHRONIZED-TRIGGER"

    bsw_trigger_ref: Optional["SwcBswSynchronizedTrigger.BswTriggerRef"] = (
        field(
            default=None,
            metadata={
                "name": "BSW-TRIGGER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    swc_trigger_iref: Optional[PTriggerInAtomicSwcTypeInstanceRef] = field(
        default=None,
        metadata={
            "name": "SWC-TRIGGER-IREF",
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
    class BswTriggerRef(Ref):
        dest: Optional[TriggerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
