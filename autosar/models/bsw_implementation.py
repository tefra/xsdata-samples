from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .bsw_debug_info import BswDebugInfo
from .bsw_internal_behavior_subtypes_enum import (
    BswInternalBehaviorSubtypesEnum,
)
from .build_action_manifest_ref_conditional import (
    BuildActionManifestRefConditional,
)
from .category_string import CategoryString
from .code import Code
from .compiler import Compiler
from .dependency_on_artifact import DependencyOnArtifact
from .ecuc_module_configuration_values_subtypes_enum import (
    EcucModuleConfigurationValuesSubtypesEnum,
)
from .ecuc_module_def_subtypes_enum import EcucModuleDefSubtypesEnum
from .hw_element_subtypes_enum import HwElementSubtypesEnum
from .identifier import Identifier
from .linker import Linker
from .mc_support_data import McSupportData
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .programminglanguage_enum import ProgramminglanguageEnum
from .ref import Ref
from .resource_consumption import ResourceConsumption
from .revision_label_string import RevisionLabelString
from .short_name_fragment import ShortNameFragment
from .string import String
from .swc_bsw_mapping_subtypes_enum import SwcBswMappingSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswImplementation:
    """
    Contains the implementation specific information in addition to the
    generic specification (BswModuleDescription and BswBehavior).

    It is possible to have several different BswImplementations referring
    to the same BswBehavior.

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
    :ivar build_action_manifests: A manifest specifying the intended
        build actions for the software delivered with this
        implementation. This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar code_descriptors: Specifies the provided implementation code.
    :ivar compilers: Specifies the compiler for which this
        implementation has been released
    :ivar generated_artifacts: Relates to an artifact that will be
        generated during the integration of this Implementation by an
        associated generator tool. Note that this is an optional
        information since it might  not always be in the scope of a
        single module or component  to provide this information. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar hw_element_refs: The hardware elements (e.g. the processor)
        required for this implementation.
    :ivar linkers: Specifies the linker for which this implementation
        has been released.
    :ivar mc_support: The measurement &amp; calibration support data
        belonging to this implementation. The aggregtion is
        &lt;&lt;atpSplitable&gt;&gt; because in case of an already
        exisiting BSW Implementation model, this description will be
        added later in the process, namely at code generation time.
    :ivar programming_language: Programming language the implementation
        was created in.
    :ivar required_artifacts: Specifies that this Implementation depends
        on the existance of another artifact (e.g. a library). This
        aggregation of DependencyOnArtifact is subject to variability
        with the purpose to support variability in the implementations.
        Different algorithms in the implementation might cause different
        dependencies, e.g. the number of used libraries. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar required_generator_tools: Relates this Implementation to a
        generator tool in order to generate additional artifacts during
        integration. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar resource_consumption: All static and dynamic resources for
        each implementation are described  within the
        ResourceConsumption class.
    :ivar sw_version: Software version of this implementation. The
        numbering contains three levels (like major, minor, patch), its
        values are vendor specific.
    :ivar swc_bsw_mapping_ref: This allows a mapping between an SWC and
        a BSW behavior to be attached to an implementation description
        (for AUTOSAR Service, ECU Abstraction and Complex Driver
        Components).  It is up to the methodology to define whether this
        reference has to be set for the Swc- or BswImplementtion or for
        both.
    :ivar used_code_generator: Optional: code generator used.
    :ivar vendor_id: Vendor ID of this Implementation according to the
        AUTOSAR vendor list
    :ivar ar_release_version: Version of the AUTOSAR Release on which
        this implementation is based. The numbering contains three
        levels (major, minor, revision) which are defined by AUTOSAR.
    :ivar behavior_ref: The behavior of this implementation. This
        relation is made as an association because * it follows the
        pattern of the SWCT * since ARElement cannot be splitted, but we
        want supply the implementation later, the BswImplementation is
        not aggregated in BswBehavior
    :ivar debug_infos: Collects the debug info for this implementation.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        1.
    :ivar preconfigured_configuration_refs: Reference to the set of
        preconfigured (i.e. fixed) configuration values for this
        BswImplementation. If the BswImplementation represents a cluster
        of several modules, more than one EcucModuleConfigurationValues
        element can be referred (at most one per module), otherwise at
        most one such element can be referred.
    :ivar recommended_configuration_refs: Reference to one or more sets
        of recommended configuration values for this module or module
        cluster.
    :ivar vendor_api_infix: In driver modules which can be instantiated
        several times on a single ECU, SRS_BSW_00347 requires that the
        names of files, APIs, published parameters and memory allocation
        keywords are extended by the vendorId and a vendor specific
        name. This parameter is used to specify the vendor specific
        name. In total, the implementation specific API name is
        generated as follows: &lt;ModuleName&gt;_&lt;vendorId&gt;_
        &lt;vendorApiInfix&gt;_&lt;API name from SWS&gt;. E.g.  assuming
        that the vendorId of the implementer is 123 and the implementer
        chose a vendorApiInfix of "v11r456" an API name Can_Write
        defined in the SWS will translate to Can_123_v11r456_Write. This
        attribute is mandatory for all modules with upper multiplicity
        &gt; 1. It shall not be used for modules with upper multiplicity
        =1. See also SWS_BSW_00102.
    :ivar vendor_specific_module_def_refs: Reference to * the vendor
        specific EcucModuleDef used in this BswImplementation if it
        represents a single module * several EcucModuleDefs used in this
        BswImplementation if it  represents a cluster of modules * one
        or no EcucModuleDefs used in this BswImplementation if it
        represents a library
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
        name = "BSW-IMPLEMENTATION"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["BswImplementation.ShortNameFragments"] = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    annotations: Optional["BswImplementation.Annotations"] = field(
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
    build_action_manifests: Optional[
        "BswImplementation.BuildActionManifests"
    ] = field(
        default=None,
        metadata={
            "name": "BUILD-ACTION-MANIFESTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    code_descriptors: Optional["BswImplementation.CodeDescriptors"] = field(
        default=None,
        metadata={
            "name": "CODE-DESCRIPTORS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    compilers: Optional["BswImplementation.Compilers"] = field(
        default=None,
        metadata={
            "name": "COMPILERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    generated_artifacts: Optional["BswImplementation.GeneratedArtifacts"] = (
        field(
            default=None,
            metadata={
                "name": "GENERATED-ARTIFACTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    hw_element_refs: Optional["BswImplementation.HwElementRefs"] = field(
        default=None,
        metadata={
            "name": "HW-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    linkers: Optional["BswImplementation.Linkers"] = field(
        default=None,
        metadata={
            "name": "LINKERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_support: Optional[McSupportData] = field(
        default=None,
        metadata={
            "name": "MC-SUPPORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    programming_language: Optional[ProgramminglanguageEnum] = field(
        default=None,
        metadata={
            "name": "PROGRAMMING-LANGUAGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_artifacts: Optional["BswImplementation.RequiredArtifacts"] = (
        field(
            default=None,
            metadata={
                "name": "REQUIRED-ARTIFACTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    required_generator_tools: Optional[
        "BswImplementation.RequiredGeneratorTools"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-GENERATOR-TOOLS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    resource_consumption: Optional[ResourceConsumption] = field(
        default=None,
        metadata={
            "name": "RESOURCE-CONSUMPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_version: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "SW-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    swc_bsw_mapping_ref: Optional["BswImplementation.SwcBswMappingRef"] = (
        field(
            default=None,
            metadata={
                "name": "SWC-BSW-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    used_code_generator: Optional[String] = field(
        default=None,
        metadata={
            "name": "USED-CODE-GENERATOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vendor_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "VENDOR-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ar_release_version: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "AR-RELEASE-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    behavior_ref: Optional["BswImplementation.BehaviorRef"] = field(
        default=None,
        metadata={
            "name": "BEHAVIOR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    debug_infos: Optional["BswImplementation.DebugInfos"] = field(
        default=None,
        metadata={
            "name": "DEBUG-INFOS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    preconfigured_configuration_refs: Optional[
        "BswImplementation.PreconfiguredConfigurationRefs"
    ] = field(
        default=None,
        metadata={
            "name": "PRECONFIGURED-CONFIGURATION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    recommended_configuration_refs: Optional[
        "BswImplementation.RecommendedConfigurationRefs"
    ] = field(
        default=None,
        metadata={
            "name": "RECOMMENDED-CONFIGURATION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vendor_api_infix: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "VENDOR-API-INFIX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vendor_specific_module_def_refs: Optional[
        "BswImplementation.VendorSpecificModuleDefRefs"
    ] = field(
        default=None,
        metadata={
            "name": "VENDOR-SPECIFIC-MODULE-DEF-REFS",
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
    class BuildActionManifests:
        build_action_manifest_ref_conditional: list[
            BuildActionManifestRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "BUILD-ACTION-MANIFEST-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CodeDescriptors:
        code: list[Code] = field(
            default_factory=list,
            metadata={
                "name": "CODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Compilers:
        compiler: list[Compiler] = field(
            default_factory=list,
            metadata={
                "name": "COMPILER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class GeneratedArtifacts:
        dependency_on_artifact: list[DependencyOnArtifact] = field(
            default_factory=list,
            metadata={
                "name": "DEPENDENCY-ON-ARTIFACT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class HwElementRefs:
        hw_element_ref: list[
            "BswImplementation.HwElementRefs.HwElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "HW-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class HwElementRef(Ref):
            dest: Optional[HwElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class Linkers:
        linker: list[Linker] = field(
            default_factory=list,
            metadata={
                "name": "LINKER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequiredArtifacts:
        dependency_on_artifact: list[DependencyOnArtifact] = field(
            default_factory=list,
            metadata={
                "name": "DEPENDENCY-ON-ARTIFACT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequiredGeneratorTools:
        dependency_on_artifact: list[DependencyOnArtifact] = field(
            default_factory=list,
            metadata={
                "name": "DEPENDENCY-ON-ARTIFACT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SwcBswMappingRef(Ref):
        dest: Optional[SwcBswMappingSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class BehaviorRef(Ref):
        dest: Optional[BswInternalBehaviorSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DebugInfos:
        bsw_debug_info: list[BswDebugInfo] = field(
            default_factory=list,
            metadata={
                "name": "BSW-DEBUG-INFO",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PreconfiguredConfigurationRefs:
        preconfigured_configuration_ref: list[
            "BswImplementation.PreconfiguredConfigurationRefs.PreconfiguredConfigurationRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "PRECONFIGURED-CONFIGURATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PreconfiguredConfigurationRef(Ref):
            dest: Optional[EcucModuleConfigurationValuesSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class RecommendedConfigurationRefs:
        recommended_configuration_ref: list[
            "BswImplementation.RecommendedConfigurationRefs.RecommendedConfigurationRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "RECOMMENDED-CONFIGURATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RecommendedConfigurationRef(Ref):
            dest: Optional[EcucModuleConfigurationValuesSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class VendorSpecificModuleDefRefs:
        vendor_specific_module_def_ref: list[
            "BswImplementation.VendorSpecificModuleDefRefs.VendorSpecificModuleDefRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "VENDOR-SPECIFIC-MODULE-DEF-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class VendorSpecificModuleDefRef(Ref):
            dest: Optional[EcucModuleDefSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
