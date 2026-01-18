from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_error_info_6 import TypeErrorInfo6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class ErrorInfo6(TypeErrorInfo6):
    """
    Container for error data when there is an application error.
    """

    class Meta:
        name = "ErrorInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"
