from dataclasses import dataclass, field
from typing import Optional
from autosar.models.contained_i_pdu_collection_semantics_enum import ContainedIPduCollectionSemanticsEnum
from autosar.models.pdu_collection_trigger_enum import PduCollectionTriggerEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ContainedIPduProps:
    """
    Defines the aspects of an IPdu which can be collected inside a
    ContainerIPdu.

    :ivar collection_semantics: Defines whether this ContainedIPdu shall
        be collected using a last-is-best or queued semantics.
    :ivar header_id_long_header: Defines the header id this IPdu shall
        have in case this IPdu is put inside a ContainerIPdu with
        headerType = longHeader.
    :ivar header_id_short_header: Defines the header id this IPdu shall
        have in case this IPdu is put inside a ContainerIPdu with
        headerType = shortHeader.
    :ivar offset: Byte offset that describes the location of the
        ContainedPdu in the ContainerPdu if no header is used.
    :ivar priority: Defines a priority of a ContainedTxPdu. 255
        represents the lowest priority and 0 represent the highest
        priority.
    :ivar timeout: Defines a IPdu specific sender timeout which can
        reduce the ContainerIPdu timer when this containedIPdu is put
        inside the ContainerIPdu. This attribute is ignored on receiver
        side.
    :ivar trigger: Defines whether this IPdu does trigger the sending of
        the ContainerIPdu. This attribute is ignored on receiver side.
    :ivar update_indication_bit_position: The updateIndicationBit
        specifies the bit location of ContainedIPdu Update-Bit in the
        Container PDU. It indicates to the receivers that the
        ContainedIPdu in the ContainerIPdu was updated.
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
        name = "CONTAINED-I-PDU-PROPS"

    collection_semantics: Optional[ContainedIPduCollectionSemanticsEnum] = field(
        default=None,
        metadata={
            "name": "COLLECTION-SEMANTICS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    header_id_long_header: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "HEADER-ID-LONG-HEADER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    header_id_short_header: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "HEADER-ID-SHORT-HEADER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    priority: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    trigger: Optional[PduCollectionTriggerEnum] = field(
        default=None,
        metadata={
            "name": "TRIGGER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    update_indication_bit_position: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "UPDATE-INDICATION-BIT-POSITION",
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
