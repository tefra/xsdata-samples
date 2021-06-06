from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import VariationPoint
from .eth_global_time_managed_coupling_port import EthGlobalTimeManagedCouplingPort
from .eth_global_time_message_format_enum import EthGlobalTimeMessageFormatEnum
from .eth_t_syn_crc_flags import EthTSynCrcFlags
from .mac_address_string import MacAddressString
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EthGlobalTimeDomainProps:
    """
    Enables the definition of Ethernet Global Time specific properties.

    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar crc_flags: Defines the fields of the message which shall be
        taken into account for CRC calculation and verification.
    :ivar destination_physical_address: Defines the MAC multicast
        address the Ethernet time sync messages are communicated on.
    :ivar fup_data_id_lists:
    :ivar managed_coupling_ports: Collection of CouplingPorts which are
        managed in the scope of this Ethernet GlobalTimeDomain.
    :ivar message_compliance: Defines the compliance of the Ethernet
        time sync messages to specific standards.
    :ivar vlan_priority: Defines which VLAN priority shall be assigned
        to a time sync message in case the message is sent using a VLAN
        tag.
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
        name = "ETH-GLOBAL-TIME-DOMAIN-PROPS"

    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    crc_flags: Optional[EthTSynCrcFlags] = field(
        default=None,
        metadata={
            "name": "CRC-FLAGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    destination_physical_address: Optional[MacAddressString] = field(
        default=None,
        metadata={
            "name": "DESTINATION-PHYSICAL-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    fup_data_id_lists: Optional["EthGlobalTimeDomainProps.FupDataIdLists"] = field(
        default=None,
        metadata={
            "name": "FUP-DATA-ID-LISTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    managed_coupling_ports: Optional["EthGlobalTimeDomainProps.ManagedCouplingPorts"] = field(
        default=None,
        metadata={
            "name": "MANAGED-COUPLING-PORTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    message_compliance: Optional[EthGlobalTimeMessageFormatEnum] = field(
        default=None,
        metadata={
            "name": "MESSAGE-COMPLIANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    vlan_priority: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "VLAN-PRIORITY",
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
    class FupDataIdLists:
        """
        :ivar fup_data_id_list: The DataIDList for FUP messages to
            calculate CRC.
        """
        fup_data_id_list: List[PositiveInteger] = field(
            default_factory=list,
            metadata={
                "name": "FUP-DATA-ID-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 16,
            }
        )

    @dataclass
    class ManagedCouplingPorts:
        eth_global_time_managed_coupling_port: List[EthGlobalTimeManagedCouplingPort] = field(
            default_factory=list,
            metadata={
                "name": "ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
