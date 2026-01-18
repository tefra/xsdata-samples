from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class QuerySubscriptionRequestType:
    """
    QuerySubscriptionRequestType describes the structure of a query for
    subscriptions.

    Subscriptions for a given organisation may be retrieved.

    :ivar organisation: Organisation provides a reference to the data
        consumer for which the subscription details should be returned.
    """

    organisation: str | None = field(
        default=None,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
            "pattern": r".+\.base\.Agency=.+:AGENCIES\(.+\).+|.+\.base\.DataConsumer=.+:DATA_CONSUMERS\(.+\).+|.+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+|.+\.base\.MetadataProvider=.+:METADATA_PROVIDERS\(.+\).+|.+\.base\.OrganisationUnit=.+",
        },
    )
