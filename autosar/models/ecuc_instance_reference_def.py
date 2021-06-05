from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.boolean import Boolean
from autosar.models.boolean_value_variation_point import BooleanValueVariationPoint
from autosar.models.category_string import CategoryString
from autosar.models.ecuc_condition_specification import EcucConditionSpecification
from autosar.models.ecuc_configuration_class_affection import EcucConfigurationClassAffection
from autosar.models.ecuc_implementation_configuration_class import EcucImplementationConfigurationClass
from autosar.models.ecuc_multiplicity_configuration_class import EcucMultiplicityConfigurationClass
from autosar.models.ecuc_scope_enum import EcucScopeEnum
from autosar.models.ecuc_validation_condition import EcucValidationCondition
from autosar.models.ecuc_value_configuration_class import EcucValueConfigurationClass
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.positive_integer_value_variation_point import PositiveIntegerValueVariationPoint
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.string import String
from autosar.models.traceable_subtypes_enum import TraceableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucInstanceReferenceDef:
    """
    Specify a reference to an XML description of an entity described in another
    AUTOSAR template using the INSTANCE REFERENCE semantics.

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
    :ivar configuration_class_affection: Specifies whether changes on
        this parameter have some affection on other parameters.
    :ivar implementation_config_classes: Specifies in which
        ConfigurationClass this parameter or reference is available for
        which ConfigurationVariant. This aggregation is optional if the
        surrounding EcucModuleDef has the category
        STANDARDIZED_MODULE_DEFINITION. If the category attribute of the
        EcucModuleDef is set to VENDOR_SPECIFIC_MODULE_DEFINITION then
        this aggregation is mandatory.
    :ivar multiplicity_config_classes: Specifies in which
        MultiplicityConfigurationClass this parameter or reference is
        available in a particular ConfigurationVariant. This aggregation
        is optional if the surrounding EcucModuleDef has the Category
        STANDARDIZED_MODULE_DEFINITION. If the category attribute of the
        EcucModuleDef is set to VENDOR_SPECIFIC_MODULE_DEFINITION, then
        this aggregation is mandatory.
    :ivar origin: String specifying if this configuration parameter is
        an AUTOSAR standardized configuration parameter or if the
        parameter is hardware- or vendor-specific.
    :ivar post_build_variant_multiplicity: Indicates if a parameter or a
        reference may have different number of instances in different
        post-build variants (previously known as post-build selectable
        configuration sets). TRUE means yes, FALSE means no.
    :ivar post_build_variant_value: Indicates if a parameter or a
        reference may have different value in different post-build
        variants (previously known as post-build selectable
        configuration sets). TRUE means yes, FALSE means no.
    :ivar requires_index: Used to define whether the value element for
        this definition shall be provided with an index.
    :ivar value_config_classes: Specifies in which
        ValueConfigurationClass this parameter or reference is available
        in a particular ConfigurationVariant. This aggregation is
        optional if the surrounding EcucModuleDef has the Category
        STANDARDIZED_MODULE_DEFINITION. If the category attribute of the
        EcucModuleDef is set to VENDOR_SPECIFIC_MODULE_DEFINITION, then
        this aggregation is mandatory.
    :ivar destination_context: The context in the AUTOSAR Metamodel to
        which' this reference is allowed to point to.
    :ivar destination_type: The type in the AUTOSAR Metamodel to which'
        instance this reference is allowed to point to.
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
        name = "ECUC-INSTANCE-REFERENCE-DEF"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["EcucInstanceReferenceDef.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["EcucInstanceReferenceDef.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    related_trace_item_ref: Optional["EcucInstanceReferenceDef.RelatedTraceItemRef"] = field(
        default=None,
        metadata={
            "name": "RELATED-TRACE-ITEM-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ecuc_validation_conds: Optional["EcucInstanceReferenceDef.EcucValidationConds"] = field(
        default=None,
        metadata={
            "name": "ECUC-VALIDATION-CONDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ecuc_cond: Optional[EcucConditionSpecification] = field(
        default=None,
        metadata={
            "name": "ECUC-COND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    lower_multiplicity: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "LOWER-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    upper_multiplicity: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "UPPER-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    upper_multiplicity_infinite: Optional[BooleanValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "UPPER-MULTIPLICITY-INFINITE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    scope: Optional[EcucScopeEnum] = field(
        default=None,
        metadata={
            "name": "SCOPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    configuration_class_affection: Optional[EcucConfigurationClassAffection] = field(
        default=None,
        metadata={
            "name": "CONFIGURATION-CLASS-AFFECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    implementation_config_classes: Optional["EcucInstanceReferenceDef.ImplementationConfigClasses"] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-CONFIG-CLASSES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    multiplicity_config_classes: Optional["EcucInstanceReferenceDef.MultiplicityConfigClasses"] = field(
        default=None,
        metadata={
            "name": "MULTIPLICITY-CONFIG-CLASSES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    origin: Optional[String] = field(
        default=None,
        metadata={
            "name": "ORIGIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    post_build_variant_multiplicity: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "POST-BUILD-VARIANT-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    post_build_variant_value: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "POST-BUILD-VARIANT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    requires_index: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "REQUIRES-INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    value_config_classes: Optional["EcucInstanceReferenceDef.ValueConfigClasses"] = field(
        default=None,
        metadata={
            "name": "VALUE-CONFIG-CLASSES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    destination_context: Optional[String] = field(
        default=None,
        metadata={
            "name": "DESTINATION-CONTEXT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    destination_type: Optional[String] = field(
        default=None,
        metadata={
            "name": "DESTINATION-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class RelatedTraceItemRef(Ref):
        dest: Optional[TraceableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class EcucValidationConds:
        ecuc_validation_condition: List[EcucValidationCondition] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-VALIDATION-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ImplementationConfigClasses:
        ecuc_implementation_configuration_class: List[EcucImplementationConfigurationClass] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-IMPLEMENTATION-CONFIGURATION-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class MultiplicityConfigClasses:
        ecuc_multiplicity_configuration_class: List[EcucMultiplicityConfigurationClass] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-MULTIPLICITY-CONFIGURATION-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ValueConfigClasses:
        ecuc_value_configuration_class: List[EcucValueConfigurationClass] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-VALUE-CONFIGURATION-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
