from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .boolean import Boolean
from .coupling_port import CouplingPort
from .ethernet_mac_layer_type_enum import EthernetMacLayerTypeEnum
from .integer import Integer
from .mac_address_string import MacAddressString
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class EthernetCommunicationControllerConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar wake_up_by_controller_supported: Defines whether the ECU shall
        be woken up by this CommunicationController. TRUE: wake up is
        possible FALSE: wake up is not supported Note: If
        wakeUpByControllerSupported is set to TRUE the feature shall be
        supported by both hardware and basic software.
    :ivar coupling_ports: Optional CouplingPort that can be used to
        connect the ECU to a CouplingElement (e.g. a switch).
    :ivar mac_layer_type: Specifies the mac layer type of the ethernet
        controller.
    :ivar mac_unicast_address: Media Access Control address (MAC
        address) that uniquely identifies each
        EthernetCommunicationController in the network.
    :ivar maximum_receive_buffer_length: Determines the maximum receive
        buffer length (frame length) in bytes.
    :ivar maximum_transmission_unit: This attribute is deprecated and
        will be removed in future. It is replaced by
        EthernetCommunicationConnector.maximumTransmissionUnit. Old
        description: This attribute specifies the maximum transmission
        unit in bytes.
    :ivar maximum_transmit_buffer_length: Determines the maximum
        transmit buffer length (frame length) in bytes.
    :ivar slave_act_as_passive_communication_slave: This attribute
        specifies if the EcuInstance is acting as a passive
        communication slave on the connected PhysicalChannel. This is
        used for EthernetCommunicationControllers that use Ethernet
        hardware which supports wake-up and sleep on the network (e.g.
        Open Alliance TC10 compliant Ethernet hardware).
    :ivar slave_qualified_unexpected_link_down_time: This attribute
        specifies time when an unexpected link down is evaluated as link
        down and indicated to the AUTOSAR communication stack.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL"

    wake_up_by_controller_supported: None | Boolean = field(
        default=None,
        metadata={
            "name": "WAKE-UP-BY-CONTROLLER-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    coupling_ports: (
        None | EthernetCommunicationControllerConditional.CouplingPorts
    ) = field(
        default=None,
        metadata={
            "name": "COUPLING-PORTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mac_layer_type: None | EthernetMacLayerTypeEnum = field(
        default=None,
        metadata={
            "name": "MAC-LAYER-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mac_unicast_address: None | MacAddressString = field(
        default=None,
        metadata={
            "name": "MAC-UNICAST-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    maximum_receive_buffer_length: None | Integer = field(
        default=None,
        metadata={
            "name": "MAXIMUM-RECEIVE-BUFFER-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    maximum_transmission_unit: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAXIMUM-TRANSMISSION-UNIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    maximum_transmit_buffer_length: None | Integer = field(
        default=None,
        metadata={
            "name": "MAXIMUM-TRANSMIT-BUFFER-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    slave_act_as_passive_communication_slave: None | Boolean = field(
        default=None,
        metadata={
            "name": "SLAVE-ACT-AS-PASSIVE-COMMUNICATION-SLAVE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    slave_qualified_unexpected_link_down_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "SLAVE-QUALIFIED-UNEXPECTED-LINK-DOWN-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class CouplingPorts:
        coupling_port: list[CouplingPort] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-PORT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
