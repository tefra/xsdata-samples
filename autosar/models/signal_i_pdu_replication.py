from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.i_signal_i_pdu_subtypes_enum import ISignalIPduSubtypesEnum
from autosar.models.integer import Integer
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SignalIPduReplication:
    """PduReplication is a form of redundancy where the data content of one
    ISignalIPdu (source) is transmitted inside a set of replica ISignalIPdus.

    These ISignalIPdus (copies) have different Pdu IDs, identical
    PduCounters, identical data content and are transmitted with the
    same frequency.

    :ivar pdu_replication_voting: Number of identical IPdus needed for
        successful voting (1-3).
    :ivar replica_pdus_refs: Reference to replica Pdus of this IPdu.
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
        name = "SIGNAL-I-PDU-REPLICATION"

    pdu_replication_voting: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "PDU-REPLICATION-VOTING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    replica_pdus_refs: Optional["SignalIPduReplication.ReplicaPdusRefs"] = field(
        default=None,
        metadata={
            "name": "REPLICA-PDUS-REFS",
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
    class ReplicaPdusRefs:
        replica_pdus_ref: List["SignalIPduReplication.ReplicaPdusRefs.ReplicaPdusRef"] = field(
            default_factory=list,
            metadata={
                "name": "REPLICA-PDUS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 2,
            }
        )

        @dataclass
        class ReplicaPdusRef(Ref):
            dest: Optional[ISignalIPduSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
