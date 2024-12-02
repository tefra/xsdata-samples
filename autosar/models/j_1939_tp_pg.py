from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .i_pdu_subtypes_enum import IPduSubtypesEnum
from .integer import Integer
from .n_pdu_subtypes_enum import NPduSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class J1939TpPg:
    """
    A J1939TpPg represents one J1939 message (parameter group, PG) identified by
    the PGN (parameter group number) that can be received or transmitted via
    J1939Tp.

    :ivar direct_pdu_ref: In case of variable length IPdus (with system
        signals of variable length), an additional NPdu (with the PGN in
        the CAN ID) is used for messages with up to 8 bytes.
    :ivar pgn: Parameter group number (PGN) of a J1939 message
        (parameter group, PG) that can be received or transmitted via
        J1939Tp. The PGN may be omitted when the a directPdu is
        referenced and is mapped into a CanFrameTriggering with an
        identifier.
    :ivar requestable: Parameter Group can be triggered by the J1939
        request message.
    :ivar sdu_refs: Reference to IPdus that are segmented by the
        Transport Protocol. If more than one IPdu is referenced, the
        IPdus are used when the same PGN is received in parallel via
        different transport protocols (BAM, CMDT, direct) on the same
        J1939TpConnection.
    :ivar tp_sdu_ref: Reference to IPdus that are segmented by the
        Transport Protocol. To support the low-level routing of NPdu's
        the NPdu is a specialization of an IPdu. More details can be
        found in the NPdu class description. Nevertheless the
        J1939TpConnection must not reference a NPdu with this tpSdu
        reference.
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
        name = "J-1939-TP-PG"

    direct_pdu_ref: Optional["J1939TpPg.DirectPduRef"] = field(
        default=None,
        metadata={
            "name": "DIRECT-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pgn: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "PGN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    requestable: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "REQUESTABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdu_refs: Optional["J1939TpPg.SduRefs"] = field(
        default=None,
        metadata={
            "name": "SDU-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tp_sdu_ref: Optional["J1939TpPg.TpSduRef"] = field(
        default=None,
        metadata={
            "name": "TP-SDU-REF",
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
    class DirectPduRef(Ref):
        dest: Optional[NPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SduRefs:
        sdu_ref: list["J1939TpPg.SduRefs.SduRef"] = field(
            default_factory=list,
            metadata={
                "name": "SDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SduRef(Ref):
            dest: Optional[IPduSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class TpSduRef(Ref):
        dest: Optional[IPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
