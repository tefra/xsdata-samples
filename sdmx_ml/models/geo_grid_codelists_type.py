from dataclasses import dataclass, field

from sdmx_ml.models.geo_grid_codelist_type import GeoGridCodelistType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GeoGridCodelistsType:
    """GeoGridCodelistsType describes the structure of the codelists container.

    It contains one or more geographic grid codelist, which can be
    explicitly detailed or referenced from an external structure
    document or registry service.

    :ivar geo_grid_codelist: GeoGridCodelist provides the details of a
        geographic grid code list, which comprises a set of GridCodes,
        which are related to the gridDefinition specified in the
        GeoGridCodelist.
    """

    geo_grid_codelist: tuple[GeoGridCodelistType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "GeoGridCodelist",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
