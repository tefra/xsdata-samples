from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .can_nm_node import CanNmNode
from .category_string import CategoryString
from .communication_cluster_subtypes_enum import (
    CommunicationClusterSubtypesEnum,
)
from .flexray_nm_node import FlexrayNmNode
from .identifier import Identifier
from .j_1939_nm_node import J1939NmNode
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .udp_nm_node import UdpNmNode

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinNmCluster:
    """
    Lin specific NmCluster attributes.

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
    :ivar communication_cluster_ref: Association to a
        CommunicationCluster in the topology description.
    :ivar nm_channel_id: This attribute has the status "removed" and
        shall not be used any longer. Old description: Channel
        identification number of the corresponding channel. Must be
        unique over all NmClusters.
    :ivar nm_channel_sleep_master: This parameter shall be set to
        indicate if the sleep of this network can be absolutely decided
        by the local node only and that no other nodes can oppose that
        decision.
    :ivar nm_nodes: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar nm_node_detection_enabled: Enables the Request Repeat Message
        Request support. Only valid if nmNodeIdEnabled is set to true.
    :ivar nm_node_id_enabled: Enables the source node identifier.
    :ivar nm_pnc_participation: Defines whether this NmCluster
        contributes to the partial network mechanism.
    :ivar nm_repeat_msg_ind_enabled: Switch for enabling the Repeat
        Message Bit Indication.
    :ivar nm_synchronizing_network: If this parameter is true, then this
        network is a synchronizing network for the NM coordination
        cluster which it belongs to. The network is expected to call
        Nm_SynchronizationPoint() at regular intervals.
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
        name = "LIN-NM-CLUSTER"

    short_name: None | Identifier = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: None | LinNmCluster.ShortNameFragments = field(
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
    annotations: None | LinNmCluster.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    communication_cluster_ref: None | LinNmCluster.CommunicationClusterRef = (
        field(
            default=None,
            metadata={
                "name": "COMMUNICATION-CLUSTER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    nm_channel_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "NM-CHANNEL-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_channel_sleep_master: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-CHANNEL-SLEEP-MASTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_nodes: None | LinNmCluster.NmNodes = field(
        default=None,
        metadata={
            "name": "NM-NODES",
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
    nm_pnc_participation: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-PNC-PARTICIPATION",
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
    nm_synchronizing_network: None | Boolean = field(
        default=None,
        metadata={
            "name": "NM-SYNCHRONIZING-NETWORK",
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
    class CommunicationClusterRef(Ref):
        dest: None | CommunicationClusterSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class NmNodes:
        can_nm_node: list[CanNmNode] = field(
            default_factory=list,
            metadata={
                "name": "CAN-NM-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_nm_node: list[FlexrayNmNode] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-NM-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_nm_node: list[J1939NmNode] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-NM-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        udp_nm_node: list[UdpNmNode] = field(
            default_factory=list,
            metadata={
                "name": "UDP-NM-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
