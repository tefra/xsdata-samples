from __future__ import annotations

from dataclasses import dataclass, field

from .identifier import Identifier
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment
from .string import String
from .time_sync_technology_enum import TimeSyncTechnologyEnum
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class TimeSyncServerConfiguration:
    """
    Defines the configuration of the time synchronisation server.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar priority: Server Priority.
    :ivar sync_interval: Synchronisation interval used by the time
        synchronisation server (in seconds).
    :ivar time_sync_server_identifier: Identifier of the TimeSyncServer.
    :ivar time_sync_technology: Defines the time synchronisation
        technology used. Possible values are: NTP_RFC958,
        PTP_IEEE1588_2002, PTP_IEEE1588_2008, AVB_IEEE802_1AS and
        others.
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
        name = "TIME-SYNC-SERVER-CONFIGURATION"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: (
        None | TimeSyncServerConfiguration.ShortNameFragments
    ) = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    priority: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_interval: None | TimeValue = field(
        default=None,
        metadata={
            "name": "SYNC-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_sync_server_identifier: None | String = field(
        default=None,
        metadata={
            "name": "TIME-SYNC-SERVER-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_sync_technology: None | TimeSyncTechnologyEnum = field(
        default=None,
        metadata={
            "name": "TIME-SYNC-TECHNOLOGY",
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
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
