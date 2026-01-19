from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.geographic_codelist_type import GeographicCodelistType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class GeographicCodelistsType:
    """
    GeographicCodelistsType describes the structure of the geographic code
    lists container.

    It contains one or more geographic codelist, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar geographic_codelist: GeographiCodelist provides the details of
        a geographic codelists container, which comprises a set of
        GeoFeatureSetCodes, by adding a value in the Code that follows a
        pattern to represent a geo feature set.
    """

    geographic_codelist: tuple[GeographicCodelistType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "GeographicCodelist",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
