from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.query_result_type import QueryResultType
from sdmx_ml.models.status_message_type_2 import StatusMessageType2

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry"


@dataclass(frozen=True, kw_only=True)
class QueryRegistrationResponseType:
    """
    QueryRegistrationResponseType describes the structure of a registration
    query response.

    It provides a status for the request, and if successful, the resulting
    data and/or metadata results.

    :ivar status_message: StatusMessage provides that status for the
        registration query request, and if necessary, any error or
        warning information.
    :ivar query_result: QueryResult contains a result for a successful
        registration query. It can occur multiple times, for each
        registration the meets the conditions specified in the query.
    """

    status_message: StatusMessageType2 = field(
        metadata={
            "name": "StatusMessage",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry",
            "required": True,
        }
    )
    query_result: tuple[QueryResultType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "QueryResult",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry",
        },
    )
