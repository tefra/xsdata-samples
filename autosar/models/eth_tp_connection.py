from __future__ import annotations

from dataclasses import dataclass, field

from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .ref import Ref
from .tp_connection_ident import TpConnectionIdent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EthTpConnection:
    """
    A connection identifies which PduTriggerings shall be handled using the
    "TP" semantics.

    :ivar ident: This adds the ability to become referrable to
        TpConnection.
    :ivar tp_sdu_refs: Reference to a PduTriggering that shall be
        transported using the "TP" semantics.
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
        name = "ETH-TP-CONNECTION"

    ident: TpConnectionIdent | None = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tp_sdu_refs: EthTpConnection.TpSduRefs | None = field(
        default=None,
        metadata={
            "name": "TP-SDU-REFS",
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
    class TpSduRefs:
        tp_sdu_ref: list[EthTpConnection.TpSduRefs.TpSduRef] = field(
            default_factory=list,
            metadata={
                "name": "TP-SDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TpSduRef(Ref):
            dest: PduTriggeringSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
