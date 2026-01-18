from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .can_nm_ecu import CanNmEcu
from .category_string import CategoryString
from .ecu_instance_subtypes_enum import EcuInstanceSubtypesEnum
from .flexray_nm_ecu import FlexrayNmEcu
from .identifier import Identifier
from .j_1939_nm_ecu import J1939NmEcu
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nm_coordinator import NmCoordinator
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue
from .udp_nm_ecu import UdpNmEcu

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class NmEcu:
    """
    ECU on which NM is running.

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
    :ivar bus_dependent_nm_ecus: Cluster specific NmEcu attributes
    :ivar bus_specific_nm_ecu: Busspecific NmEcu attributes. Please note
        that this aggregation is deprecated and is replaced by the
        busDependentNmEcu aggregation.
    :ivar ecu_instance_ref: Association to an ECUInstance in the
        topology description.
    :ivar nm_bus_synchronization_enabled: Enables bus synchronization
        support.
    :ivar nm_com_control_enabled: Enables the Communication Control
        support.
    :ivar nm_coordinator: Nm ECU may coordinate different clusters.
    :ivar nm_cycletime_main_function: The period between successive
        calls to the Main Function of the NM Interface in seconds.
    :ivar nm_multiple_channels_enabled: Enables channel multiplicity
        support.
    :ivar nm_node_detection_enabled: Enables the Request Repeat Message
        Request support. Only valid if nmNodeIdEnabled is set to true.
        Please note that this attribute is deprecated and will be
        removed in future. It is replaced by the channel specific
        attribute located in NmCluster.
    :ivar nm_node_id_enabled: Enables the source node identifier. Please
        note that this attribute is deprecated and will be removed in
        future. It is replaced by the channel specific attribute located
        in NmCluster.
    :ivar nm_passive_mode_enabled: This attribute enables the support of
        the Passive Mode.
    :ivar nm_pdu_rx_indication_enabled: Switch for enabling the PDU Rx
        Indication.
    :ivar nm_remote_sleep_ind_enabled: Switch for enabling remote sleep
        indication support.
    :ivar nm_repeat_msg_ind_enabled: Switch for enabling the Repeat
        Message Bit Indication. Please note that this attribute is
        deprecated and will be removed in future. It is replaced by the
        channel specific attribute located in NmCluster.
    :ivar nm_state_change_ind_enabled: Enables the CAN Network
        Management state change notification.
    :ivar nm_user_data_enabled: Switch for enabling user data support.
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
        name = "NM-ECU"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | NmEcu.ShortNameFragments = field(
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
    annotations: None | NmEcu.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bus_dependent_nm_ecus: None | NmEcu.BusDependentNmEcus = field(
        default=None,
        metadata={
            "name": "BUS-DEPENDENT-NM-ECUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bus_specific_nm_ecu: None | NmEcu.BusSpecificNmEcu = field(
        default=None,
        metadata={
            "name": "BUS-SPECIFIC-NM-ECU",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_instance_ref: None | NmEcu.EcuInstanceRef = field(
        default=None,
        metadata={
            "name": "ECU-INSTANCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_bus_synchronization_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-BUS-SYNCHRONIZATION-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_com_control_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-COM-CONTROL-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_coordinator: None | NmCoordinator = field(
        default=None,
        metadata={
            "name": "NM-COORDINATOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_cycletime_main_function: None | TimeValue = field(
        default=None,
        metadata={
            "name": "NM-CYCLETIME-MAIN-FUNCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_multiple_channels_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-MULTIPLE-CHANNELS-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_node_detection_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-NODE-DETECTION-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_node_id_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-NODE-ID-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_passive_mode_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-PASSIVE-MODE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_pdu_rx_indication_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-PDU-RX-INDICATION-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_remote_sleep_ind_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-REMOTE-SLEEP-IND-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_repeat_msg_ind_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-REPEAT-MSG-IND-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_state_change_ind_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-STATE-CHANGE-IND-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_user_data_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-USER-DATA-ENABLED",
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
    class BusDependentNmEcus:
        can_nm_ecu: list[CanNmEcu] = field(
            default_factory=list,
            metadata={
                "name": "CAN-NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_nm_ecu: list[FlexrayNmEcu] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_nm_ecu: list[J1939NmEcu] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        udp_nm_ecu: list[UdpNmEcu] = field(
            default_factory=list,
            metadata={
                "name": "UDP-NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class BusSpecificNmEcu:
        can_nm_ecu: None | CanNmEcu = field(
            default=None,
            metadata={
                "name": "CAN-NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_nm_ecu: None | FlexrayNmEcu = field(
            default=None,
            metadata={
                "name": "FLEXRAY-NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_nm_ecu: None | J1939NmEcu = field(
            default=None,
            metadata={
                "name": "J-1939-NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        udp_nm_ecu: None | UdpNmEcu = field(
            default=None,
            metadata={
                "name": "UDP-NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class EcuInstanceRef(Ref):
        dest: EcuInstanceSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
