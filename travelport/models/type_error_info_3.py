from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.auxdata_3 import Auxdata3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class TypeErrorInfo3:
    """
    Container for error data when there is an application error.
    """

    class Meta:
        name = "typeErrorInfo"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "required": True,
        }
    )
    service: str = field(
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "required": True,
        }
    )
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "required": True,
        }
    )
    transaction_id: str = field(
        metadata={
            "name": "TransactionId",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "required": True,
        }
    )
    trace_id: None | str = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    command_history: None | str = field(
        default=None,
        metadata={
            "name": "CommandHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    auxdata: None | Auxdata3 = field(
        default=None,
        metadata={
            "name": "Auxdata",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    stack_trace: None | str = field(
        default=None,
        metadata={
            "name": "StackTrace",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
