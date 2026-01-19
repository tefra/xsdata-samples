from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.item_scheme_type import ItemSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class OrganisationSchemeBaseType(ItemSchemeType):
    """
    OrganisationSchemeBaseType is an abstract base type for any
    organisation scheme.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    version: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
