from dataclasses import dataclass, field
from typing import Optional
from .admin_data import VariationPoint
from .identifier import Identifier
from .ref import Ref
from .trigger_subtypes_enum import TriggerSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswTriggerDirectImplementation:
    """
    Specifies a released trigger to be directly implemented via OS calls, for
    example in a Complex Driver module.

    :ivar cat_2_isr: The name of the OS category 2 ISR, which is
        controlled by the referred trigger. This means, that the module
        manages the category 2 ISR (e.g. according hardware
        initialization and enabling of ISR). Instead of calling an RTE /
        SchM API to raise the appropriate events in components or
        modules receiving the trigger, this ISR directly schedules the
        triggered ExecutableEntitys. The ISR name is required by the
        integrator to map the BswEvents and RTEEvents to  this ISR.
    :ivar mastered_trigger_ref: The trigger which is directly mastered
        by this module. There may be several different
        BswTriggerDirectImplementations mastering the same Trigger. This
        may be required e.g. due to memory partitioning.
    :ivar task: The name of the OS task, which is controlled by the
        referred trigger. This means, that the module uses the trigger
        condition to directly activate an OS task instead of calling an
        API of the BswScheduler. The task name is required by the RTE
        generator resp. BswScheduler to raise the appropriate events in
        components or modules receiving the trigger.
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
        name = "BSW-TRIGGER-DIRECT-IMPLEMENTATION"

    cat_2_isr: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "CAT-2-ISR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mastered_trigger_ref: Optional[
        "BswTriggerDirectImplementation.MasteredTriggerRef"
    ] = field(
        default=None,
        metadata={
            "name": "MASTERED-TRIGGER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    task: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "TASK",
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
    class MasteredTriggerRef(Ref):
        dest: Optional[TriggerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
