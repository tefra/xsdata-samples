from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .byte_order_enum import ByteOrderEnum
from .category_string import CategoryString
from .chapter import Chapter
from .client_id_definition_set_subtypes_enum import (
    ClientIdDefinitionSetSubtypesEnum,
)
from .cp_software_cluster_ref_conditional import (
    CpSoftwareClusterRefConditional,
)
from .fibex_element_ref_conditional import FibexElementRefConditional
from .identifier import Identifier
from .interpolation_routine_mapping_set_subtypes_enum import (
    InterpolationRoutineMappingSetSubtypesEnum,
)
from .j_1939_shared_address_cluster import J1939SharedAddressCluster
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .revision_label_string import RevisionLabelString
from .root_sw_composition_prototype import RootSwCompositionPrototype
from .short_name_fragment import ShortNameFragment
from .system_mapping import SystemMapping

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class System:
    """@RESTRICT_TO_STANDARD:CP!
    The top level element of the System Description.
    The System description defines five major elements: Topology, Software, Communication, Mapping and Mapping Constraints.
    The System element directly aggregates the elements describing the Software, Mapping and Mapping Constraints; it contains a reference to an ASAM FIBEX description specifying Communication and Topology.
    @END_RESTRICT_TO_STANDARD!
    @RESTRICT_TO_STANDARD:AP!
    The top level element of the System Description.
    @END_RESTRICT_TO_STANDARD!
    @RESTRICT_TO_STANDARD:FO!
    The top level element of the Abstract Platform System Description.
    @END_RESTRICT_TO_STANDARD!

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
    :ivar system_documentations: Possibility to provide additional
        documentation while defining the System. The System
        documentation can be composed of several chapters. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar client_id_definition_set_refs: Set of Client Identifiers that
        are used for inter-ECU client-server communication in the
        System.
    :ivar container_i_pdu_header_byte_order: Defines the byteOrder of
        the header in ContainerIPdus.
    :ivar ecu_extract_version: Version number of the Ecu Extract.
    :ivar fibex_elements: This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar interpolation_routine_mapping_set_refs: This reference
        identifies the InterpolationRoutineMappingSets that are relevant
        in the context of the enclosing System.
    :ivar j_1939_shared_address_clusters: Collection of J1939Clusters
        that share a common address space for the routing of messages.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        -1.
    :ivar mappings: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar pnc_vector_length: Length of the partial networking request
        release information vector (in bytes).
    :ivar pnc_vector_offset: Absolute offset (with respect to the NM-
        PDU) of the partial networking request release information
        vector that is defined in bytes as an index starting with 0.
    :ivar root_software_compositions: The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was 1.
    :ivar sw_clusters: CP Software Clusters of this System This property
        was modified due to atpVariation (DirectedAssociationPattern).
    :ivar system_version: Version number of the System Description.
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
        name = "SYSTEM"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["System.ShortNameFragments"] = field(
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
    annotations: Optional["System.Annotations"] = field(
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
    system_documentations: Optional["System.SystemDocumentations"] = field(
        default=None,
        metadata={
            "name": "SYSTEM-DOCUMENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_id_definition_set_refs: Optional[
        "System.ClientIdDefinitionSetRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CLIENT-ID-DEFINITION-SET-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    container_i_pdu_header_byte_order: Optional[ByteOrderEnum] = field(
        default=None,
        metadata={
            "name": "CONTAINER-I-PDU-HEADER-BYTE-ORDER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_extract_version: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "ECU-EXTRACT-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    fibex_elements: Optional["System.FibexElements"] = field(
        default=None,
        metadata={
            "name": "FIBEX-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    interpolation_routine_mapping_set_refs: Optional[
        "System.InterpolationRoutineMappingSetRefs"
    ] = field(
        default=None,
        metadata={
            "name": "INTERPOLATION-ROUTINE-MAPPING-SET-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    j_1939_shared_address_clusters: Optional[
        "System.J1939SharedAddressClusters"
    ] = field(
        default=None,
        metadata={
            "name": "J-1939-SHARED-ADDRESS-CLUSTERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mappings: Optional["System.Mappings"] = field(
        default=None,
        metadata={
            "name": "MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_vector_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PNC-VECTOR-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_vector_offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PNC-VECTOR-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_software_compositions: Optional["System.RootSoftwareCompositions"] = (
        field(
            default=None,
            metadata={
                "name": "ROOT-SOFTWARE-COMPOSITIONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    sw_clusters: Optional["System.SwClusters"] = field(
        default=None,
        metadata={
            "name": "SW-CLUSTERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    system_version: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "SYSTEM-VERSION",
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
    class SystemDocumentations:
        chapter: list[Chapter] = field(
            default_factory=list,
            metadata={
                "name": "CHAPTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ClientIdDefinitionSetRefs:
        client_id_definition_set_ref: list[
            "System.ClientIdDefinitionSetRefs.ClientIdDefinitionSetRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-ID-DEFINITION-SET-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ClientIdDefinitionSetRef(Ref):
            dest: Optional[ClientIdDefinitionSetSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class FibexElements:
        fibex_element_ref_conditional: list[FibexElementRefConditional] = (
            field(
                default_factory=list,
                metadata={
                    "name": "FIBEX-ELEMENT-REF-CONDITIONAL",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class InterpolationRoutineMappingSetRefs:
        interpolation_routine_mapping_set_ref: list[
            "System.InterpolationRoutineMappingSetRefs.InterpolationRoutineMappingSetRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "INTERPOLATION-ROUTINE-MAPPING-SET-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class InterpolationRoutineMappingSetRef(Ref):
            dest: Optional[InterpolationRoutineMappingSetSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class J1939SharedAddressClusters:
        j_1939_shared_address_cluster: list[J1939SharedAddressCluster] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-SHARED-ADDRESS-CLUSTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Mappings:
        system_mapping: list[SystemMapping] = field(
            default_factory=list,
            metadata={
                "name": "SYSTEM-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RootSoftwareCompositions:
        root_sw_composition_prototype: list[RootSwCompositionPrototype] = (
            field(
                default_factory=list,
                metadata={
                    "name": "ROOT-SW-COMPOSITION-PROTOTYPE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class SwClusters:
        cp_software_cluster_ref_conditional: list[
            CpSoftwareClusterRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "CP-SOFTWARE-CLUSTER-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
