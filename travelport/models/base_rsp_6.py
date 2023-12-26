from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.response_message_6 import ResponseMessage6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class BaseRsp6:
    """
    The base type for all responses.

    Parameters
    ----------
    response_message
    trace_id
        Unique identifier for this atomic transaction traced by the user.
        Use is optional.
    transaction_id
        System generated unique identifier for this atomic transaction.
    response_time
        The time (in ms) the system spent processing this request, not
        including transmission times.
    command_history
        HTTP link to download command history and debugging information of
        the request that generated this response. Must be enabled on the
        system.
    """

    class Meta:
        name = "BaseRsp"

    response_message: list[ResponseMessage6] = field(
        default_factory=list,
        metadata={
            "name": "ResponseMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "max_occurs": 999,
        },
    )
    trace_id: None | str = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Attribute",
        },
    )
    transaction_id: None | str = field(
        default=None,
        metadata={
            "name": "TransactionId",
            "type": "Attribute",
        },
    )
    response_time: None | int = field(
        default=None,
        metadata={
            "name": "ResponseTime",
            "type": "Attribute",
        },
    )
    command_history: None | str = field(
        default=None,
        metadata={
            "name": "CommandHistory",
            "type": "Attribute",
        },
    )
