from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.organisation_unit_scheme_type import (
    OrganisationUnitSchemeType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class OrganisationUnitSchemesType:
    """
    OrganisationUnitSchemesType describes the structure of the organisation
    unit schemes container.

    It contains one or more organisation unit scheme, which can be
    explicitly detailed or referenced from an external structure document
    or registry service.

    :ivar organisation_unit_scheme: OrganisationUnitScheme provides the
        details of an organisation unit scheme, in which organisation
        units are described.
    """

    organisation_unit_scheme: tuple[OrganisationUnitSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrganisationUnitScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
