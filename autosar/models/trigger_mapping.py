from dataclasses import dataclass, field
from typing import Optional

from .ref import Ref
from .trigger_subtypes_enum import TriggerSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TriggerMapping:
    """
    Defines the mapping of two particular unequally named Triggers in the given
    context.

    :ivar first_trigger_ref: A Trigger to be mapped.
    :ivar second_trigger_ref: A Trigger to be mapped.
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
        name = "TRIGGER-MAPPING"

    first_trigger_ref: Optional["TriggerMapping.FirstTriggerRef"] = field(
        default=None,
        metadata={
            "name": "FIRST-TRIGGER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_trigger_ref: Optional["TriggerMapping.SecondTriggerRef"] = field(
        default=None,
        metadata={
            "name": "SECOND-TRIGGER-REF",
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
    class FirstTriggerRef(Ref):
        dest: Optional[TriggerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SecondTriggerRef(Ref):
        dest: Optional[TriggerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
