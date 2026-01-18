from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.metadata_provider_scheme_type import (
    MetadataProviderSchemeType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class MetadataProviderSchemesType:
    """
    MetadataProviderSchemesType describes the structure of the metadata
    provider schemes container.

    It contains one or more metadata provider scheme, which can be
    explicitly detailed or referenced from an external structure document
    or registry service.

    :ivar metadata_provider_scheme: MetadataProviderScheme provides the
        details of an metadata provider scheme, in which metadata
        providers are described.
    """

    metadata_provider_scheme: tuple[MetadataProviderSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataProviderScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
