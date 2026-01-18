from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .boolean import Boolean
from .category_string import CategoryString
from .do_ip_routing_activation import DoIpRoutingActivation
from .do_ip_tp_config_subtypes_enum import DoIpTpConfigSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .socket_connection_bundle_subtypes_enum import (
    SocketConnectionBundleSubtypesEnum,
)
from .static_socket_connection_subtypes_enum import (
    StaticSocketConnectionSubtypesEnum,
)
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DoIpInterface:
    """
    A logical interface over which the DoIP Node is able to communicate via
    DoIP independently from other existing DoIpInterfaces.

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
    :ivar alive_check_response_timeout: This attribute defines the
        timeout  in seconds for waiting for response to an Alive Check
        request before the connection is considered to be disconnected.
        Represents parameter T_TCP_AliveCheck of ISO 13400-2:2012.
    :ivar do_ip_routing_activations: Collection of DoIpRoutingActivation
        possibilities defined in the DoIpInterface.
    :ivar doip_channel_collection_ref: Configuration of DoIPChannels
        available in an DoIpInterface. Each DoIPChannel describes a
        connection between a doIpSourceAddress and a doIpTargetAddress
        and the exchange of DcmIPdus between the PduR and DoIP. A DoIP
        channel is constituted by the set of all DoIpTpConnection
        elements via which the configured EcuInstance sends or receives
        SDUs that are sharing the same local diagnosis address and
        tester address.
    :ivar doip_connection_refs: DoIP Connections in the DoIpInterface
        that define the DoIP Pdus that are sent and received via SoAd
        over TCP or UDP.
    :ivar general_inactivity_time: This attribute defines the timeout in
        seconds for maximum inactivity of a TCP socket connection before
        the DoIP module will close the according socket connection.
        Represents parameter T_TCP_General_Inactivity of ISO
        13400-2:2012
    :ivar initial_inactivity_time: This attribute defines the timeout in
        seconds used for initial inactivity of a connected TCP socket
        connection directly after socket connection. Represents
        parameter T_TCP_Initial_Inactivity of ISO 13400-2:2012
    :ivar initial_vehicle_announcement_time: This attribute defines the
        waiting time in seconds for sending first vehicle announcement
        message after IP address assignment. Represents parameter
        A_DoIP_Announce_Wait of ISO 13400-2:2012
    :ivar is_activation_line_dependent: This attribute defines whether
        the network interface * is started "on-demand" when an
        activation line is sensed or * is always available.
    :ivar max_tester_connections: Maximum amount of tester connections
        that shall be maintained at one time before alive check is
        performed.
    :ivar socket_connection_refs: DoIP Connections in the DoIpInterface
        that define the DoIP Pdus that are sent and received via SoAd
        over TCP or UDP.
    :ivar use_mac_address_for_identification: This attribute defines
        whether a configured EID at vehicle identification
        response/vehicle announcement is used or the MAC address. TRUE:
        Use MAC Address instead of EID for Vehicle
        identification/announcement. FALSE: Use configured EID for
        vehicle identification/announcement.
    :ivar use_vehicle_identification_sync_status: This attribute defines
        if the optional VIN/GID synchronization status is used
        additionally in the vehicle identification/announcement.
    :ivar vehicle_announcement_count: This attribute defines the number
        of vehicle announcement messages on IP address assignment.
        Represents parameter A_DoIP_Announce_Num of ISO 13400-2:2012.
    :ivar vehicle_announcement_interval: This attribute defines the
        waiting time in seconds for sending subsequent vehicle
        announcement messages. Represents parameter
        A_DoIP_Announce_Interval of ISO 13400-2:2012
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
        name = "DO-IP-INTERFACE"

    short_name: None | Identifier = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: None | DoIpInterface.ShortNameFragments = field(
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
    annotations: None | DoIpInterface.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    alive_check_response_timeout: None | TimeValue = field(
        default=None,
        metadata={
            "name": "ALIVE-CHECK-RESPONSE-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    do_ip_routing_activations: None | DoIpInterface.DoIpRoutingActivations = (
        field(
            default=None,
            metadata={
                "name": "DO-IP-ROUTING-ACTIVATIONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    doip_channel_collection_ref: (
        None | DoIpInterface.DoipChannelCollectionRef
    ) = field(
        default=None,
        metadata={
            "name": "DOIP-CHANNEL-COLLECTION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    doip_connection_refs: None | DoIpInterface.DoipConnectionRefs = field(
        default=None,
        metadata={
            "name": "DOIP-CONNECTION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    general_inactivity_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "GENERAL-INACTIVITY-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    initial_inactivity_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "INITIAL-INACTIVITY-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    initial_vehicle_announcement_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "INITIAL-VEHICLE-ANNOUNCEMENT-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_activation_line_dependent: None | Boolean = field(
        default=None,
        metadata={
            "name": "IS-ACTIVATION-LINE-DEPENDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_tester_connections: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-TESTER-CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    socket_connection_refs: None | DoIpInterface.SocketConnectionRefs = field(
        default=None,
        metadata={
            "name": "SOCKET-CONNECTION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    use_mac_address_for_identification: None | Boolean = field(
        default=None,
        metadata={
            "name": "USE-MAC-ADDRESS-FOR-IDENTIFICATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    use_vehicle_identification_sync_status: None | Boolean = field(
        default=None,
        metadata={
            "name": "USE-VEHICLE-IDENTIFICATION-SYNC-STATUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vehicle_announcement_count: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "VEHICLE-ANNOUNCEMENT-COUNT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vehicle_announcement_interval: None | TimeValue = field(
        default=None,
        metadata={
            "name": "VEHICLE-ANNOUNCEMENT-INTERVAL",
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

    @dataclass
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DoIpRoutingActivations:
        do_ip_routing_activation: list[DoIpRoutingActivation] = field(
            default_factory=list,
            metadata={
                "name": "DO-IP-ROUTING-ACTIVATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DoipChannelCollectionRef(Ref):
        dest: None | DoIpTpConfigSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DoipConnectionRefs:
        doip_connection_ref: list[
            DoIpInterface.DoipConnectionRefs.DoipConnectionRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "DOIP-CONNECTION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DoipConnectionRef(Ref):
            dest: None | SocketConnectionBundleSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SocketConnectionRefs:
        socket_connection_ref: list[
            DoIpInterface.SocketConnectionRefs.SocketConnectionRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOCKET-CONNECTION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SocketConnectionRef(Ref):
            dest: None | StaticSocketConnectionSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
