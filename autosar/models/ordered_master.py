from dataclasses import dataclass, field
from typing import Optional

from .positive_integer import PositiveInteger
from .ref import Ref
from .time_sync_server_configuration_subtypes_enum import (
    TimeSyncServerConfigurationSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class OrderedMaster:
    """
    Element in the network endpoint list.

    :ivar index: Defines the order of the network endpoint list (e.g. 0,
        1, 2, ...).
    :ivar time_sync_server_ref: Reference to a master (Time Sync
        Server).
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
        name = "ORDERED-MASTER"

    index: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_sync_server_ref: Optional["OrderedMaster.TimeSyncServerRef"] = field(
        default=None,
        metadata={
            "name": "TIME-SYNC-SERVER-REF",
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
    class TimeSyncServerRef(Ref):
        dest: Optional[TimeSyncServerConfigurationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
