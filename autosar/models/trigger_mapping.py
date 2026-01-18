from __future__ import annotations

from dataclasses import dataclass, field

from .ref import Ref
from .trigger_subtypes_enum import TriggerSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class TriggerMapping:
    """
    Defines the mapping of two particular unequally named Triggers in the
    given context.

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

    first_trigger_ref: None | TriggerMapping.FirstTriggerRef = field(
        default=None,
        metadata={
            "name": "FIRST-TRIGGER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_trigger_ref: None | TriggerMapping.SecondTriggerRef = field(
        default=None,
        metadata={
            "name": "SECOND-TRIGGER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass(kw_only=True)
    class FirstTriggerRef(Ref):
        dest: TriggerSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SecondTriggerRef(Ref):
        dest: TriggerSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
