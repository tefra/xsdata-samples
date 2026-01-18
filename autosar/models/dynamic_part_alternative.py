from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .i_signal_i_pdu_subtypes_enum import ISignalIPduSubtypesEnum
from .integer import Integer
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DynamicPartAlternative:
    """
    One of the Com IPdu alternatives that are transmitted in the Dynamic
    Part of the MultiplexedIPdu.

    The selectorFieldCode specifies which Com IPdu is contained in the
    DynamicPart within a certain transmission of a multiplexed PDU.

    :ivar i_pdu_ref: Reference to a Com IPdu which is routed to the
        IPduM module and is combined to a multiplexedPdu.
    :ivar initial_dynamic_part: Dynamic part that shall be used to
        initialize this multiplexed IPdu. Constraint: Only one
        "DynamicPartAlternative" in a "DynamicPart" shall be the
        initialDynamicPart.
    :ivar selector_field_code: The selector field is part of a
        multiplexed IPdu. It consists of contiguous bits. The value of
        the selector field selects the layout of the multiplexed part of
        the IPdu.
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
        name = "DYNAMIC-PART-ALTERNATIVE"

    i_pdu_ref: DynamicPartAlternative.IPduRef | None = field(
        default=None,
        metadata={
            "name": "I-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    initial_dynamic_part: Boolean | None = field(
        default=None,
        metadata={
            "name": "INITIAL-DYNAMIC-PART",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    selector_field_code: Integer | None = field(
        default=None,
        metadata={
            "name": "SELECTOR-FIELD-CODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class IPduRef(Ref):
        dest: ISignalIPduSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
