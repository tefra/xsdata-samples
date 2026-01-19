from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


class GeoCodelistTypeType(Enum):
    """
    GeoCodelistTypeType defines an enumeration of the specific types of
    geographic codelists.
    """

    GEOGRAPHIC_CODELIST = "GeographicCodelist"
    GEO_GRID_CODELIST = "GeoGridCodelist"
