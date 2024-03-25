from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.organisation_scheme_type import OrganisationSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataConsumerSchemeType(OrganisationSchemeType):
    """DataConsumerSchemeType defines a type of organisation scheme which contains
    only data consumers.

    The data consumer scheme maintained by a particular maintenance
    agency is always provided a fixed identifier and is never versioned.
    Therefore, consumers can be added or removed without have to version
    the scheme. This scheme has no hierarchy, meaning that no
    organisation may define a relationship with another organisation in
    the scheme.
    """

    choice_2: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    choice_3: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    id: str = field(
        init=False,
        default="DATA_CONSUMERS",
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
