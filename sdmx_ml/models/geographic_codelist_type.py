from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.geo_codelist_type import GeoCodelistType
from sdmx_ml.models.geo_codelist_type_type import GeoCodelistTypeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class GeographicCodelistType(GeoCodelistType):
    """
    GeographicCodelistType defines the structure of a geographic codelist.

    It comprises a set of GeoFeatureSetCodes, by adding a value in the Code
    that follows a pattern to represent a geo feature set.
    """

    choice_3: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    geo_type: GeoCodelistTypeType = field(
        init=False,
        default=GeoCodelistTypeType.GEOGRAPHIC_CODELIST,
        metadata={
            "name": "geoType",
            "type": "Attribute",
            "required": True,
        },
    )
