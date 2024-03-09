from dataclasses import dataclass, field
from typing import Optional

from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv4AutoIpProps:
    """
    Specifies the configuration options for Auto-IP (automatic private IP
    addressing).

    :ivar tcp_ip_auto_ip_init_timeout: This attribute specifies the
        time in seconds Auto-IP waits at startup, before beginning with
        ARP probing. This delay is used to give DHCP time to acquire a
        lease in case a DHCP server is present.
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
        name = "IPV-4-AUTO-IP-PROPS"

    tcp_ip_auto_ip_init_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-IP-AUTO-IP-INIT-TIMEOUT",
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
