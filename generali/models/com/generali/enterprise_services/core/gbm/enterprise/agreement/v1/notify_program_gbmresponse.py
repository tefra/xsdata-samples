from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.notify_program_gbmresponse_type import (
    NotifyProgramGbmresponseType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"
)


@dataclass
class NotifyProgramGbmresponse(NotifyProgramGbmresponseType):
    """
    <description xmlns="">The definition of the response message that supports
    retrieve of a program</description>
    """

    class Meta:
        name = "NotifyProgramGBMResponse"
        namespace = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"
