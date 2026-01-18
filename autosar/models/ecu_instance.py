from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .can_communication_connector import CanCommunicationConnector
from .can_communication_controller import CanCommunicationController
from .can_tp_address_subtypes_enum import CanTpAddressSubtypesEnum
from .category_string import CategoryString
from .client_id_range import ClientIdRange
from .consumed_provided_service_instance_group_ref_conditional import (
    ConsumedProvidedServiceInstanceGroupRefConditional,
)
from .diagnostic_ecu_props import DiagnosticEcuProps
from .dlt_config import DltConfig
from .do_ip_config import DoIpConfig
from .ecu_instance_props import EcuInstanceProps
from .ecu_partition import EcuPartition
from .eth_tcp_ip_icmp_props_subtypes_enum import EthTcpIpIcmpPropsSubtypesEnum
from .eth_tcp_ip_props_subtypes_enum import EthTcpIpPropsSubtypesEnum
from .ethernet_communication_connector import EthernetCommunicationConnector
from .ethernet_communication_controller import EthernetCommunicationController
from .flexray_communication_connector import FlexrayCommunicationConnector
from .flexray_communication_controller import FlexrayCommunicationController
from .i_signal_i_pdu_group_subtypes_enum import ISignalIPduGroupSubtypesEnum
from .identifier import Identifier
from .integer import Integer
from .lin_communication_connector import LinCommunicationConnector
from .lin_master import LinMaster
from .lin_slave import LinSlave
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdur_i_pdu_group_subtypes_enum import PdurIPduGroupSubtypesEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue
from .tp_address_subtypes_enum import TpAddressSubtypesEnum
from .ttcan_communication_connector import TtcanCommunicationConnector
from .ttcan_communication_controller import TtcanCommunicationController
from .user_defined_communication_connector import (
    UserDefinedCommunicationConnector,
)
from .user_defined_communication_controller import (
    UserDefinedCommunicationController,
)
from .v_2_x_support_enum import V2XSupportEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class EcuInstance:
    """
    ECUInstances are used to define the ECUs used in the topology.

    The type of the ECU is defined by a reference to an ECU specified with
    the ECU resource description.

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
    :ivar associated_com_i_pdu_group_refs: With this reference it is
        possible to identify which ISignalIPduGroups are applicable for
        which CommunicationConnector/ ECU. Only top level
        ISignalIPduGroups shall be referenced by an EcuInstance. If an
        ISignalIPduGroup contains other ISignalIPduGroups than these
        contained ISignalIPduGroups shall not be referenced by the
        EcuInstance. Contained ISignalIPduGroups are associated to an
        EcuInstance via the top level ISignalIPduGroup.
    :ivar associated_consumed_provided_service_instance_groups: With
        this reference it is possible to identify which
        ConsumedProvidedServiceInstanceGroups are applicable for which
        ECUInstance. This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar associated_pdur_i_pdu_group_refs: With this reference it is
        possible to identify which PduR IPdu Groups are applicable for
        which CommunicationConnector/ ECU.
    :ivar can_tp_address_refs: Please note that this reference is
        deprecated and will be removed in future. A Tp Address can be
        assigned to an ECU without an existing TP Configuration. If
        TpNodes are described this reference shall not be used.
    :ivar client_id_range: Restriction of the Client Identifier for this
        Ecu to an allowed range of numerical values. The Client
        Identifier of the transaction handle is generated by the client
        RTE for inter-Ecu Client/Server communication.
    :ivar com_configuration_gw_time_base: The period between successive
        calls to Com_MainFunctionRouteSignals of the AUTOSAR COM module
        in seconds.
    :ivar com_configuration_rx_time_base: The period between successive
        calls to Com_MainFunctionRx of the AUTOSAR COM module in
        seconds.
    :ivar com_configuration_tx_time_base: The period between successive
        calls to Com_MainFunctionTx of the AUTOSAR COM module in
        seconds.
    :ivar com_enable_mdt_for_cyclic_transmission: Enables for the Com
        module of this EcuInstance the minimum delay time monitoring for
        cyclic and repeated transmissions (TransmissionModeTiming has
        cyclicTiming assigned or eventControlledTiming with
        numberOfRepetitions &gt; 0).
    :ivar comm_controllers: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar connectors: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar diagnostic_address: An ECU specific ID for responses of
        diagnostic routines.
    :ivar diagnostic_props: This represents the diagnostic-related
        properties of an entire ECU.
    :ivar dlt_config: Describes the Dlt configuration on this
        EcuInstance.
    :ivar do_ip_config: DoIp configuration on this EcuInstance.
    :ivar ecu_instance_propss: Additional properties of the EcuInstance
        that may vary in different Variants of the Ecu. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar eth_switch_port_group_derivation: Defines whether the
        derivation of SwitchPortGroups based on VLAN and/or
        CouplingPort.pncMapping shall be performed for this EcuInstance.
        If not defined the derivation shall not be done.
    :ivar partitions: Optional definition of Partitions within an Ecu.
    :ivar pn_reset_time: Specifies the runtime of the reset timer in
        seconds. This reset time is valid for the reset of PN requests
        in the EIRA and in the ERA.
    :ivar pnc_prepare_sleep_timer: Time in seconds the PNC state machine
        shall wait in PNC_PREPARE_SLEEP.
    :ivar pnc_synchronous_wakeup: If this parameter is available and set
        to true then all available PNCs will be woken up as soon as a
        channel wakeup occurs. This is ensured by adding all PNCs to all
        channel wakeup sources during upstream mapping.
    :ivar sleep_mode_supported: Specifies whether the ECU instance may
        be put to a "low power mode" * true: sleep mode is supported *
        false: sleep mode is not supported Note: This flag may only be
        set to "true" if the feature is supported by both hardware and
        basic software.
    :ivar tcp_ip_icmp_props_ref: EcuInstance specific ICMP (Internet
        Control Message Protocol) attributes
    :ivar tcp_ip_props_ref: EcuInstance specific TcpIp Stack attributes.
    :ivar tp_address_refs: Please note that this reference is deprecated
        and will be removed in future. A Tp Address can be assigned to
        an ECU without an existing TP Configuration. If TpNodes are
        described this reference shall not be used.
    :ivar v_2_x_supported: This attribute is used to control the
        existence of the V2X stack on the given EcuInstance.
    :ivar wake_up_over_bus_supported: Driver support for wakeup over
        Bus.
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
        name = "ECU-INSTANCE"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | EcuInstance.ShortNameFragments = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: None | EcuInstance.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    associated_com_i_pdu_group_refs: (
        None | EcuInstance.AssociatedComIPduGroupRefs
    ) = field(
        default=None,
        metadata={
            "name": "ASSOCIATED-COM-I-PDU-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    associated_consumed_provided_service_instance_groups: (
        None | EcuInstance.AssociatedConsumedProvidedServiceInstanceGroups
    ) = field(
        default=None,
        metadata={
            "name": "ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    associated_pdur_i_pdu_group_refs: (
        None | EcuInstance.AssociatedPdurIPduGroupRefs
    ) = field(
        default=None,
        metadata={
            "name": "ASSOCIATED-PDUR-I-PDU-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_tp_address_refs: None | EcuInstance.CanTpAddressRefs = field(
        default=None,
        metadata={
            "name": "CAN-TP-ADDRESS-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_id_range: None | ClientIdRange = field(
        default=None,
        metadata={
            "name": "CLIENT-ID-RANGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    com_configuration_gw_time_base: None | TimeValue = field(
        default=None,
        metadata={
            "name": "COM-CONFIGURATION-GW-TIME-BASE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    com_configuration_rx_time_base: None | TimeValue = field(
        default=None,
        metadata={
            "name": "COM-CONFIGURATION-RX-TIME-BASE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    com_configuration_tx_time_base: None | TimeValue = field(
        default=None,
        metadata={
            "name": "COM-CONFIGURATION-TX-TIME-BASE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    com_enable_mdt_for_cyclic_transmission: None | Boolean = field(
        default=None,
        metadata={
            "name": "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    comm_controllers: None | EcuInstance.CommControllers = field(
        default=None,
        metadata={
            "name": "COMM-CONTROLLERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    connectors: None | EcuInstance.Connectors = field(
        default=None,
        metadata={
            "name": "CONNECTORS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    diagnostic_address: None | Integer = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    diagnostic_props: None | DiagnosticEcuProps = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dlt_config: None | DltConfig = field(
        default=None,
        metadata={
            "name": "DLT-CONFIG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    do_ip_config: None | DoIpConfig = field(
        default=None,
        metadata={
            "name": "DO-IP-CONFIG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_instance_propss: None | EcuInstance.EcuInstancePropss = field(
        default=None,
        metadata={
            "name": "ECU-INSTANCE-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    eth_switch_port_group_derivation: None | Boolean = field(
        default=None,
        metadata={
            "name": "ETH-SWITCH-PORT-GROUP-DERIVATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    partitions: None | EcuInstance.Partitions = field(
        default=None,
        metadata={
            "name": "PARTITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pn_reset_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "PN-RESET-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_prepare_sleep_timer: None | TimeValue = field(
        default=None,
        metadata={
            "name": "PNC-PREPARE-SLEEP-TIMER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_synchronous_wakeup: None | Boolean = field(
        default=None,
        metadata={
            "name": "PNC-SYNCHRONOUS-WAKEUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sleep_mode_supported: None | Boolean = field(
        default=None,
        metadata={
            "name": "SLEEP-MODE-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_icmp_props_ref: None | EcuInstance.TcpIpIcmpPropsRef = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_props_ref: None | EcuInstance.TcpIpPropsRef = field(
        default=None,
        metadata={
            "name": "TCP-IP-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tp_address_refs: None | EcuInstance.TpAddressRefs = field(
        default=None,
        metadata={
            "name": "TP-ADDRESS-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    v_2_x_supported: None | V2XSupportEnum = field(
        default=None,
        metadata={
            "name": "V-2-X-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wake_up_over_bus_supported: None | Boolean = field(
        default=None,
        metadata={
            "name": "WAKE-UP-OVER-BUS-SUPPORTED",
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
    uuid: None | str = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class AssociatedComIPduGroupRefs:
        associated_com_i_pdu_group_ref: list[
            EcuInstance.AssociatedComIPduGroupRefs.AssociatedComIPduGroupRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "ASSOCIATED-COM-I-PDU-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class AssociatedComIPduGroupRef(Ref):
            dest: ISignalIPduGroupSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class AssociatedConsumedProvidedServiceInstanceGroups:
        consumed_provided_service_instance_group_ref_conditional: list[
            ConsumedProvidedServiceInstanceGroupRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class AssociatedPdurIPduGroupRefs:
        associated_pdur_i_pdu_group_ref: list[
            EcuInstance.AssociatedPdurIPduGroupRefs.AssociatedPdurIPduGroupRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "ASSOCIATED-PDUR-I-PDU-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class AssociatedPdurIPduGroupRef(Ref):
            dest: PdurIPduGroupSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class CanTpAddressRefs:
        can_tp_address_ref: list[
            EcuInstance.CanTpAddressRefs.CanTpAddressRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "CAN-TP-ADDRESS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class CanTpAddressRef(Ref):
            dest: CanTpAddressSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class CommControllers:
        can_communication_controller: list[CanCommunicationController] = field(
            default_factory=list,
            metadata={
                "name": "CAN-COMMUNICATION-CONTROLLER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_communication_controller: list[
            EthernetCommunicationController
        ] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-COMMUNICATION-CONTROLLER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_communication_controller: list[
            FlexrayCommunicationController
        ] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-COMMUNICATION-CONTROLLER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_master: list[LinMaster] = field(
            default_factory=list,
            metadata={
                "name": "LIN-MASTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_slave: list[LinSlave] = field(
            default_factory=list,
            metadata={
                "name": "LIN-SLAVE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ttcan_communication_controller: list[TtcanCommunicationController] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TTCAN-COMMUNICATION-CONTROLLER",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        user_defined_communication_controller: list[
            UserDefinedCommunicationController
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-COMMUNICATION-CONTROLLER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Connectors:
        can_communication_connector: list[CanCommunicationConnector] = field(
            default_factory=list,
            metadata={
                "name": "CAN-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_communication_connector: list[
            EthernetCommunicationConnector
        ] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_communication_connector: list[
            FlexrayCommunicationConnector
        ] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_communication_connector: list[LinCommunicationConnector] = field(
            default_factory=list,
            metadata={
                "name": "LIN-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ttcan_communication_connector: list[TtcanCommunicationConnector] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TTCAN-COMMUNICATION-CONNECTOR",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        user_defined_communication_connector: list[
            UserDefinedCommunicationConnector
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-COMMUNICATION-CONNECTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class EcuInstancePropss:
        ecu_instance_props: list[EcuInstanceProps] = field(
            default_factory=list,
            metadata={
                "name": "ECU-INSTANCE-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Partitions:
        ecu_partition: list[EcuPartition] = field(
            default_factory=list,
            metadata={
                "name": "ECU-PARTITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class TcpIpIcmpPropsRef(Ref):
        dest: EthTcpIpIcmpPropsSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TcpIpPropsRef(Ref):
        dest: EthTcpIpPropsSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TpAddressRefs:
        tp_address_ref: list[EcuInstance.TpAddressRefs.TpAddressRef] = field(
            default_factory=list,
            metadata={
                "name": "TP-ADDRESS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class TpAddressRef(Ref):
            dest: TpAddressSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
