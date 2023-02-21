from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .coupling_port_details import CouplingPortDetails
from .coupling_port_role_enum import CouplingPortRoleEnum
from .ethernet_connection_negotiation_enum import EthernetConnectionNegotiationEnum
from .ethernet_mac_layer_type_enum import EthernetMacLayerTypeEnum
from .ethernet_physical_channel_subtypes_enum import EthernetPhysicalChannelSubtypesEnum
from .ethernet_physical_layer_type_enum import EthernetPhysicalLayerTypeEnum
from .ethernet_switch_vlan_ingress_tag_enum import EthernetSwitchVlanIngressTagEnum
from .ethernet_wakeup_sleep_on_dataline_config_subtypes_enum import EthernetWakeupSleepOnDatalineConfigSubtypesEnum
from .identifier import Identifier
from .mac_multicast_group_subtypes_enum import MacMulticastGroupSubtypesEnum
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .plca_props import PlcaProps
from .pnc_mapping_ident_subtypes_enum import PncMappingIdentSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .vlan_membership import VlanMembership

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CouplingPort:
    """A CouplingPort is used to connect a CouplingElement with an EcuInstance or
    two CouplingElements with each other via a CouplingPortConnection.

    Optionally, the CouplingPort may also have a reference to a
    macMulticastGroup and a defaultVLAN.

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
    :ivar connection_negotiation_behavior: Specifies the connection
        negotiation of the CouplingPort.
    :ivar coupling_port_details: Defines more details of a CouplingPort
        in case a more specific configuration is required.
    :ivar coupling_port_role: Defines the role this CouplingPort takes
        in the context of the CouplingElement.
    :ivar coupling_port_speed: CouplingPort speed in bits/s.
    :ivar default_vlan_ref: The vLanIdentifier of the referenced VLAN is
        the Default-PVID (port VLAN ID). A Port VLAN ID is a default
        VLAN ID that is assigned to an access CouplingPort to designate
        the VLAN segment to which this port is connected. Also, if a
        CouplingPort has not been configured with any VLAN memberships,
        the virtual switch's Port VLAN ID (pvid) becomes the default
        VLAN ID for the ports connection. This identifier/tag is added
        for incoming untagged messages at the port (ingress tagging).
        For outgoing messages with this identifier, the tag is removed
        at the port (egress untagging, depending on the
        VlanMembership.sendActivity).
    :ivar mac_layer_type: Specifies the mac layer type of the
        CouplingPort.
    :ivar mac_multicast_address_refs: Assigns a set of MAC-Multicast-
        Addresses which are addressable via this CouplingPort. This is a
        static pre-configuration and further addresses may be learned
        during runtime.
    :ivar physical_layer_type: Specifies the physical layer type of the
        CouplingPort.
    :ivar plca_props: Optional properties for configuration of PLCA
        (Physical Layer Collision Avoidance) in case 10-BASE-T1S
        Ethernet is used and PLCA is enabled on the CouplingPort (PHY).
    :ivar pnc_mapping_refs: Reference to the partial networks this
        CouplingPort participates in.
    :ivar receive_activity: Defines the handling of frames at the
        ingress port.
    :ivar vlan_memberships: Messages of VLANs that are defined here can
        be communicated via the CouplingPort.
    :ivar vlan_modifier_ref: All incoming messages at this CouplingPort
        shall be tagged with this VLAN Id. This tagging is performed
        regardless whether the message already has a VLAN tag or is
        untagged, an existing VLAN tag will be overwritten. This feature
        is XOR with CoupligPort.defaultVlan.
    :ivar wakeup_sleep_on_dataline_config_ref: Optional reference to
        EthernetWakeupSleepOnDatalineConfig.
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
        name = "COUPLING-PORT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["CouplingPort.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["CouplingPort.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    connection_negotiation_behavior: Optional[EthernetConnectionNegotiationEnum] = field(
        default=None,
        metadata={
            "name": "CONNECTION-NEGOTIATION-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    coupling_port_details: Optional[CouplingPortDetails] = field(
        default=None,
        metadata={
            "name": "COUPLING-PORT-DETAILS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    coupling_port_role: Optional[CouplingPortRoleEnum] = field(
        default=None,
        metadata={
            "name": "COUPLING-PORT-ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    coupling_port_speed: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "COUPLING-PORT-SPEED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    default_vlan_ref: Optional["CouplingPort.DefaultVlanRef"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-VLAN-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mac_layer_type: Optional[EthernetMacLayerTypeEnum] = field(
        default=None,
        metadata={
            "name": "MAC-LAYER-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mac_multicast_address_refs: Optional["CouplingPort.MacMulticastAddressRefs"] = field(
        default=None,
        metadata={
            "name": "MAC-MULTICAST-ADDRESS-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    physical_layer_type: Optional[EthernetPhysicalLayerTypeEnum] = field(
        default=None,
        metadata={
            "name": "PHYSICAL-LAYER-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    plca_props: Optional[PlcaProps] = field(
        default=None,
        metadata={
            "name": "PLCA-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pnc_mapping_refs: Optional["CouplingPort.PncMappingRefs"] = field(
        default=None,
        metadata={
            "name": "PNC-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    receive_activity: Optional[EthernetSwitchVlanIngressTagEnum] = field(
        default=None,
        metadata={
            "name": "RECEIVE-ACTIVITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    vlan_memberships: Optional["CouplingPort.VlanMemberships"] = field(
        default=None,
        metadata={
            "name": "VLAN-MEMBERSHIPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    vlan_modifier_ref: Optional["CouplingPort.VlanModifierRef"] = field(
        default=None,
        metadata={
            "name": "VLAN-MODIFIER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    wakeup_sleep_on_dataline_config_ref: Optional["CouplingPort.WakeupSleepOnDatalineConfigRef"] = field(
        default=None,
        metadata={
            "name": "WAKEUP-SLEEP-ON-DATALINE-CONFIG-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class DefaultVlanRef(Ref):
        dest: Optional[EthernetPhysicalChannelSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class MacMulticastAddressRefs:
        mac_multicast_address_ref: List["CouplingPort.MacMulticastAddressRefs.MacMulticastAddressRef"] = field(
            default_factory=list,
            metadata={
                "name": "MAC-MULTICAST-ADDRESS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class MacMulticastAddressRef(Ref):
            dest: Optional[MacMulticastGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class PncMappingRefs:
        pnc_mapping_ref: List["CouplingPort.PncMappingRefs.PncMappingRef"] = field(
            default_factory=list,
            metadata={
                "name": "PNC-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class PncMappingRef(Ref):
            dest: Optional[PncMappingIdentSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class VlanMemberships:
        vlan_membership: List[VlanMembership] = field(
            default_factory=list,
            metadata={
                "name": "VLAN-MEMBERSHIP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class VlanModifierRef(Ref):
        dest: Optional[EthernetPhysicalChannelSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class WakeupSleepOnDatalineConfigRef(Ref):
        dest: Optional[EthernetWakeupSleepOnDatalineConfigSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
