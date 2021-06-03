from dataclasses import dataclass, field
from typing import Optional
from autosar.models.time_sync_client_configuration import TimeSyncClientConfiguration
from autosar.models.time_sync_server_configuration import TimeSyncServerConfiguration

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TimeSynchronization:
    """
    Defines the servers / clients in a time synchronised network.

    :ivar time_sync_client: Configuration of the time synchronisation
        client.
    :ivar time_sync_server: Configuration of the time synchronisation
        server.
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
        name = "TIME-SYNCHRONIZATION"

    time_sync_client: Optional[TimeSyncClientConfiguration] = field(
        default=None,
        metadata={
            "name": "TIME-SYNC-CLIENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    time_sync_server: Optional[TimeSyncServerConfiguration] = field(
        default=None,
        metadata={
            "name": "TIME-SYNC-SERVER",
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
