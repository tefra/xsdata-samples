from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import VariationPoint
from autosar.models.integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SignalIPduCounter:
    """A PduCounter is included in a predefined set of Pdus and used to ensure
    that a sequence of Pdus is maintained.

    The counter is incremented when a Pdu is transmitted. The receivers
    check if the received Pdu is the next one in sequence.

    :ivar pdu_counter_size: Size of PduCounter expressed in bits.
        Range: 1..8
    :ivar pdu_counter_start_position: Position of PduCounter expressed
        in bits. Note that PduCounter is not allowed to cross a byte
        border.
    :ivar pdu_counter_threshold: Threshold value of IPduCounter
        algorithm. See AUTOSAR COM Spec for more details.
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
        name = "SIGNAL-I-PDU-COUNTER"

    pdu_counter_size: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "PDU-COUNTER-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pdu_counter_start_position: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "PDU-COUNTER-START-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pdu_counter_threshold: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "PDU-COUNTER-THRESHOLD",
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
