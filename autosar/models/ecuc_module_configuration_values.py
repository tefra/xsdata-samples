from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .bsw_implementation_subtypes_enum import BswImplementationSubtypesEnum
from .category_string import CategoryString
from .ecuc_configuration_variant_enum import EcucConfigurationVariantEnum
from .ecuc_container_value import EcucContainerValue
from .ecuc_module_def_subtypes_enum import EcucModuleDefSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .revision_label_string import RevisionLabelString
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucModuleConfigurationValues:
    """
    Head of the configuration of one Module.

    A Module can be a BSW module as well as the RTE and ECU Infrastructure.
    As part of the BSW module description, the
    EcucModuleConfigurationValues element has two different roles: The
    recommendedConfiguration contains parameter values recommended by the
    BSW module vendor. The preconfiguredConfiguration contains values for
    those parameters which are fixed by the implementation and cannot be
    changed. These two EcucModuleConfigurationValues are used when the base
    EcucModuleConfigurationValues (as part of the base ECU configuration)
    is created to fill parameters with initial values.

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
    :ivar definition_ref: Reference to the definition of this
        EcucModuleConfigurationValues element. Typically, this is a
        vendor specific module configuration.
    :ivar ecuc_def_edition: This is the version info of the ModuleDef
        ECUC Parameter definition to which this values conform to / are
        based on. For the Definition of ModuleDef ECUC Parameters the
        AdminData shall be used to express the semantic changes. The
        compatibility rules between the definition and value revision
        labels is up to the module's vendor.
    :ivar implementation_config_variant: Specifies the kind of
        deliverable this EcucModuleConfigurationValues element provides.
        If this element is not used in a particular role (e.g.
        preconfiguredConfiguration or recommendedConfiguration) then the
        value shall be one of VariantPreCompile, VariantLinkTime,
        VariantPostBuild.
    :ivar module_description_ref: Referencing the BSW module
        description, which this EcucModuleConfigurationValues element is
        configuring. This is optional because the
        EcucModuleConfigurationValues element is also used to configure
        the ECU infrastructure (memory map) or Application SW-Cs.
        However in case the EcucModuleConfigurationValues are used to
        configure the module, the reference is mandatory in order to
        fetch module specific "common" published information.
    :ivar post_build_variant_used: Indicates whether a module
        implementation has or plans to have (i.e., introduced at link or
        post-build time) new post-build variation points. TRUE means
        yes, FALSE means no. If the attribute is not defined, FALSE
        semantics shall be assumed.
    :ivar containers: Aggregates all containers that belong to this
        module configuration. atpVariation: [RS_ECUC_00078] The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
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
        name = "ECUC-MODULE-CONFIGURATION-VALUES"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: (
        EcucModuleConfigurationValues.ShortNameFragments | None
    ) = field(
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
    annotations: EcucModuleConfigurationValues.Annotations | None = field(
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
    definition_ref: EcucModuleConfigurationValues.DefinitionRef | None = field(
        default=None,
        metadata={
            "name": "DEFINITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecuc_def_edition: RevisionLabelString | None = field(
        default=None,
        metadata={
            "name": "ECUC-DEF-EDITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implementation_config_variant: EcucConfigurationVariantEnum | None = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-CONFIG-VARIANT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    module_description_ref: (
        EcucModuleConfigurationValues.ModuleDescriptionRef | None
    ) = field(
        default=None,
        metadata={
            "name": "MODULE-DESCRIPTION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    post_build_variant_used: Boolean | None = field(
        default=None,
        metadata={
            "name": "POST-BUILD-VARIANT-USED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    containers: EcucModuleConfigurationValues.Containers | None = field(
        default=None,
        metadata={
            "name": "CONTAINERS",
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
    class DefinitionRef(Ref):
        dest: EcucModuleDefSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ModuleDescriptionRef(Ref):
        dest: BswImplementationSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Containers:
        ecuc_container_value: list[EcucContainerValue] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-CONTAINER-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
