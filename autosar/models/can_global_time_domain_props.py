from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanGlobalTimeDomainProps:
    """
    Enables the definition of Can Global Time specific properties.

    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar fup_data_id_lists:
    :ivar ofns_data_id_lists:
    :ivar ofs_data_id_lists:
    :ivar sync_data_id_lists:
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
        name = "CAN-GLOBAL-TIME-DOMAIN-PROPS"

    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    fup_data_id_lists: CanGlobalTimeDomainProps.FupDataIdLists | None = field(
        default=None,
        metadata={
            "name": "FUP-DATA-ID-LISTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ofns_data_id_lists: CanGlobalTimeDomainProps.OfnsDataIdLists | None = (
        field(
            default=None,
            metadata={
                "name": "OFNS-DATA-ID-LISTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    ofs_data_id_lists: CanGlobalTimeDomainProps.OfsDataIdLists | None = field(
        default=None,
        metadata={
            "name": "OFS-DATA-ID-LISTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_data_id_lists: CanGlobalTimeDomainProps.SyncDataIdLists | None = (
        field(
            default=None,
            metadata={
                "name": "SYNC-DATA-ID-LISTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class FupDataIdLists:
        """
        :ivar fup_data_id_list: The DataIDList for FUP messages to
            calculate CRC.
        """

        fup_data_id_list: list[PositiveInteger] = field(
            default_factory=list,
            metadata={
                "name": "FUP-DATA-ID-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 16,
            },
        )

    @dataclass
    class OfnsDataIdLists:
        """
        :ivar ofns_data_id_list: The DataIDList for OFNS messages to
            calculate CRC.
        """

        ofns_data_id_list: list[PositiveInteger] = field(
            default_factory=list,
            metadata={
                "name": "OFNS-DATA-ID-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 16,
            },
        )

    @dataclass
    class OfsDataIdLists:
        """
        :ivar ofs_data_id_list: The DataIDList for OFS messages to
            calculate CRC.
        """

        ofs_data_id_list: list[PositiveInteger] = field(
            default_factory=list,
            metadata={
                "name": "OFS-DATA-ID-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 16,
            },
        )

    @dataclass
    class SyncDataIdLists:
        """
        :ivar sync_data_id_list: The DataIDList for SYNC messages to
            calculate CRC.
        """

        sync_data_id_list: list[PositiveInteger] = field(
            default_factory=list,
            metadata={
                "name": "SYNC-DATA-ID-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 16,
            },
        )
