from dataclasses import dataclass, field
from typing import Optional
from .ethernet_physical_channel_subtypes_enum import EthernetPhysicalChannelSubtypesEnum
from .ip_transport_protocol_enum import IpTransportProtocolEnum
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IpIamAuthenticConnectionProps:
    """
    This meta-class defines a set of properties for IP connections in the
    context of IAM configuration.

    :ivar ip_protocol: This attribute defines the relevant IP protocol.
    :ivar local_network_endpoint_ref: This reference defines an
        authentic local NetworkEndpoint in terms of IAM configuration.
    :ivar local_port_range_end: This attribute restricts the traffic
        monitoring and defines an end value for the local port range.
    :ivar local_port_range_start: This attribute restricts the traffic
        monitoring and defines a start value for the local port range.
    :ivar remote_network_endpoint_ref: This reference defines an
        authentic remote NetworkEndpoint in terms of IAM configuration.
    :ivar remote_port_range_end: This attribute restricts the traffic
        monitoring and defines an end value for the remote port range.
    :ivar remote_port_range_start: This attribute restricts the traffic
        monitoring and defines a start value for the remote port range.
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
        name = "IP-IAM-AUTHENTIC-CONNECTION-PROPS"

    ip_protocol: Optional[IpTransportProtocolEnum] = field(
        default=None,
        metadata={
            "name": "IP-PROTOCOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    local_network_endpoint_ref: Optional["IpIamAuthenticConnectionProps.LocalNetworkEndpointRef"] = field(
        default=None,
        metadata={
            "name": "LOCAL-NETWORK-ENDPOINT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    local_port_range_end: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOCAL-PORT-RANGE-END",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    local_port_range_start: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOCAL-PORT-RANGE-START",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    remote_network_endpoint_ref: Optional["IpIamAuthenticConnectionProps.RemoteNetworkEndpointRef"] = field(
        default=None,
        metadata={
            "name": "REMOTE-NETWORK-ENDPOINT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    remote_port_range_end: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "REMOTE-PORT-RANGE-END",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    remote_port_range_start: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "REMOTE-PORT-RANGE-START",
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

    @dataclass
    class LocalNetworkEndpointRef(Ref):
        dest: Optional[EthernetPhysicalChannelSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class RemoteNetworkEndpointRef(Ref):
        dest: Optional[EthernetPhysicalChannelSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
