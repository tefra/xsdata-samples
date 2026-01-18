from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_error_info_2 import TypeErrorInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass(kw_only=True)
class ErrorInfo2(TypeErrorInfo2):
    """
    Container for error data when there is an application error.
    """

    class Meta:
        name = "ErrorInfo"
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"
