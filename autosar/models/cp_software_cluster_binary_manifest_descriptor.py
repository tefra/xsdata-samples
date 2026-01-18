from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .binary_manifest_meta_data_field import BinaryManifestMetaDataField
from .binary_manifest_provide_resource import BinaryManifestProvideResource
from .binary_manifest_require_resource import BinaryManifestRequireResource
from .binary_manifest_resource_definition import (
    BinaryManifestResourceDefinition,
)
from .category_string import CategoryString
from .cp_software_cluster_subtypes_enum import CpSoftwareClusterSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CpSoftwareClusterBinaryManifestDescriptor:
    """
    This meta-class has the ability to act as a hub for all information
    related to the binary manifest of a given CP software cluster.

    The manifest is subject to integrator work and therefore not a part of
    the definition of the CP software cluster itself.

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
    :ivar cp_software_cluster_ref: This reference identifies the
        CpSoftwareCluster to which the enclosing
        CpSoftwareClusterBinaryManifestDescriptor belongs, The
        CpSoftwareClusterBinaryManifestDescriptor is defined in an
        integration phase while the refrenced CpSoftwareCluster
        represents a design element. Therefore, it makes sense to use a
        reference rather than an aggregation in the relation of the two
        meta-classes.
    :ivar meta_data_fields: This aggregation identifies the collection
        of meta-data contained in the enclosing binary manifest.
    :ivar provide_resources: This aggregation represents the collection
        of provided resources in the enclosing binary manifest.
    :ivar require_resources: This aggregation represents the collection
        of required resources in the enclosing binary manifest.
    :ivar resource_definitions: This aggregation represents the
        collection of binary manifest resource definitions that belong
        to the enclosing CpSoftwareClusterBinaryManifestDescriptor.
    :ivar software_cluster_id: This attribute represents the value of
        the id of the corresponding CP software cluster. This id is only
        assigned by an integrator and can therefore not be part of the
        description of the CP software cluster itself.
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
        name = "CP-SOFTWARE-CLUSTER-BINARY-MANIFEST-DESCRIPTOR"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: CpSoftwareClusterBinaryManifestDescriptor.ShortNameFragments | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: AdminData | None = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: CpSoftwareClusterBinaryManifestDescriptor.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cp_software_cluster_ref: CpSoftwareClusterBinaryManifestDescriptor.CpSoftwareClusterRef | None = field(
        default=None,
        metadata={
            "name": "CP-SOFTWARE-CLUSTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    meta_data_fields: CpSoftwareClusterBinaryManifestDescriptor.MetaDataFields | None = field(
        default=None,
        metadata={
            "name": "META-DATA-FIELDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    provide_resources: CpSoftwareClusterBinaryManifestDescriptor.ProvideResources | None = field(
        default=None,
        metadata={
            "name": "PROVIDE-RESOURCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    require_resources: CpSoftwareClusterBinaryManifestDescriptor.RequireResources | None = field(
        default=None,
        metadata={
            "name": "REQUIRE-RESOURCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    resource_definitions: CpSoftwareClusterBinaryManifestDescriptor.ResourceDefinitions | None = field(
        default=None,
        metadata={
            "name": "RESOURCE-DEFINITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    software_cluster_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SOFTWARE-CLUSTER-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: str | None = field(
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
    class CpSoftwareClusterRef(Ref):
        dest: CpSoftwareClusterSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class MetaDataFields:
        binary_manifest_meta_data_field: list[BinaryManifestMetaDataField] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BINARY-MANIFEST-META-DATA-FIELD",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class ProvideResources:
        binary_manifest_provide_resource: list[
            BinaryManifestProvideResource
        ] = field(
            default_factory=list,
            metadata={
                "name": "BINARY-MANIFEST-PROVIDE-RESOURCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequireResources:
        binary_manifest_require_resource: list[
            BinaryManifestRequireResource
        ] = field(
            default_factory=list,
            metadata={
                "name": "BINARY-MANIFEST-REQUIRE-RESOURCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ResourceDefinitions:
        binary_manifest_resource_definition: list[
            BinaryManifestResourceDefinition
        ] = field(
            default_factory=list,
            metadata={
                "name": "BINARY-MANIFEST-RESOURCE-DEFINITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
