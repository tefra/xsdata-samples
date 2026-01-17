from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .application_partition_to_ecu_partition_mapping import (
    ApplicationPartitionToEcuPartitionMapping,
)
from .category_string import CategoryString
from .client_server_to_signal_group_mapping import (
    ClientServerToSignalGroupMapping,
)
from .client_server_to_signal_mapping import ClientServerToSignalMapping
from .com_management_mapping import ComManagementMapping
from .common_signal_path import CommonSignalPath
from .component_clustering import ComponentClustering
from .component_separation import ComponentSeparation
from .cp_software_cluster_resource_to_application_partition_mapping import (
    CpSoftwareClusterResourceToApplicationPartitionMapping,
)
from .cp_software_cluster_to_ecu_instance_mapping import (
    CpSoftwareClusterToEcuInstanceMapping,
)
from .cp_software_cluster_to_resource_mapping import (
    CpSoftwareClusterToResourceMapping,
)
from .ecu_mapping import EcuMapping
from .ecu_resource_estimation import EcuResourceEstimation
from .forbidden_signal_path import ForbiddenSignalPath
from .identifier import Identifier
from .j_1939_controller_application_to_j_1939_nm_node_mapping import (
    J1939ControllerApplicationToJ1939NmNodeMapping,
)
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .permissible_signal_path import PermissibleSignalPath
from .pnc_mapping import PncMapping
from .port_element_to_communication_resource_mapping import (
    PortElementToCommunicationResourceMapping,
)
from .sec_oc_crypto_service_mapping import SecOcCryptoServiceMapping
from .sender_receiver_composite_element_to_signal_mapping import (
    SenderReceiverCompositeElementToSignalMapping,
)
from .sender_receiver_to_signal_group_mapping import (
    SenderReceiverToSignalGroupMapping,
)
from .sender_receiver_to_signal_mapping import SenderReceiverToSignalMapping
from .separate_signal_path import SeparateSignalPath
from .short_name_fragment import ShortNameFragment
from .swc_to_application_partition_mapping import (
    SwcToApplicationPartitionMapping,
)
from .swc_to_ecu_mapping import SwcToEcuMapping
from .swc_to_ecu_mapping_constraint import SwcToEcuMappingConstraint
from .swc_to_impl_mapping import SwcToImplMapping
from .tls_crypto_service_mapping import TlsCryptoServiceMapping
from .trigger_to_signal_mapping import TriggerToSignalMapping

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SystemMapping:
    """
    @RESTRICT_TO_STANDARD:CP!

    The system mapping aggregates all mapping aspects (mapping of SW
    components to ECUs, mapping of data elements to signals, and mapping
    constraints). @END_RESTRICT_TO_STANDARD! @RESTRICT_TO_STANDARD:AP! The
    system mapping aggregates all mapping aspects that are relevant in the
    System Description. @END_RESTRICT_TO_STANDARD!

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
    :ivar application_partition_to_ecu_partition_mappings: Mapping of
        ApplicationPartitions to EcuPartitions The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar com_management_mappings: Mappings between Mode Management
        PortGroups and communication channels. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar crypto_service_mappings: This aggregation represents the
        collection of crypto service mappings in the context of the
        enclosing SystemMapping. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar data_mappings: The data mappings defined. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar ecu_resource_mappings: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar j_1939_controller_application_to_j_1939_nm_node_mappings:
        Mapping of a J1939ControllerApplication to a J1939NmNode.
    :ivar mapping_constraints: Constraints that limit the mapping
        freedom for the mapping of SW components to ECUs. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar pnc_mappings: Mappings between Virtual Function Clusters and
        Partial Network Clusters. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar port_element_to_com_resource_mappings: maps a communication
        resource to CP Software Clusters The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar resource_estimations: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar resource_to_application_partition_mappings: Maps a Software
        Cluster resource to an Application Partition to restrict the
        usage. The upper multiplicity of this role has been increased to
        * due to resolving an atpVariation stereotype. The previous
        value was -1.
    :ivar signal_path_constraints: Constraints that limit the mapping
        freedom for the mapping of data elements to signals. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar software_cluster_to_resource_mappings: maps a service resource
        to CP Software Clusters The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar sw_cluster_mappings: The mappings of SW cluster to ECUs. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar sw_impl_mappings: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar sw_mappings: The mappings of SW components to ECUs.
        atpVariation: SWC shall be mapped to other ECUs. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar swc_to_application_partition_mappings: Allows to map a given
        SwComponentPrototype to a formally defined partition at a point
        in time when the corresponding EcuInstance is not yet known or
        defined. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was -1.
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
        name = "SYSTEM-MAPPING"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["SystemMapping.ShortNameFragments"] = field(
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
    annotations: Optional["SystemMapping.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    application_partition_to_ecu_partition_mappings: Optional[
        "SystemMapping.ApplicationPartitionToEcuPartitionMappings"
    ] = field(
        default=None,
        metadata={
            "name": "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    com_management_mappings: Optional[
        "SystemMapping.ComManagementMappings"
    ] = field(
        default=None,
        metadata={
            "name": "COM-MANAGEMENT-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    crypto_service_mappings: Optional[
        "SystemMapping.CryptoServiceMappings"
    ] = field(
        default=None,
        metadata={
            "name": "CRYPTO-SERVICE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_mappings: Optional["SystemMapping.DataMappings"] = field(
        default=None,
        metadata={
            "name": "DATA-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_resource_mappings: Optional["SystemMapping.EcuResourceMappings"] = (
        field(
            default=None,
            metadata={
                "name": "ECU-RESOURCE-MAPPINGS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    j_1939_controller_application_to_j_1939_nm_node_mappings: Optional[
        "SystemMapping.J1939ControllerApplicationToJ1939NmNodeMappings"
    ] = field(
        default=None,
        metadata={
            "name": "J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapping_constraints: Optional["SystemMapping.MappingConstraints"] = field(
        default=None,
        metadata={
            "name": "MAPPING-CONSTRAINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_mappings: Optional["SystemMapping.PncMappings"] = field(
        default=None,
        metadata={
            "name": "PNC-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_element_to_com_resource_mappings: Optional[
        "SystemMapping.PortElementToComResourceMappings"
    ] = field(
        default=None,
        metadata={
            "name": "PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    resource_estimations: Optional["SystemMapping.ResourceEstimations"] = (
        field(
            default=None,
            metadata={
                "name": "RESOURCE-ESTIMATIONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    resource_to_application_partition_mappings: Optional[
        "SystemMapping.ResourceToApplicationPartitionMappings"
    ] = field(
        default=None,
        metadata={
            "name": "RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    signal_path_constraints: Optional[
        "SystemMapping.SignalPathConstraints"
    ] = field(
        default=None,
        metadata={
            "name": "SIGNAL-PATH-CONSTRAINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    software_cluster_to_resource_mappings: Optional[
        "SystemMapping.SoftwareClusterToResourceMappings"
    ] = field(
        default=None,
        metadata={
            "name": "SOFTWARE-CLUSTER-TO-RESOURCE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_cluster_mappings: Optional["SystemMapping.SwClusterMappings"] = field(
        default=None,
        metadata={
            "name": "SW-CLUSTER-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_impl_mappings: Optional["SystemMapping.SwImplMappings"] = field(
        default=None,
        metadata={
            "name": "SW-IMPL-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_mappings: Optional["SystemMapping.SwMappings"] = field(
        default=None,
        metadata={
            "name": "SW-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    swc_to_application_partition_mappings: Optional[
        "SystemMapping.SwcToApplicationPartitionMappings"
    ] = field(
        default=None,
        metadata={
            "name": "SWC-TO-APPLICATION-PARTITION-MAPPINGS",
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
    class ApplicationPartitionToEcuPartitionMappings:
        application_partition_to_ecu_partition_mapping: list[
            ApplicationPartitionToEcuPartitionMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ComManagementMappings:
        com_management_mapping: list[ComManagementMapping] = field(
            default_factory=list,
            metadata={
                "name": "COM-MANAGEMENT-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CryptoServiceMappings:
        sec_oc_crypto_service_mapping: list[SecOcCryptoServiceMapping] = field(
            default_factory=list,
            metadata={
                "name": "SEC-OC-CRYPTO-SERVICE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        tls_crypto_service_mapping: list[TlsCryptoServiceMapping] = field(
            default_factory=list,
            metadata={
                "name": "TLS-CRYPTO-SERVICE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataMappings:
        client_server_to_signal_group_mapping: list[
            ClientServerToSignalGroupMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-TO-SIGNAL-GROUP-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        client_server_to_signal_mapping: list[ClientServerToSignalMapping] = (
            field(
                default_factory=list,
                metadata={
                    "name": "CLIENT-SERVER-TO-SIGNAL-MAPPING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        sender_receiver_composite_element_to_signal_mapping: list[
            SenderReceiverCompositeElementToSignalMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sender_receiver_to_signal_group_mapping: list[
            SenderReceiverToSignalGroupMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sender_receiver_to_signal_mapping: list[
            SenderReceiverToSignalMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "SENDER-RECEIVER-TO-SIGNAL-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        trigger_to_signal_mapping: list[TriggerToSignalMapping] = field(
            default_factory=list,
            metadata={
                "name": "TRIGGER-TO-SIGNAL-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EcuResourceMappings:
        ecu_mapping: list[EcuMapping] = field(
            default_factory=list,
            metadata={
                "name": "ECU-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class J1939ControllerApplicationToJ1939NmNodeMappings:
        j_1939_controller_application_to_j_1939_nm_node_mapping: list[
            J1939ControllerApplicationToJ1939NmNodeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class MappingConstraints:
        component_clustering: list[ComponentClustering] = field(
            default_factory=list,
            metadata={
                "name": "COMPONENT-CLUSTERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        component_separation: list[ComponentSeparation] = field(
            default_factory=list,
            metadata={
                "name": "COMPONENT-SEPARATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        swc_to_ecu_mapping_constraint: list[SwcToEcuMappingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TO-ECU-MAPPING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PncMappings:
        pnc_mapping: list[PncMapping] = field(
            default_factory=list,
            metadata={
                "name": "PNC-MAPPING",
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
    class ResourceEstimations:
        ecu_resource_estimation: list[EcuResourceEstimation] = field(
            default_factory=list,
            metadata={
                "name": "ECU-RESOURCE-ESTIMATION",
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
    class SignalPathConstraints:
        common_signal_path: list[CommonSignalPath] = field(
            default_factory=list,
            metadata={
                "name": "COMMON-SIGNAL-PATH",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        forbidden_signal_path: list[ForbiddenSignalPath] = field(
            default_factory=list,
            metadata={
                "name": "FORBIDDEN-SIGNAL-PATH",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        permissible_signal_path: list[PermissibleSignalPath] = field(
            default_factory=list,
            metadata={
                "name": "PERMISSIBLE-SIGNAL-PATH",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        separate_signal_path: list[SeparateSignalPath] = field(
            default_factory=list,
            metadata={
                "name": "SEPARATE-SIGNAL-PATH",
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
    class SwClusterMappings:
        cp_software_cluster_to_ecu_instance_mapping: list[
            CpSoftwareClusterToEcuInstanceMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SwImplMappings:
        swc_to_impl_mapping: list[SwcToImplMapping] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TO-IMPL-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SwMappings:
        swc_to_ecu_mapping: list[SwcToEcuMapping] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TO-ECU-MAPPING",
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
