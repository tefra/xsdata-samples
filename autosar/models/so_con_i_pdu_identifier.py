from dataclasses import dataclass, field
from typing import List, Optional
from .identifier import Identifier
from .pdu_collection_semantics_enum import PduCollectionSemanticsEnum
from .pdu_collection_trigger_enum import PduCollectionTriggerEnum
from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoConIPduIdentifier:
    """Identification of Pdu content on a socket connection.

    This Identifier is required in case that multiple Pdus are
    transmitted over the same socket connection.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar header_id: If multiple Pdus are transmitted over the same
        connection this headerId can be used to distinguish between the
        different Pdus.
    :ivar pdu_collection_pdu_timeout: Defines the timeout in seconds the
        PDU collection shall be transmitted at the latest after this PDU
        has been put into the buffer.
    :ivar pdu_collection_semantics: Specifies if the referenced
        PduTriggering shall be collected using a queued (i.e. all PDU
        instances) or last-is-best (i.e. only the last PDU instance)
        semantics. If this attribute is not present the behavior of
        "queued" is assumed.
    :ivar pdu_collection_trigger: Defines whether the referenced Pdu
        contributes to the triggering of the socket transmission if Pdu
        collection is enabled for this socket.
    :ivar pdu_triggering_ref: Reference to a Pdu that is transmitted
        over a socket connection.
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
        name = "SO-CON-I-PDU-IDENTIFIER"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["SoConIPduIdentifier.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    header_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "HEADER-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pdu_collection_pdu_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-PDU-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pdu_collection_semantics: Optional[PduCollectionSemanticsEnum] = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-SEMANTICS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pdu_collection_trigger: Optional[PduCollectionTriggerEnum] = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-TRIGGER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pdu_triggering_ref: Optional["SoConIPduIdentifier.PduTriggeringRef"] = field(
        default=None,
        metadata={
            "name": "PDU-TRIGGERING-REF",
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
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class PduTriggeringRef(Ref):
        dest: Optional[PduTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
