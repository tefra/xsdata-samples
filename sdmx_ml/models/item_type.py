from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ForwardRef

from sdmx_ml.models.concept_representation import ConceptRepresentation
from sdmx_ml.models.contact_type_1 import ContactType1
from sdmx_ml.models.empty_type import EmptyType
from sdmx_ml.models.from_vtl_mapping_type import FromVtlMappingType
from sdmx_ml.models.isoconcept_reference_type import IsoconceptReferenceType
from sdmx_ml.models.item_base_type import ItemBaseType
from sdmx_ml.models.simple_data_type import SimpleDataType
from sdmx_ml.models.to_vtl_mapping_type import ToVtlMappingType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class ItemType(ItemBaseType):
    """
    ItemType is an abstract base type for all items with in an item scheme.

    Concrete instances of this type may or may not utilize the nested item,
    but if so should restrict the actual types of item allowed.
    """

    choice: tuple[
        str
        | CustomType
        | UserDefinedOperator
        | Ruleset
        | NamePersonalisation
        | VtlMapping
        | Transformation
        | ReportingCategory
        | OrganisationUnit
        | MetadataProvider
        | DataProvider
        | DataConsumer
        | Agency
        | Concept
        | GeoGridCode
        | GeoFeatureSetCode
        | Code
        | Category,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Parent",
                    "type": str,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                    "pattern": r"[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*",
                },
                {
                    "name": "CustomType",
                    "type": ForwardRef("CustomType"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "UserDefinedOperator",
                    "type": ForwardRef("UserDefinedOperator"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Ruleset",
                    "type": ForwardRef("Ruleset"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "NamePersonalisation",
                    "type": ForwardRef("NamePersonalisation"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "VtlMapping",
                    "type": ForwardRef("VtlMapping"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Transformation",
                    "type": ForwardRef("Transformation"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "ReportingCategory",
                    "type": ForwardRef("ReportingCategory"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "OrganisationUnit",
                    "type": ForwardRef("OrganisationUnit"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataProvider",
                    "type": ForwardRef("MetadataProvider"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DataProvider",
                    "type": ForwardRef("DataProvider"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DataConsumer",
                    "type": ForwardRef("DataConsumer"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Agency",
                    "type": ForwardRef("Agency"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Concept",
                    "type": ForwardRef("Concept"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "GeoGridCode",
                    "type": ForwardRef("GeoGridCode"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "GeoFeatureSetCode",
                    "type": ForwardRef("GeoFeatureSetCode"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Category",
                    "type": ForwardRef("Category"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )


@dataclass(frozen=True, kw_only=True)
class BaseOrganisationType(ItemType):
    """
    BaseOrganisationType is an abstract base type the forms the basis for
    the OrganisationType.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class CategoryType(ItemType):
    """
    CategoryType describes the details of a category.

    A category is defined as an item at any level in a classification. The
    Category element represents a set of nested categories which are child
    categories.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class CodeType(ItemType):
    """
    CodeType describes the structure of a code.

    A code is defined as a language independent set of letters, numbers or
    symbols that represent a concept whose meaning is described in a
    natural language. Presentational information not present may be added
    through the use of annotations.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class ConceptBaseType(ItemType):
    """
    ConceptBaseType is an abstract base type the forms the basis of the
    ConceptType by requiring a name and id, and restricting the content of
    the id.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class ReportingCategoryBaseType(ItemType):
    """
    ReportingCategoryBaseType is an abstract base type that serves as the
    basis for the ReportingCategoryType.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class UnnestedItemType(ItemType):
    """
    UnnestedItemType is an abstract base type for all items with in an item
    scheme that do not contain nested items.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class Category(CategoryType):
    """
    Category represents a set of nested categories which describe a simple
    classification hierarchy.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class Code(CodeType):
    """
    Code describes a code in a codelist.

    In addition to the identification and description of the code, basic
    presentational information is also available. Presentational
    information not present may be added through the use of annotations.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class ConceptType(ConceptBaseType):
    """
    ConceptType describes the details of a concept.

    A concept is defined as a unit of knowledge created by a unique
    combination of characteristics. If a concept does not specify a
    TextFormat or a core representation, then the representation of the
    concept is assumed to be represented by any set of valid characters
    (corresponding to the xs:string datatype of W3C XML Schema).

    :ivar core_representation:
    :ivar isoconcept_reference: Provides a reference to an ISO 11179
        concept.
    """

    core_representation: None | ConceptRepresentation = field(
        default=None,
        metadata={
            "name": "CoreRepresentation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    isoconcept_reference: None | IsoconceptReferenceType = field(
        default=None,
        metadata={
            "name": "ISOConceptReference",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )


@dataclass(frozen=True, kw_only=True)
class CustomTypeBaseType(UnnestedItemType):
    """
    CustomTypeBaseType defines the base refinement of the CustomTypeType.

    Its purpose is to retrict the urn attribute.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class GeoRefCodeType(CodeType):
    """
    GeoRefCodeType is the abstract base type defining the structure of
    geographic codes.
    """


@dataclass(frozen=True, kw_only=True)
class NamePersonalisationBaseType(UnnestedItemType):
    """
    NamePersonalisationBaseType defines the base refinement of the
    NamePersonalisationType.

    Its purpose is to retrict the urn attribute.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class OrganisationType(BaseOrganisationType):
    """
    OrganisationType in an abstract type which describes the structure of
    the details of an organisation.

    In addition to the basic organisation identification, contact details
    can be provided.

    :ivar contact: Contact describes a contact for the organisation,
    """

    contact: tuple[ContactType1, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )


@dataclass(frozen=True, kw_only=True)
class ReportingCategoryType(ReportingCategoryBaseType):
    """
    ReportingCategoryType describes the structure of a reporting category,
    which groups structure usages into useful sub-packages.

    Sub ordinate reporting categories can be nested within the category
    definition.
    """

    structural_metadata_or_provisioning_metadata: tuple[
        ReportingCategoryType.StructuralMetadata
        | ReportingCategoryType.ProvisioningMetadata,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StructuralMetadata",
                    "type": ForwardRef(
                        "ReportingCategoryType.StructuralMetadata"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "ProvisioningMetadata",
                    "type": ForwardRef(
                        "ReportingCategoryType.ProvisioningMetadata"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )

    @dataclass(frozen=True, kw_only=True)
    class StructuralMetadata:
        value: str = field(
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.DataStructure=.+|.+\.metadatastructure\.MetadataStructure=.+",
            }
        )

    @dataclass(frozen=True, kw_only=True)
    class ProvisioningMetadata:
        value: str = field(
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.Dataflow=.+|.+\.metadatastructure\.Metadataflow=.+",
            }
        )


@dataclass(frozen=True, kw_only=True)
class RulesetBaseType(UnnestedItemType):
    """
    RulesetBaseType defines the base refinement of the RulesetType.

    Its purpose is to retrict the urn attribute.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class TransformationBaseType(UnnestedItemType):
    """
    TransformationBaseType defines the base refinement of the
    TransformationType.

    Its purpose is to retrict the urn attribute.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class UserDefinedOperatorBaseType(UnnestedItemType):
    """
    UserDefinedOperatorBaseType defines the base refinement of the
    UserDefinedOperatorType.

    Its purpose is to retrict the urn attribute.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class VtlMappingBaseType(UnnestedItemType):
    """
    VtlMappingBaseType defines the base refinement of the VtlMappingType.

    Its purpose is to retrict the urn attribute.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class AgencyType(OrganisationType):
    """
    AgencyType defines the structure of an agency description.

    The contacts defined for the organisation are specific to the agency
    role the organisation is serving.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class Concept(ConceptType):
    """
    Concept describes the details of a concept within a concept scheme.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class CustomTypeType(CustomTypeBaseType):
    """
    CustomTypeType defines the structure of a custom type.

    A custom type specifies a custom conversion for a VTL scalar type to a
    resulting data type. This conversion overrides the default conversion.

    :ivar vtl_scalar_type: Identifies the VTL scalar type that is to be
        converted to an resulting output data type.
    :ivar data_type: Identifies the resulting output data type the VTL
        scalar type is to be converted to. If this is an SDMX data type,
        it must use the proper SimpleDataType enumeration value. For all
        other data types, a string value can be used to identify the
        type.
    :ivar vtl_literal_format: The format in which the literals of the
        VTL scalar type are expressed in the transformations. This is
        only needed if the format is different than the output format
        expressed by means of the VTL type.
    :ivar output_format: The format the VTL scalar type has to assume
        (e.g. YYYY-MM-DD; see VTL specifications), both for the literals
        in the VTL expressions and for the conversion to the output.
    :ivar null_value: The value to be produced in the output of the
        conversion when a component has a null value.
    """

    vtl_scalar_type: str = field(
        metadata={
            "name": "VtlScalarType",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )
    data_type: SimpleDataType | str = field(
        metadata={
            "name": "DataType",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )
    vtl_literal_format: None | str = field(
        default=None,
        metadata={
            "name": "VtlLiteralFormat",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    output_format: None | str = field(
        default=None,
        metadata={
            "name": "OutputFormat",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    null_value: None | str = field(
        default=None,
        metadata={
            "name": "NullValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )


@dataclass(frozen=True, kw_only=True)
class DataConsumerType(OrganisationType):
    """
    DataConsumerType defines the structure of a data consumer description.

    The contacts defined for the organisation are specific to the data
    consumer role the organisation is serving.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class DataProviderType(OrganisationType):
    """
    DataProviderType defines the structure of a data provider description.

    The contacts defined for the organisation are specific to the data
    provider role the organisation is serving.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class GeoFeatureSetCodeType(GeoRefCodeType):
    """
    GeoFeatureSetCodeType defines the structure of a geogrphic code.

    :ivar value: The geo feature set of the Code, which represents a set
        of points defining a feature in a format defined a predefined
        pattern (see section 6).
    """

    value: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class GeoGridCodeType(GeoRefCodeType):
    """
    GeoGridCodeType defines the structure of a geographic grid cell.

    :ivar geo_cell: The value used to assign the Code to one cell in the
        grid.
    """

    geo_cell: str = field(
        metadata={
            "name": "GeoCell",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class MetadataProviderType(OrganisationType):
    """
    MetadataProviderType defines the structure of a metadata provider
    description.

    The contacts defined for the organisation are specific to the metadata
    provider role the organisation is serving.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class NamePersonalisationType(NamePersonalisationBaseType):
    """
    NamePersonalisationType defines the structure of a name
    personalisation.

    A name personalisation is is used in place of a standard VTL name in
    some VTL operations.

    :ivar vtl_default_name: Provides the VTL standard name that is being
        personalised.
    :ivar personalised_name: Provides the personalised name that is used
        in place of the VTL standard name in the transformation
        expressions.
    :ivar vtl_artefact: Identifies the type of VTL model artefact that
        is being personalised. In VTL 2.0, this is valuedomain or
        variable.
    """

    vtl_default_name: str = field(
        metadata={
            "name": "VtlDefaultName",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )
    personalised_name: str = field(
        metadata={
            "name": "PersonalisedName",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )
    vtl_artefact: str = field(
        metadata={
            "name": "vtlArtefact",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class OrganisationUnitType(OrganisationType):
    """
    OrganisationUnitType defines the structure of an organisation unit
    description.

    In addition to general identification and contact information, an
    organisation unit can specify a relationship with another organisation
    unit from the same scheme which is its parent organisation.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(frozen=True, kw_only=True)
class ReportingCategory(ReportingCategoryType):
    """
    ReportingCateogry defines a reporting category, which is used to group
    structure usages into useful sub-packages.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class RulesetType(RulesetBaseType):
    """
    RulesetType defines the structure of a ruleset.

    A ruleset is a persistent set of rules which can be invoked by using
    appropriate VTL operators.

    :ivar ruleset_definition: A VTL statement for the definition of a
        ruleset. This must conform to the syntax of the VTL definition
        language.
    :ivar ruleset_type: The VTL type of the ruleset. In VTL 2.0, this is
        datapoint or hierarchical
    :ivar ruleset_scope: This model artefact on which the ruleset is
        defined. In VTL 2.0, this is value domain or variable.
    """

    ruleset_definition: str = field(
        metadata={
            "name": "RulesetDefinition",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )
    ruleset_type: str = field(
        metadata={
            "name": "rulesetType",
            "type": "Attribute",
            "required": True,
        }
    )
    ruleset_scope: str = field(
        metadata={
            "name": "rulesetScope",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class TransformationType(TransformationBaseType):
    """
    TransformationType defines the structure of a transformation.

    A transformation is an assignment of a VTL expression to a specific
    result.

    :ivar expression: The right-hand side of the VTL statement. This is
        expression that is executed for this transformation. It include
        references to operands and other artefacts. The expression may
        contain references to SDMX artefacts using the reduced URN
        format; see Section 6 SDMX Standards ("SDMX Technical Notes"),
        10.2.3 ("Abbreviation of the URN").
    :ivar result: The left-hand side of the VTL statement. This
        identifies the result artefact, which may be used in subsequent
        transformations. If the result is an SDMX artefact, the is
        expressed using the alias; see Section 6 SDMX Standards ("SDMX
        Technical Notes"), 10.2.3 ("Abbreviation of the URN").
    :ivar is_persistent: Indicates if the the result is permanently
        stored. A persistent result (value of true) can be used by
        transformation defined in other transformation schemes, but a
        non-persistent result (value of false) can only be used by
        transformations within the same transformation scheme.
    """

    expression: str = field(
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )
    result: str = field(
        metadata={
            "name": "Result",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )
    is_persistent: bool = field(
        metadata={
            "name": "isPersistent",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class UserDefinedOperatorType(UserDefinedOperatorBaseType):
    """
    UserDefinedOperatorType defines the structure of a user defined
    operator.

    A user defined operator is a custom VTL operator (not existing in the
    standard library) that extends the VTL standard library for specific
    purposes. In addition to its identification and name, and definition of
    the operator must be provided.

    :ivar operator_definition: A VTL statement for the definition of a
        new operator: it specifies the operator name, its parameters and
        their data types, the VTL expression that defines its behaviour.
    """

    operator_definition: str = field(
        metadata={
            "name": "OperatorDefinition",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class VtlMappingType(VtlMappingBaseType):
    """
    VtlMappingType defines the structure of a single mapping between the
    reference to a SDMX artefact made from VTL transformations, rulesets,
    user defined operators and the corresponding SDMX structure identifier.

    These are used to assign an alternative names to SDMX Dataflows,
    Codelists, Concept Schemes, or Concepts. Although are distinct
    sub-classes in the Information Model, this structure serves to express
    them all. The references SDMX artefact serves to distinguish which type
    of sub-class (VtlDatflowMapping or VtlCodelistMapping, or
    VtlConceptMapping) is being described. When this is used to assign an
    alias for a SDMX Dataflow, this can also be used to indicate the
    methods used to convert the data structure from SDMX to VTL and
    vice-versa. Finally, this can be used to override the deault Basic
    mapping methods used for Dataflows by utilizing the GenericDataflow
    element in place of a reference to a specific Dataflow.

    :ivar choice_1:
    :ivar alias: The alias used to refer to the reference SDMX artefact
        in the transformations. This must be unique within the mapping
        scheme in which it is defined.
    """

    choice_1: tuple[
        VtlMappingType.Dataflow
        | EmptyType
        | ToVtlMappingType
        | FromVtlMappingType
        | VtlMappingType.Codelist
        | VtlMappingType.Concept,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Dataflow",
                    "type": ForwardRef("VtlMappingType.Dataflow"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "GenericDataflow",
                    "type": EmptyType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "ToVtlMapping",
                    "type": ToVtlMappingType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "FromVtlMapping",
                    "type": FromVtlMappingType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Codelist",
                    "type": ForwardRef("VtlMappingType.Codelist"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Concept",
                    "type": ForwardRef("VtlMappingType.Concept"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
            "max_occurs": 3,
        },
    )
    alias: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(frozen=True, kw_only=True)
    class Dataflow:
        value: str = field(
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.Dataflow=.+",
            }
        )

    @dataclass(frozen=True, kw_only=True)
    class Codelist:
        value: str = field(
            metadata={
                "required": True,
                "pattern": r".+\.codelist\.Codelist=.+",
            }
        )

    @dataclass(frozen=True, kw_only=True)
    class Concept:
        value: str = field(
            metadata={
                "required": True,
                "pattern": r".+\.conceptscheme\.Concept=.+",
            }
        )


@dataclass(frozen=True, kw_only=True)
class Agency(AgencyType):
    """
    Agency is an organisation which maintains structural metadata such as
    classifications, concepts, data structures, and metadata structures.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class CustomType(CustomTypeType):
    """
    CustomType details a custom type within a custom type scheme.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class DataConsumer(DataConsumerType):
    """
    DataConsumer describes an organisation using data as input for further
    processing.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class DataProvider(DataProviderType):
    """
    DataProvider describes an organisation that produces data.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class GeoFeatureSetCode(GeoFeatureSetCodeType):
    """
    Is a geographic code in a geographic codelist.

    It adds a value to a code that folows a pattern to represent a geo
    feature set.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class GeoGridCode(GeoGridCodeType):
    """
    GeoGridCode is a code the represents a geographic grid cell that
    belongs to a specific grid definition.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class MetadataProvider(MetadataProviderType):
    """
    MetadataProvider describes an organisation that produces metadata .
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class NamePersonalisation(NamePersonalisationType):
    """
    NamePersonalisation details a name personalisation that is used in a
    transformation.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class OrganisationUnit(OrganisationUnitType):
    """
    OrganisationUnit describes a generic organisation, which serves not
    predefined role in SDMX.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class Ruleset(RulesetType):
    """
    Ruleset details a ruleset within a ruleset scheme.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class Transformation(TransformationType):
    """
    Transformation describes the details of a single transformation within
    a transformation scheme.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class UserDefinedOperator(UserDefinedOperatorType):
    """
    UserDefinedOperator details a user defined operators within a user
    defined operator scheme.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )


@dataclass(frozen=True, kw_only=True)
class VtlMapping(VtlMappingType):
    """
    VtlMapping details a mapping between SDMX and VTL transformation.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
