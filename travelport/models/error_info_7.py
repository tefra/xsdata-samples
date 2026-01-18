from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_error_info_7 import TypeErrorInfo7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class ErrorInfo7(TypeErrorInfo7):
    """
    Container for error data when there is an application error.
    """

    class Meta:
        name = "ErrorInfo"
        namespace = "http://www.travelport.com/schema/common_v38_0"
