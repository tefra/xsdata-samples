from dataclasses import dataclass, field

from sdmx_ml.models.reporting_taxonomy_type import ReportingTaxonomyType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ReportingTaxonomiesType:
    """ReportingTaxonomiesType describes the structure of the reporting taxonomies
    container.

    It contains one or more reporting taxonomy, which can be explicitly
    detailed or referenced from an external structure document or
    registry service.

    :ivar reporting_taxonomy: ReportingTaxonomy provides the details of
        a reporting taxonomy, which is a scheme which defines the
        composition structure of a data report where each component can
        be described by an independent data or metadata flow definition.
    """

    reporting_taxonomy: tuple[ReportingTaxonomyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReportingTaxonomy",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
