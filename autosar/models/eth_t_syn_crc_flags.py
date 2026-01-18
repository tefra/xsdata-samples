from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EthTSynCrcFlags:
    """
    Defines the fields of the message which shall be taken into account for
    CRC calculation and verification.

    :ivar crc_correction_field: CorrectionField from the Follow_Up
        Message Header shall be included in CRC calculation.
    :ivar crc_domain_number: DomainNumber from the Follow_Up Message
        Header shall be included in CRC calculation.
    :ivar crc_message_length: MessageLength from the Follow_Up Message
        Header shall be included in CRC calculation.
    :ivar crc_precise_origin_timestamp: PreciseOriginTimestamp from the
        Follow_Up Message Field shall be included in CRC calculation.
    :ivar crc_sequence_id: SequenceId from the Follow_Up Message Header
        shall be included in CRC calculation.
    :ivar crc_source_port_identity: SourcePortIdentity from the
        Follow_Up Message Header shall be included in CRC calculation.
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
        name = "ETH-T-SYN-CRC-FLAGS"

    crc_correction_field: Boolean | None = field(
        default=None,
        metadata={
            "name": "CRC-CORRECTION-FIELD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    crc_domain_number: Boolean | None = field(
        default=None,
        metadata={
            "name": "CRC-DOMAIN-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    crc_message_length: Boolean | None = field(
        default=None,
        metadata={
            "name": "CRC-MESSAGE-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    crc_precise_origin_timestamp: Boolean | None = field(
        default=None,
        metadata={
            "name": "CRC-PRECISE-ORIGIN-TIMESTAMP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    crc_sequence_id: Boolean | None = field(
        default=None,
        metadata={
            "name": "CRC-SEQUENCE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    crc_source_port_identity: Boolean | None = field(
        default=None,
        metadata={
            "name": "CRC-SOURCE-PORT-IDENTITY",
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
