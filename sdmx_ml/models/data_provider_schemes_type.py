from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_provider_scheme_type import DataProviderSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class DataProviderSchemesType:
    """
    DataProviderSchemesType describes the structure of the data provider
    schemes container.

    It contains one or more data provider scheme, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar data_provider_scheme: DataProviderScheme provides the details
        of an data provider scheme, in which data providers are
        described.
    """

    data_provider_scheme: tuple[DataProviderSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataProviderScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
