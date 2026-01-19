from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.item_type import (
    Agency,
    DataConsumer,
    DataProvider,
    MetadataProvider,
    OrganisationUnit,
)
from sdmx_ml.models.organisation_scheme_base_type import (
    OrganisationSchemeBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class OrganisationSchemeType(OrganisationSchemeBaseType):
    """
    OrganisationSchemeType describes the structure of an organisation
    scheme.
    """

    choice_1: tuple[
        OrganisationUnit
        | MetadataProvider
        | DataProvider
        | DataConsumer
        | Agency,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OrganisationUnit",
                    "type": OrganisationUnit,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "MetadataProvider",
                    "type": MetadataProvider,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "DataProvider",
                    "type": DataProvider,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "DataConsumer",
                    "type": DataConsumer,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "Agency",
                    "type": Agency,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
            ),
        },
    )
