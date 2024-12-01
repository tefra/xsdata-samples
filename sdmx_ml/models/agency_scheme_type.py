from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.organisation_scheme_type import OrganisationSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class AgencySchemeType(OrganisationSchemeType):
    """AgencySchemeType defines a specific type of organisation scheme which
    contains only maintenance agencies.

    The agency scheme maintained by a particular maintenance agency is
    always provided a fixed identifier and is never versioned.
    Therefore, agencies can be added or removed without have to version
    the scheme. Agencies schemes have no hierarchy, meaning that no
    agency may define a relationship with another agency in the scheme.
    In fact, the actual parent agency for an agency in a scheme is the
    agency which defines the scheme.
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
    id: str = field(
        init=False,
        default="AGENCIES",
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
