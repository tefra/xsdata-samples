from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .platform_module_ethernet_endpoint_configuration_subtypes_enum import (
    PlatformModuleEthernetEndpointConfigurationSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DoIpNetworkConfiguration:
    """
    This element collects DoIP properties that are network interface
    specific.

    :ivar eid_use_mac: This attribute defines whther the MAC of the
        network interface is used as eid. True: MAC is used False: eid
        needs to be configured manually by DoIpInstantiation.eid.
    :ivar is_activation_line_dependent: This attribute defines whether
        the network interface * is started "on-demand" when an
        activation line is sensed or * is always available.
    :ivar max_initial_vehicle_announcement_time: Upper bound for the
        time to wait in [s] for sending first vehicle anouncement
        message after IP address assignment. Represents parameter
        A_DoIP_Announce_Wait of ISO 13400-2:2012. The value of this
        timing shall be determined randomly in the closed interval
        [0..maxInitialVehicleAnnouncementTime].
    :ivar max_tester_connections: Maximum amount of tester connections
        that shall be maintained at one time before alive check is
        performed.
    :ivar network_configuration_ref: Network configuration (Protocol,
        Port, IP Address) for transmission of DoIP messages on a
        specific VLAN.
    :ivar network_interface_id: This attribute defines the identifier
        for the DoIPInterface.
    :ivar tcp_alive_check_response_timeout: Timeout in [s] for waiting
        for a response to an Alive Check request before the connection
        is considered to be disconnected. Represents parameter
        T_TCP_AliveCheck of ISO 13400-2:2012.
    :ivar tcp_general_inactivity_time: Timeout in [s] for maximum
        inactivity of a TCP socket connection before the DoIP module
        will close the according socket connection. Represents parameter
        T_TCP_General_Inactivity of ISO 13400-2:2012.
    :ivar tcp_initial_inactivity_time: Timeout in [s] used for initial
        inactivity of a connected TCP socket connection directly after
        socket connection. Represents parameter T_TCP_Initial_Inactivity
        of ISO 13400-2:2012.
    :ivar vehicle_announcement_count: Number of vehicle announcement
        messages on IP address assignment. Represents parameter
        A_DoIP_Announce_Num of ISO 13400-2:2012.
    :ivar vehicle_announcement_interval: Time to wait in [s] for sending
        subsequent vehicle anouncement messages. Represents parameter
        A_DoIP_Announce_Interval of ISO 13400-2:2012.
    :ivar vehicle_identification_sync_status: Defines if the optional
        VIN/GID synchronization status is used additionally in the
        vehicle identification/announcement.
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
        name = "DO-IP-NETWORK-CONFIGURATION"

    eid_use_mac: None | Boolean = field(
        default=None,
        metadata={
            "name": "EID-USE-MAC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_activation_line_dependent: None | Boolean = field(
        default=None,
        metadata={
            "name": "IS-ACTIVATION-LINE-DEPENDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_initial_vehicle_announcement_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "MAX-INITIAL-VEHICLE-ANNOUNCEMENT-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_tester_connections: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-TESTER-CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_configuration_ref: (
        None | DoIpNetworkConfiguration.NetworkConfigurationRef
    ) = field(
        default=None,
        metadata={
            "name": "NETWORK-CONFIGURATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_interface_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "NETWORK-INTERFACE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_alive_check_response_timeout: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TCP-ALIVE-CHECK-RESPONSE-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_general_inactivity_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TCP-GENERAL-INACTIVITY-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_initial_inactivity_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TCP-INITIAL-INACTIVITY-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vehicle_announcement_count: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "VEHICLE-ANNOUNCEMENT-COUNT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vehicle_announcement_interval: None | TimeValue = field(
        default=None,
        metadata={
            "name": "VEHICLE-ANNOUNCEMENT-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vehicle_identification_sync_status: None | Boolean = field(
        default=None,
        metadata={
            "name": "VEHICLE-IDENTIFICATION-SYNC-STATUS",
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

    @dataclass
    class NetworkConfigurationRef(Ref):
        dest: (
            None | PlatformModuleEthernetEndpointConfigurationSubtypesEnum
        ) = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
