from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.network_endpoint_subtypes_enum import NetworkEndpointSubtypesEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref
from autosar.models.secure_com_props_subtypes_enum import SecureComPropsSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SomeipServiceDiscovery:
    """
    This meta-class represents a specialization of the generic service
    discovery for the SOME/IP case.

    :ivar multicast_sd_ip_address_ref: This reference identifies the
        multicast IP address used for service discovery.
    :ivar multicast_secure_com_props_ref: Reference to a communication
        security protocol and its configuration settings that will
        provide communication security for Service Discovery messages
        that are transmitted using multicast, e.g. FindService message.
    :ivar someip_service_discovery_port: This attribute represents the
        port number reserved for service discovery.
    :ivar unicast_secure_com_props_refs: Reference to a communication
        security protocol and its configuration settings that will
        provide communication security for Service Discovery messages
        that are transmitted using unicast, e.g. OfferService as answer
        to a FindService message. .
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
        name = "SOMEIP-SERVICE-DISCOVERY"

    multicast_sd_ip_address_ref: Optional["SomeipServiceDiscovery.MulticastSdIpAddressRef"] = field(
        default=None,
        metadata={
            "name": "MULTICAST-SD-IP-ADDRESS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    multicast_secure_com_props_ref: Optional["SomeipServiceDiscovery.MulticastSecureComPropsRef"] = field(
        default=None,
        metadata={
            "name": "MULTICAST-SECURE-COM-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    someip_service_discovery_port: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SOMEIP-SERVICE-DISCOVERY-PORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    unicast_secure_com_props_refs: Optional["SomeipServiceDiscovery.UnicastSecureComPropsRefs"] = field(
        default=None,
        metadata={
            "name": "UNICAST-SECURE-COM-PROPS-REFS",
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
    class MulticastSdIpAddressRef(Ref):
        dest: Optional[NetworkEndpointSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class MulticastSecureComPropsRef(Ref):
        dest: Optional[SecureComPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class UnicastSecureComPropsRefs:
        unicast_secure_com_props_ref: List["SomeipServiceDiscovery.UnicastSecureComPropsRefs.UnicastSecureComPropsRef"] = field(
            default_factory=list,
            metadata={
                "name": "UNICAST-SECURE-COM-PROPS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class UnicastSecureComPropsRef(Ref):
            dest: Optional[SecureComPropsSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
