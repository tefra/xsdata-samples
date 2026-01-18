from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_consumer_scheme_type import DataConsumerSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataConsumerSchemesType:
    """
    DataConsumerSchemesType describes the structure of the data consumer
    schemes container.

    It contains one or more data consumer scheme, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar data_consumer_scheme: DataConsumerScheme provides the details
        of an data consumer scheme, in which data consumers are
        described.
    """

    data_consumer_scheme: tuple[DataConsumerSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataConsumerScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
