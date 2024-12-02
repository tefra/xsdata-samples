from dataclasses import dataclass, field
from typing import Union

from sdmx_ml.models.item_type import (
    Agency,
    Category,
    Code,
    Concept,
    CustomType,
    DataConsumer,
    DataProvider,
    GeoFeatureSetCode,
    GeoGridCode,
    MetadataProvider,
    NamePersonalisation,
    OrganisationUnit,
    ReportingCategory,
    Ruleset,
    Transformation,
    UserDefinedOperator,
    VtlMapping,
)
from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ItemSchemeType(MaintainableType):
    """ItemSchemeType is an abstract base type for all item scheme objects.

    It contains a collection of items. Concrete instances of this type
    should restrict the actual types of items allowed within the scheme.

    :ivar choice:
    :ivar is_partial: The isPartial, if true, indicates that only the
        relevant portion of the item scheme is being communicated. This
        is used in cases where a codelist is returned for a data
        structure in the context of a constraint.
    """

    choice: tuple[
        Union[
            CustomType,
            UserDefinedOperator,
            Ruleset,
            NamePersonalisation,
            VtlMapping,
            Transformation,
            ReportingCategory,
            OrganisationUnit,
            MetadataProvider,
            DataProvider,
            DataConsumer,
            Agency,
            Concept,
            GeoGridCode,
            GeoFeatureSetCode,
            Code,
            Category,
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomType",
                    "type": CustomType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "UserDefinedOperator",
                    "type": UserDefinedOperator,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Ruleset",
                    "type": Ruleset,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "NamePersonalisation",
                    "type": NamePersonalisation,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "VtlMapping",
                    "type": VtlMapping,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Transformation",
                    "type": Transformation,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "ReportingCategory",
                    "type": ReportingCategory,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "OrganisationUnit",
                    "type": OrganisationUnit,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataProvider",
                    "type": MetadataProvider,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DataProvider",
                    "type": DataProvider,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DataConsumer",
                    "type": DataConsumer,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Agency",
                    "type": Agency,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Concept",
                    "type": Concept,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "GeoGridCode",
                    "type": GeoGridCode,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "GeoFeatureSetCode",
                    "type": GeoFeatureSetCode,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Code",
                    "type": Code,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Category",
                    "type": Category,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    is_partial: bool = field(
        default=False,
        metadata={
            "name": "isPartial",
            "type": "Attribute",
        },
    )
