from __future__ import annotations

from dataclasses import dataclass, field

from .dhcp_server_configuration import DhcpServerConfiguration
from .ethernet_physical_channel_subtypes_enum import (
    EthernetPhysicalChannelSubtypesEnum,
)
from .ethernet_switch_vlan_egress_tagging_enum import (
    EthernetSwitchVlanEgressTaggingEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class VlanMembership:
    """
    Static logical channel or VLAN binding to a switch-port.

    The reference to an EthernetPhysicalChannel without a VLAN defined
    represents the handling of untagged frames.

    :ivar default_priority: Standard output-priority outgoing Frames
        will be tagged with. Defines the priority that received frames
        are assigned together with the VLAN Id (defaultVlan). The values
        from 0 (best effort) to 7 (highest) are allowed. In case
        modifyVlan and an already tagged received frame, the actual
        priority of the received frame is not modified.
    :ivar dhcp_address_assignment: Specifies the IP Address which will
        be assigned to a DHCP Client at this SwitchPort. If no
        dhcpAddressAssignment is provided all DHCP-Discover messages
        received at this Port will be discarded by the DHCP Server.
    :ivar send_activity: Attribute denotes whether a VLAN tagged
        ethernet frame will be # sent with its VLAN tag (sentTagged) #
        sent without a VLAN tag (sentUntagged) # will be dropped at this
        port (notSent or VLAN  not member of this list)
    :ivar vlan_ref: References a channel that represents a VLAN or an
        untagged channel.
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
        name = "VLAN-MEMBERSHIP"

    default_priority: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "DEFAULT-PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dhcp_address_assignment: None | DhcpServerConfiguration = field(
        default=None,
        metadata={
            "name": "DHCP-ADDRESS-ASSIGNMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    send_activity: None | EthernetSwitchVlanEgressTaggingEnum = field(
        default=None,
        metadata={
            "name": "SEND-ACTIVITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vlan_ref: None | VlanMembership.VlanRef = field(
        default=None,
        metadata={
            "name": "VLAN-REF",
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
    class VlanRef(Ref):
        dest: EthernetPhysicalChannelSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
