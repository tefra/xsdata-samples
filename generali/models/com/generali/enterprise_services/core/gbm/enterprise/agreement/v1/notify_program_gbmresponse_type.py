from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmtype import BaseGbmtype

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"


@dataclass
class NotifyProgramGbmresponseType(BaseGbmtype):
    """
    <description xmlns="">The definition of the response message that supports
    retrieve of a agreement</description>
    """
    class Meta:
        name = "NotifyProgramGBMResponseType"

    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
            "required": True,
        }
    )
    error_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
        }
    )
