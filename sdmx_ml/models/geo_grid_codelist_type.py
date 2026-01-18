from dataclasses import dataclass, field

from sdmx_ml.models.geo_grid_codelist_base_type import GeoGridCodelistBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GeoGridCodelistType(GeoGridCodelistBaseType):
    """
    GeoGridCodelistType defines the structure of a geographic grid code
    list.

    These define a geographical grid composed of cells representing regular
    squared portions of the Earth.

    :ivar grid_definition: Contains a regular expression string
        corresponding to the grid definition for the GeoGrid Codelist.
    """

    grid_definition: str | None = field(
        default=None,
        metadata={
            "name": "GridDefinition",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
