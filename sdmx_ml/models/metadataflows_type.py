from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.metadataflow_type import MetadataflowType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class MetadataflowsType:
    """
    MetadataflowsType describes the structure of the metadata flows
    container.

    It contains one or more metadata flow, which can be explicitly detailed
    or referenced from an external structure document or registry service.

    :ivar metadataflow: Metadataflow provides the details of a metadata
        flow, which is defined as the structure of reference metadata
        that will be provided for different reference periods
    """

    metadataflow: tuple[MetadataflowType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Metadataflow",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
