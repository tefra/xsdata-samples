from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.organisation_scheme_map_type import (
    OrganisationSchemeMapType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class OrganisationSchemeMapsType:
    """
    OrganisationSchemeMapsType describes the structure of the organisation
    scheme maps container.

    It contains one or more organisation scheme map, which can be
    explicitly detailed or referenced from an external structure document
    or registry service.

    :ivar organisation_scheme_map: OrganisationSchemeMap provides the
        details of an organisation scheme map, which describes mappings
        between organisations in different schemes.
    """

    organisation_scheme_map: tuple[OrganisationSchemeMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrganisationSchemeMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
