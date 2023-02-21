from dataclasses import dataclass, field
from typing import Optional
from .annotation import (
    DocumentationBlock,
    VariationPoint,
)
from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .target_i_pdu_ref import TargetIPduRef

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IPduMapping:
    """
    Arranges those IPdus that are transferred by the gateway from one channel to
    the other in pairs and defines the mapping between them.

    :ivar introduction: This represents introductory documentation about
        the IPdu mapping.
    :ivar pdu_max_length: Define the maximum length in bytes which
        limits the length of the Pdu during gateway operation if the
        runtime length of the received Pdu exceeds this limit.
    :ivar pdur_tp_chunk_size: Optionally defines the to be configured
        Pdu Router TpChunkSize for this routing relation.
    :ivar source_i_pdu_ref: Source destination of the referencing
        mapping.
    :ivar target_i_pdu: Target destination of the referencing mapping.
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
        name = "I-PDU-MAPPING"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pdu_max_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PDU-MAX-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pdur_tp_chunk_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PDUR-TP-CHUNK-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    source_i_pdu_ref: Optional["IPduMapping.SourceIPduRef"] = field(
        default=None,
        metadata={
            "name": "SOURCE-I-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_i_pdu: Optional[TargetIPduRef] = field(
        default=None,
        metadata={
            "name": "TARGET-I-PDU",
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
    class SourceIPduRef(Ref):
        dest: Optional[PduTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
