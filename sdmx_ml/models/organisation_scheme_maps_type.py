from dataclasses import dataclass, field

from sdmx_ml.models.organisation_scheme_map_type import (
    OrganisationSchemeMapType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class OrganisationSchemeMapsType:
    """OrganisationSchemeMapsType describes the structure of the organisation
    scheme maps container.

    It contains one or more organisation scheme map, which can be
    explicitly detailed or referenced from an external structure
    document or registry service.

    :ivar organisation_scheme_map: OrganisationSchemeMap provides the
        details of a organisation scheme map, which descibes mappings
        between organisations in different schemes.
    """

    organisation_scheme_map: tuple[OrganisationSchemeMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrganisationSchemeMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
