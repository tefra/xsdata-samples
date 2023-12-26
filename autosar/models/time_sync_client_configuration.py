from dataclasses import dataclass, field
from typing import List, Optional
from .ordered_master import OrderedMaster
from .time_sync_technology_enum import TimeSyncTechnologyEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TimeSyncClientConfiguration:
    """
    Defines the configuration of the time synchronisation client.

    :ivar ordered_master_list: Defines a list of ordered
        NetworkEndpoints.
    :ivar time_sync_technology: Defines the time synchronisation
        technology used.
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
        name = "TIME-SYNC-CLIENT-CONFIGURATION"

    ordered_master_list: Optional[
        "TimeSyncClientConfiguration.OrderedMasterList"
    ] = field(
        default=None,
        metadata={
            "name": "ORDERED-MASTER-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_sync_technology: Optional[TimeSyncTechnologyEnum] = field(
        default=None,
        metadata={
            "name": "TIME-SYNC-TECHNOLOGY",
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
    class OrderedMasterList:
        ordered_master: List[OrderedMaster] = field(
            default_factory=list,
            metadata={
                "name": "ORDERED-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
