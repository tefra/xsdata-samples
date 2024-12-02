from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .cp_software_cluster_resource_to_application_partition_mapping import (
    CpSoftwareClusterResourceToApplicationPartitionMapping,
)
from .cp_software_cluster_to_resource_mapping import (
    CpSoftwareClusterToResourceMapping,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .port_element_to_communication_resource_mapping import (
    PortElementToCommunicationResourceMapping,
)
from .short_name_fragment import ShortNameFragment
from .swc_to_application_partition_mapping import (
    SwcToApplicationPartitionMapping,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CpSoftwareClusterMappingSet:
    """This meta-class represents the ability to aggregate a collection of CP
    Software Cluster relevant mappings.

    This is applicable if a CP Software Cluster is described besides a
    concrete System, e.g. a reusable CP Software Cluster.

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
    :ivar port_element_to_com_resource_mappings: maps a communication
        resource to CP Software Clusters The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar resource_to_application_partition_mappings: Maps a Software
        Cluster resource to an Application Partition to restrict the
        usage. The upper multiplicity of this role has been increased to
        * due to resolving an atpVariation stereotype. The previous
        value was -1.
    :ivar software_cluster_to_resource_mappings: maps a service resource
        to CP Software Clusters The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar swc_to_application_partition_mappings: maps
        SwComponentPrototypes in a CP Software Cluster to
        ApplicationPartitions The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
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
        name = "CP-SOFTWARE-CLUSTER-MAPPING-SET"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "CpSoftwareClusterMappingSet.ShortNameFragments"
    ] = field(
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
    annotations: Optional["CpSoftwareClusterMappingSet.Annotations"] = field(
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
    port_element_to_com_resource_mappings: Optional[
        "CpSoftwareClusterMappingSet.PortElementToComResourceMappings"
    ] = field(
        default=None,
        metadata={
            "name": "PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    resource_to_application_partition_mappings: Optional[
        "CpSoftwareClusterMappingSet.ResourceToApplicationPartitionMappings"
    ] = field(
        default=None,
        metadata={
            "name": "RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    software_cluster_to_resource_mappings: Optional[
        "CpSoftwareClusterMappingSet.SoftwareClusterToResourceMappings"
    ] = field(
        default=None,
        metadata={
            "name": "SOFTWARE-CLUSTER-TO-RESOURCE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    swc_to_application_partition_mappings: Optional[
        "CpSoftwareClusterMappingSet.SwcToApplicationPartitionMappings"
    ] = field(
        default=None,
        metadata={
            "name": "SWC-TO-APPLICATION-PARTITION-MAPPINGS",
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
    class PortElementToComResourceMappings:
        port_element_to_communication_resource_mapping: list[
            PortElementToCommunicationResourceMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ResourceToApplicationPartitionMappings:
        cp_software_cluster_resource_to_application_partition_mapping: list[
            CpSoftwareClusterResourceToApplicationPartitionMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SoftwareClusterToResourceMappings:
        cp_software_cluster_to_resource_mapping: list[
            CpSoftwareClusterToResourceMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SwcToApplicationPartitionMappings:
        swc_to_application_partition_mapping: list[
            SwcToApplicationPartitionMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TO-APPLICATION-PARTITION-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
