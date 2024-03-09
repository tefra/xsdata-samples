from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_error_info_1 import TypeErrorInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class ErrorInfo1(TypeErrorInfo1):
    """
    Container for error data when there is an application error.
    """

    class Meta:
        name = "ErrorInfo"
        namespace = "http://www.travelport.com/schema/common_v52_0"
