from dataclasses import dataclass, field
from typing import List, Optional
from .access_control_enum import AccessControlEnum
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .can_communication_connector import CanCommunicationConnector
from .category_string import CategoryString
from .eth_ip_props_subtypes_enum import EthIpPropsSubtypesEnum
from .eth_tcp_ip_icmp_props_subtypes_enum import EthTcpIpIcmpPropsSubtypesEnum
from .eth_tcp_ip_props_subtypes_enum import EthTcpIpPropsSubtypesEnum
from .ethernet_communication_connector import EthernetCommunicationConnector
from .flexray_communication_connector import FlexrayCommunicationConnector
from .identifier import Identifier
from .lin_communication_connector import LinCommunicationConnector
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .someip_service_discovery import SomeipServiceDiscovery
from .time_value import TimeValue
from .ttcan_communication_connector import TtcanCommunicationConnector
from .user_defined_communication_connector import (
    UserDefinedCommunicationConnector,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MachineDesign:
    """
    This meta-class represents the ability to define requirements on a Machine in
    the context of designing a system.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar access_control: This attribute defines how the access
        restriction to the Service Instance is defined.
    :ivar communication_connectors: This aggregation defines the network
        connection of the machine.
    :ivar eth_ip_props_ref: Maschine specific IP attributes.
    :ivar pn_reset_timer: Specifies the runtime of the reset timer in
        seconds. This reset time is valid for the reset of PN requests.
    :ivar pnc_prepare_sleep_timer: Time in seconds the PNC state machine
        shall wait in PNC_PREPARE_SLEEP.
    :ivar service_discover_configs: Set of service discovery
        configuration settings that are defined on the machine for
        individual CommunicationConnectors.
    :ivar tcp_ip_icmp_props_ref: Machine specific ICMP (Internet Control
        Message Protocol) attributes
    :ivar tcp_ip_props_ref: Machine specific TcpIp Stack attributes.
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "MACHINE-DESIGN"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["MachineDesign.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["MachineDesign.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    access_control: Optional[AccessControlEnum] = field(
        default=None,
        metadata={
            "name": "ACCESS-CONTROL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    communication_connectors: Optional[
        "MachineDesign.CommunicationConnectors"
    ] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CONNECTORS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    eth_ip_props_ref: Optional["MachineDesign.EthIpPropsRef"] = field(
        default=None,
        metadata={
            "name": "ETH-IP-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pn_reset_timer: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PN-RESET-TIMER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_prepare_sleep_timer: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PNC-PREPARE-SLEEP-TIMER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_discover_configs: Optional[
        "MachineDesign.ServiceDiscoverConfigs"
    ] = field(
        default=None,
        metadata={
            "name": "SERVICE-DISCOVER-CONFIGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_icmp_props_ref: Optional["MachineDesign.TcpIpIcmpPropsRef"] = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_props_ref: Optional["MachineDesign.TcpIpPropsRef"] = field(
        default=None,
        metadata={
            "name": "TCP-IP-PROPS-REF",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CommunicationConnectors:
        can_communication_connector: List[CanCommunicationConnector] = field(
            default_factory=list,
            metadata={
                "name": "CAN-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_communication_connector: List[
            EthernetCommunicationConnector
        ] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_communication_connector: List[
            FlexrayCommunicationConnector
        ] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_communication_connector: List[LinCommunicationConnector] = field(
            default_factory=list,
            metadata={
                "name": "LIN-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ttcan_communication_connector: List[
            TtcanCommunicationConnector
        ] = field(
            default_factory=list,
            metadata={
                "name": "TTCAN-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_communication_connector: List[
            UserDefinedCommunicationConnector
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EthIpPropsRef(Ref):
        dest: Optional[EthIpPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ServiceDiscoverConfigs:
        someip_service_discovery: List[SomeipServiceDiscovery] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SERVICE-DISCOVERY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TcpIpIcmpPropsRef(Ref):
        dest: Optional[EthTcpIpIcmpPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TcpIpPropsRef(Ref):
        dest: Optional[EthTcpIpPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
