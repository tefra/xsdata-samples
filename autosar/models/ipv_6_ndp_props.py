from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class Ipv6NdpProps:
    """
    This meta-class specifies the configuration options for the Neighbor
    Discovery Protocol for IPv6.

    :ivar tcp_ip_ndp_default_reachable_time: Configuration of the
        ReachableTime (s) specified in [RFC4861 6.3.2. Host Variables].
    :ivar tcp_ip_ndp_default_retrans_timer: Configures the default value
        (s) for the RetransTimer variable specified in [RFC4861 6.3.2.
        Host Variables].
    :ivar tcp_ip_ndp_default_router_list_size: Maximum number of default
        router entries.
    :ivar tcp_ip_ndp_defensive_processing: If enabled the NDP shall only
        process Neighbor Advertisements which are received in reaction
        to a previously transmitted Neighbor Solicitation as well as
        skipping updates to the Neighbor Cache based on received
        Neighbor Solicitations. If disabled all Neighbor Advertisements
        and Solicitations shall be processed as specified in RFC4861.
    :ivar tcp_ip_ndp_delay_first_probe_time: Delay before sending the
        first NUD probe in (s).
    :ivar tcp_ip_ndp_destination_cache_size: Maximum number of entries
        in the destination cache.
    :ivar tcp_ip_ndp_dynamic_hop_limit_enabled: If enabled the default
        hop limit may be reconfigured based on received Router
        Advertisements.
    :ivar tcp_ip_ndp_dynamic_mtu_enabled: Allow dynamic reconfiguration
        of link MTU via Router Advertisements.
    :ivar tcp_ip_ndp_dynamic_reachable_time_enabled: If enabled the
        default Reachable Time value may be reconfigured based on
        received Router Advertisements.
    :ivar tcp_ip_ndp_dynamic_retrans_time_enabled: If enabled the
        default Retransmit Timer value may be reconfigured based on
        received Router Advertisements.
    :ivar tcp_ip_ndp_max_random_factor: Maximum random factor used for
        randomization
    :ivar tcp_ip_ndp_max_rtr_solicitation_delay: Maximum delay before
        the first Router Solicitation will be sent after interface
        initialization in (s).
    :ivar tcp_ip_ndp_max_rtr_solicitations: Maximum number of Router
        Solicitations that will be sent before the first Router
        Advertisement has been received.
    :ivar tcp_ip_ndp_min_random_factor: Minimum random factor used for
        randomization
    :ivar tcp_ip_ndp_neighbor_unreachability_detection_enabled: Neighbor
        Unreachability Detection is used to remove unused entries from
        the neighbor cache. This feature is a basic feature of NDP and
        should be turned on.
    :ivar tcp_ip_ndp_num_multicast_solicitations: Maximum number of
        multicast solicitations that will be sent when performing
        address resolution.
    :ivar tcp_ip_ndp_num_unicast_solicitations: Maximum number of
        unicast solicitations that will be sent when performig Neighbor
        Unreachability Detection.
    :ivar tcp_ip_ndp_packet_queue_enabled: Enables (TRUE) or disables
        (FALSE) support of a NDP Packet Queue according to IETF RFC
        4861, section 7.2.2.
    :ivar tcp_ip_ndp_prefix_list_size: Maximum number of entries in the
        on-link prefix list.
    :ivar tcp_ip_ndp_random_reachable_time_enabled: If enabled the value
        of ReachableTime will be multiplied with a random value between
        MIN_RANDOM_FACTOR and MAX_RANDOM_FACTOR in order to prevent
        multiple nodes from transmitting at exactly the same time.
    :ivar tcp_ip_ndp_rnd_rtr_solicitation_delay_enabled: If enabled the
        first router solicitation will be delayed randomly from
        [0...MAX_RTR_SOLICITATION_DELAY]. Otherwise the first router
        solicitation will be sent after exactly
        MAX_RTR_SOLICITATION_DELAY milliseconds.
    :ivar tcp_ip_ndp_rtr_solicitation_interval: Interval between
        consecutive Router Solicitations in (s).
    :ivar tcp_ip_ndp_slaac_dad_number_of_transmissions: Number of
        Neighbor Solicitations that have to be unanswered in order to
        set an autoconfigurated address to PREFERRED (usable) state.
    :ivar tcp_ip_ndp_slaac_dad_retransmission_delay: Sets the maximum
        value for the address configuration delay (s).
    :ivar tcp_ip_ndp_slaac_delay_enabled: If enabled transmission of the
        first DAD Neighbor Solicitation will be delayed by a random
        value from [0...MAX_DAD_DELAY].
    :ivar tcp_ip_ndp_slaac_optimistic_dad_enabled: Enable Optimistic
        Duplicate Address Detection (DAD) according to RFC4429.
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
        name = "IPV-6-NDP-PROPS"

    tcp_ip_ndp_default_reachable_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DEFAULT-REACHABLE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_default_retrans_timer: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DEFAULT-RETRANS-TIMER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_default_router_list_size: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_defensive_processing: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DEFENSIVE-PROCESSING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_delay_first_probe_time: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DELAY-FIRST-PROBE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_destination_cache_size: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DESTINATION-CACHE-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_dynamic_hop_limit_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DYNAMIC-HOP-LIMIT-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_dynamic_mtu_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DYNAMIC-MTU-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_dynamic_reachable_time_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DYNAMIC-REACHABLE-TIME-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_dynamic_retrans_time_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-DYNAMIC-RETRANS-TIME-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_max_random_factor: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-MAX-RANDOM-FACTOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_max_rtr_solicitation_delay: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-MAX-RTR-SOLICITATION-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_max_rtr_solicitations: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-MAX-RTR-SOLICITATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_min_random_factor: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-MIN-RANDOM-FACTOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_neighbor_unreachability_detection_enabled: None | Boolean = (
        field(
            default=None,
            metadata={
                "name": "TCP-IP-NDP-NEIGHBOR-UNREACHABILITY-DETECTION-ENABLED",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    tcp_ip_ndp_num_multicast_solicitations: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-NUM-MULTICAST-SOLICITATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_num_unicast_solicitations: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-NUM-UNICAST-SOLICITATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_packet_queue_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-PACKET-QUEUE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_prefix_list_size: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-PREFIX-LIST-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_random_reachable_time_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-RANDOM-REACHABLE-TIME-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_rnd_rtr_solicitation_delay_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-RND-RTR-SOLICITATION-DELAY-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_rtr_solicitation_interval: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-RTR-SOLICITATION-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_slaac_dad_number_of_transmissions: None | PositiveInteger = (
        field(
            default=None,
            metadata={
                "name": "TCP-IP-NDP-SLAAC-DAD-NUMBER-OF-TRANSMISSIONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    tcp_ip_ndp_slaac_dad_retransmission_delay: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-SLAAC-DAD-RETRANSMISSION-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_slaac_delay_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-SLAAC-DELAY-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ndp_slaac_optimistic_dad_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-NDP-SLAAC-OPTIMISTIC-DAD-ENABLED",
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
