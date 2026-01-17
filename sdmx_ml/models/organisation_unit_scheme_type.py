from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.organisation_scheme_type import OrganisationSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class OrganisationUnitSchemeType(OrganisationSchemeType):
    """
    OrganisationUnitSchemeType defines a type of organisation scheme which
    simply defines organisations and there parent child relationships.

    Organisations in this scheme are assigned no particular role, and may
    in fact exist within the other type of organisation schemes as well.
    """

    choice_2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    choice_3: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
