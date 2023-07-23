from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.auxdata_5 import Auxdata5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class TypeErrorInfo5:
    """
    Container for error data when there is an application error.
    """
    class Meta:
        name = "typeErrorInfo"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "required": True,
        }
    )
    service: None | str = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "required": True,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "required": True,
        }
    )
    transaction_id: None | str = field(
        default=None,
        metadata={
            "name": "TransactionId",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "required": True,
        }
    )
    trace_id: None | str = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    command_history: None | str = field(
        default=None,
        metadata={
            "name": "CommandHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    auxdata: None | Auxdata5 = field(
        default=None,
        metadata={
            "name": "Auxdata",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    stack_trace: None | str = field(
        default=None,
        metadata={
            "name": "StackTrace",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
