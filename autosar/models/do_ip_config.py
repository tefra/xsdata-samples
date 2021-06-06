from dataclasses import dataclass, field
from typing import List, Optional
from .do_ip_interface import DoIpInterface
from .do_ip_logic_address import DoIpLogicAddress

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DoIpConfig:
    """
    This element defines the DoIp configuration for a specific Ecu.

    :ivar doip_interfaces: DoIP node consists of one or several
        DoIPInterfaces over which the ECU is able to communicate via
        DoIP independently. I.e. DoIP functionalities on each IP
        interface are isolated from each other.
    :ivar logic_address: Describes the logical address of the DoIP
        entity,  i.e. the Local Address that will route diagnostic
        requests to the Dcm of the DoIP entity.
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
        name = "DO-IP-CONFIG"

    doip_interfaces: Optional["DoIpConfig.DoipInterfaces"] = field(
        default=None,
        metadata={
            "name": "DOIP-INTERFACES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    logic_address: Optional[DoIpLogicAddress] = field(
        default=None,
        metadata={
            "name": "LOGIC-ADDRESS",
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
    class DoipInterfaces:
        do_ip_interface: List[DoIpInterface] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-INTERFACE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
