from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.vtl_mapping_scheme_type import VtlMappingSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class VtlMappingSchemesType:
    """
    VtlMappingSchemesType describes the structure of the VTL mappings
    schemes container.

    It contains one or more VTL mapping schemes, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar vtl_mapping_scheme: VtlMappingScheme provides the details of a
        VTL mapping scheme, in which VTL mappings are described.
    """

    vtl_mapping_scheme: tuple[VtlMappingSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "VtlMappingScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
