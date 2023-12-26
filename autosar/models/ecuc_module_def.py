from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .blueprint_policy_list import BlueprintPolicyList
from .blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from .blueprint_policy_single import BlueprintPolicySingle
from .boolean import Boolean
from .boolean_value_variation_point import BooleanValueVariationPoint
from .c_identifier import CIdentifier
from .category_string import CategoryString
from .ecuc_condition_specification import EcucConditionSpecification
from .ecuc_configuration_variant_enum import EcucConfigurationVariantEnum
from .ecuc_module_def_subtypes_enum import EcucModuleDefSubtypesEnum
from .ecuc_param_conf_container_def import (
    EcucChoiceContainerDef,
    EcucParamConfContainerDef,
)
from .ecuc_scope_enum import EcucScopeEnum
from .ecuc_validation_condition import EcucValidationCondition
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String
from .traceable_subtypes_enum import TraceableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucModuleDef:
    """
    Used as the top-level element for configuration definition for Software
    Modules, including BSW and RTE as well as ECU Infrastructure.

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
    :ivar blueprint_policys: This role indicates whether the
        blueprintable element will be modifiable or not motifiable.
    :ivar short_name_pattern: This attribute represents the pattern
        which shall be used to build the shortName of the derived
        elements. As of now it is modeled as a String.  In general it
        should follow the pattern: pattern = (placeholder | namePart)*
        placeholder = "{" namePart "}" namePart = identifier | "_" This
        is subject to be refined in subsequent versions. Note that this
        is marked as obsolete. Use the xml attribute namePattern instead
        as it applies to Identifier and CIdentifier (shortName, symbol
        etc.)
    :ivar related_trace_item_ref: This contains a sloppy reference to
        the Autosar compatible identifier of the element (EcucId).
    :ivar ecuc_validation_conds: Collection of validation conditions
        which all need to evaluate to true in order to indicate a valid
        validation condition of the EcucDefinitionElement.
    :ivar ecuc_cond: If it evaluates to true the Ecu Parameter
        definition shall be processed as specified. Otherwise the
        parameter definition shall be ignored.
    :ivar lower_multiplicity: The lower multiplicity of the specified
        element. 0: optional 1: at least one occurrence n: at least n
        occurrences atpVariation: [RS_ECUC_00082]
    :ivar upper_multiplicity: The upper multiplicity of the specified
        element. 0: no occurrence (used for VSMD) 1: at most one
        occurrence m: at most m occurrences If upperMultiplicity is set
        than upperMultiplicityInfinite shall not be used. atpVariation:
        [RS_ECUC_00082]
    :ivar upper_multiplicity_infinite: To express an infinite number of
        occurrences of this element this attribute has to be set to
        true. If upperMultiplicityInfinite is set than upperMultiplicity
        shall not be used. atpVariation: [RS_ECUC_00082]
    :ivar scope: Specifies the scope of this configuration element.
    :ivar api_service_prefix: For CDD modules this attribute holds the
        apiServicePrefix. The shortName of the module definition of a
        Complex Driver is always "Cdd". Therefore for CDD modules the
        module apiServicePrefix is described with this attribute.
    :ivar post_build_variant_support: Indicates if a module supports
        different post-build variants (previously known as post-build
        selectable configuration sets). TRUE means yes, FALSE means no.
    :ivar refined_module_def_ref: Optional reference from the Vendor
        Specific Module Definition to the Standardized Module Definition
        it refines. In case this EcucModuleDef has the category
        STANDARDIZED_MODULE_DEFINITION this reference shall not be
        provided. In case this EcucModuleDef has the category
        VENDOR_SPECIFIC_MODULE_DEFINITION this reference is mandatory.
    :ivar supported_config_variants:
    :ivar containers: Aggregates the top-level container definitions of
        this specific module definition.
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
        name = "ECUC-MODULE-DEF"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["EcucModuleDef.ShortNameFragments"] = field(
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
    annotations: Optional["EcucModuleDef.Annotations"] = field(
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
    blueprint_policys: Optional["EcucModuleDef.BlueprintPolicys"] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    short_name_pattern: Optional[String] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    related_trace_item_ref: Optional[
        "EcucModuleDef.RelatedTraceItemRef"
    ] = field(
        default=None,
        metadata={
            "name": "RELATED-TRACE-ITEM-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecuc_validation_conds: Optional[
        "EcucModuleDef.EcucValidationConds"
    ] = field(
        default=None,
        metadata={
            "name": "ECUC-VALIDATION-CONDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecuc_cond: Optional[EcucConditionSpecification] = field(
        default=None,
        metadata={
            "name": "ECUC-COND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lower_multiplicity: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "LOWER-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_multiplicity: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "UPPER-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_multiplicity_infinite: Optional[BooleanValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "UPPER-MULTIPLICITY-INFINITE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    scope: Optional[EcucScopeEnum] = field(
        default=None,
        metadata={
            "name": "SCOPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    api_service_prefix: Optional[CIdentifier] = field(
        default=None,
        metadata={
            "name": "API-SERVICE-PREFIX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    post_build_variant_support: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "POST-BUILD-VARIANT-SUPPORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    refined_module_def_ref: Optional[
        "EcucModuleDef.RefinedModuleDefRef"
    ] = field(
        default=None,
        metadata={
            "name": "REFINED-MODULE-DEF-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    supported_config_variants: Optional[
        "EcucModuleDef.SupportedConfigVariants"
    ] = field(
        default=None,
        metadata={
            "name": "SUPPORTED-CONFIG-VARIANTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    containers: Optional["EcucModuleDef.Containers"] = field(
        default=None,
        metadata={
            "name": "CONTAINERS",
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
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class BlueprintPolicys:
        blueprint_policy_list: List[BlueprintPolicyList] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_not_modifiable: List[
            BlueprintPolicyNotModifiable
        ] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-NOT-MODIFIABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_single: List[BlueprintPolicySingle] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-SINGLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RelatedTraceItemRef(Ref):
        dest: Optional[TraceableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class EcucValidationConds:
        ecuc_validation_condition: List[EcucValidationCondition] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-VALIDATION-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RefinedModuleDefRef(Ref):
        dest: Optional[EcucModuleDefSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SupportedConfigVariants:
        """
        :ivar supported_config_variant: Specifies which
            ConfigurationVariants are supported by this software module.
            This attribute is optional if the EcucModuleDef has the
            category STANDARDIZED_MODULE_DEFINITION. If the category
            attribute of the EcucModuleDef is set to
            VENDOR_SPECIFIC_MODULE_DEFINITION then this attribute is
            mandatory.
        """

        supported_config_variant: List[EcucConfigurationVariantEnum] = field(
            default_factory=list,
            metadata={
                "name": "SUPPORTED-CONFIG-VARIANT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Containers:
        ecuc_choice_container_def: List[EcucChoiceContainerDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-CHOICE-CONTAINER-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_param_conf_container_def: List[EcucParamConfContainerDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-PARAM-CONF-CONTAINER-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
