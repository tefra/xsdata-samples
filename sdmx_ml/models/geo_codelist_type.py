from dataclasses import dataclass, field

from sdmx_ml.models.geo_codelist_base_type import GeoCodelistBaseType
from sdmx_ml.models.geo_codelist_type_type import GeoCodelistTypeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GeoCodelistType(GeoCodelistBaseType):
    """
    GeoCodelistType is an abstract refinement of a codelist from which
    specific types of geographic codelists will be derived.

    :ivar geo_type: The type of geographic codelist. The will be refined
        and provided a fixed value in the specific geographic codelist
        type implementations.
    """

    geo_type: GeoCodelistTypeType | None = field(
        default=None,
        metadata={
            "name": "geoType",
            "type": "Attribute",
            "required": True,
        },
    )
