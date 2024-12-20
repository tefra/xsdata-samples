from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .can_nm_cluster import CanNmCluster
from .can_nm_cluster_coupling import CanNmClusterCoupling
from .category_string import CategoryString
from .flexray_nm_cluster import FlexrayNmCluster
from .flexray_nm_cluster_coupling import FlexrayNmClusterCoupling
from .identifier import Identifier
from .j_1939_nm_cluster import J1939NmCluster
from .lin_nm_cluster import LinNmCluster
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nm_ecu import NmEcu
from .short_name_fragment import ShortNameFragment
from .udp_nm_cluster import UdpNmCluster
from .udp_nm_cluster_coupling import UdpNmClusterCoupling

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NmConfig:
    """
    Contains the all configuration elements for AUTOSAR Nm.

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
    :ivar nm_clusters: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar nm_cluster_couplings: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar nm_if_ecus: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
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
        name = "NM-CONFIG"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["NmConfig.ShortNameFragments"] = field(
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
    annotations: Optional["NmConfig.Annotations"] = field(
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
    nm_clusters: Optional["NmConfig.NmClusters"] = field(
        default=None,
        metadata={
            "name": "NM-CLUSTERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_cluster_couplings: Optional["NmConfig.NmClusterCouplings"] = field(
        default=None,
        metadata={
            "name": "NM-CLUSTER-COUPLINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_if_ecus: Optional["NmConfig.NmIfEcus"] = field(
        default=None,
        metadata={
            "name": "NM-IF-ECUS",
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
    class NmClusters:
        can_nm_cluster: list[CanNmCluster] = field(
            default_factory=list,
            metadata={
                "name": "CAN-NM-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_nm_cluster: list[FlexrayNmCluster] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-NM-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_nm_cluster: list[J1939NmCluster] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-NM-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_nm_cluster: list[LinNmCluster] = field(
            default_factory=list,
            metadata={
                "name": "LIN-NM-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        udp_nm_cluster: list[UdpNmCluster] = field(
            default_factory=list,
            metadata={
                "name": "UDP-NM-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class NmClusterCouplings:
        can_nm_cluster_coupling: list[CanNmClusterCoupling] = field(
            default_factory=list,
            metadata={
                "name": "CAN-NM-CLUSTER-COUPLING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_nm_cluster_coupling: list[FlexrayNmClusterCoupling] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-NM-CLUSTER-COUPLING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        udp_nm_cluster_coupling: list[UdpNmClusterCoupling] = field(
            default_factory=list,
            metadata={
                "name": "UDP-NM-CLUSTER-COUPLING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class NmIfEcus:
        nm_ecu: list[NmEcu] = field(
            default_factory=list,
            metadata={
                "name": "NM-ECU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
