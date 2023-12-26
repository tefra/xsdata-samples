from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_error_info_3 import TypeErrorInfo3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class ErrorInfo3(TypeErrorInfo3):
    """
    Container for error data when there is an application error.
    """

    class Meta:
        name = "ErrorInfo"
        namespace = "http://www.travelport.com/schema/common_v32_0"
