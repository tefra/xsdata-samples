from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.geo_codelist_type import GeoCodelistType
from sdmx_ml.models.geo_codelist_type_type import GeoCodelistTypeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GeoGridCodelistBaseType(GeoCodelistType):
    """
    GeoGridCodelistBaseType is the abstract base refinement for a geographic grid
    codelist.
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
        default=GeoCodelistTypeType.GEO_GRID_CODELIST,
        metadata={
            "name": "geoType",
            "type": "Attribute",
            "required": True,
        },
    )
