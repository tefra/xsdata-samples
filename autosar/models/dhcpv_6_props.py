from dataclasses import dataclass, field
from typing import Optional
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Dhcpv6Props:
    """
    This meta-class specifies the configuration options for DHCPv6.

    :ivar tcp_ip_dhcp_v_6_cnf_delay_max: Maximum delay in seconds before
        sending the first Confirm message. If this value is bigger than
        the previous minimum delay value a random delay will be chosen
        from the interval.
    :ivar tcp_ip_dhcp_v_6_cnf_delay_min: Minimum delay in seconds before
        the first Confirm message will be sent.
    :ivar tcp_ip_dhcp_v_6_inf_delay_max: Maximum delay in seconds before
        sending the first Information Request message. If this value is
        bigger than the previous minimum delay value a random delay will
        be chosen from the interval.
    :ivar tcp_ip_dhcp_v_6_inf_delay_min: Minimum delay (s) before the
        first Information Request message will be sent.
    :ivar tcp_ip_dhcp_v_6_sol_delay_max: Maximum delay in seconds before
        sending the first Solicit message. If this value is bigger than
        the previous minimum delay value a random delay will be chosen
        from the interval.
    :ivar tcp_ip_dhcp_v_6_sol_delay_min: Minimum delay (s) before the
        first Solicit message will be sent.
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
        name = "DHCPV-6-PROPS"

    tcp_ip_dhcp_v_6_cnf_delay_max: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-IP-DHCP-V-6-CNF-DELAY-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_dhcp_v_6_cnf_delay_min: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-IP-DHCP-V-6-CNF-DELAY-MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_dhcp_v_6_inf_delay_max: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-IP-DHCP-V-6-INF-DELAY-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_dhcp_v_6_inf_delay_min: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-IP-DHCP-V-6-INF-DELAY-MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_dhcp_v_6_sol_delay_max: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-IP-DHCP-V-6-SOL-DELAY-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_dhcp_v_6_sol_delay_min: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-IP-DHCP-V-6-SOL-DELAY-MIN",
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
