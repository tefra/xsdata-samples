from dataclasses import dataclass, field

from .boolean import Boolean

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EthTSynSubTlvConfig:
    """
    Defines the subTLV fields which shall be included in the time sync
    message.

    :ivar ofs_sub_tlv: Defines whether an AUTOSAR Follow_Up TLV OFS Sub-
        TLV is used.
    :ivar status_sub_tlv: Defines whether an AUTOSAR Follow_Up TLV
        Status Sub-TLV is used.
    :ivar time_sub_tlv: Defines whether an AUTOSAR Follow_Up TLV Time
        Sub-TLV is used.
    :ivar user_data_sub_tlv: Defines whether an AUTOSAR Follow_Up TLV
        UserData Sub-TLV is used.
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
        name = "ETH-T-SYN-SUB-TLV-CONFIG"

    ofs_sub_tlv: Boolean | None = field(
        default=None,
        metadata={
            "name": "OFS-SUB-TLV",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    status_sub_tlv: Boolean | None = field(
        default=None,
        metadata={
            "name": "STATUS-SUB-TLV",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_sub_tlv: Boolean | None = field(
        default=None,
        metadata={
            "name": "TIME-SUB-TLV",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    user_data_sub_tlv: Boolean | None = field(
        default=None,
        metadata={
            "name": "USER-DATA-SUB-TLV",
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
