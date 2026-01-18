from dataclasses import dataclass, field
from typing import Optional

from .dhcp_server_configuration import DhcpServerConfiguration
from .do_ip_entity import DoIpEntity
from .time_synchronization import TimeSynchronization

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InfrastructureServices:
    """
    Defines the network infrastructure services provided or consumed.

    :ivar dhcp_server_configuration: Defines the configuration of DHCP
        servers that are running on the network endpoint.
    :ivar do_ip_entity: Defines whether a infrastructure service that
        runs on the network endpoint is a DoIP-Entity.
    :ivar time_synchronization: Defines the servers / clients in a time
        synchronised network.
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
        name = "INFRASTRUCTURE-SERVICES"

    dhcp_server_configuration: DhcpServerConfiguration | None = field(
        default=None,
        metadata={
            "name": "DHCP-SERVER-CONFIGURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    do_ip_entity: DoIpEntity | None = field(
        default=None,
        metadata={
            "name": "DO-IP-ENTITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_synchronization: TimeSynchronization | None = field(
        default=None,
        metadata={
            "name": "TIME-SYNCHRONIZATION",
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
