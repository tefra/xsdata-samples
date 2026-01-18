from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class FrGlobalTimeDomainProps:
    """
    Enables the definition of Flexray GlobalTime specific properties.

    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "FR-GLOBAL-TIME-DOMAIN-PROPS"

    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ofs_data_id_lists: None | FrGlobalTimeDomainProps.OfsDataIdLists = field(
        default=None,
        metadata={
            "name": "OFS-DATA-ID-LISTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_data_id_lists: None | FrGlobalTimeDomainProps.SyncDataIdLists = field(
        default=None,
        metadata={
            "name": "SYNC-DATA-ID-LISTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
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
