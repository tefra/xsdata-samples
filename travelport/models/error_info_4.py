from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_error_info_4 import TypeErrorInfo4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class ErrorInfo4(TypeErrorInfo4):
    """
    Container for error data when there is an application error.
    """
    class Meta:
        name = "ErrorInfo"
        namespace = "http://www.travelport.com/schema/common_v33_0"
