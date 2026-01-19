from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.reporting_taxonomy_map_type import ReportingTaxonomyMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class ReportingTaxonomyMapsType:
    """
    ReportingTaxonomyMapsType describes the structure of the reporting
    taxonomy maps container.

    It contains one or reporting taxonomy map, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar reporting_taxonomy_map: ReportingTaxonomyMap provides the
        details of a reporting taxonomy map, which describes mappings
        between reporting taxonomies.
    """

    reporting_taxonomy_map: tuple[ReportingTaxonomyMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReportingTaxonomyMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
