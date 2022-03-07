from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.notify_program_gbmrequest_type import NotifyProgramGbmrequestType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"


@dataclass
class NotifyProgramGbmrequest(NotifyProgramGbmrequestType):
    """
    <description xmlns="">The definition of the request message that supports
    retrieval of a agreement</description>
    """
    class Meta:
        name = "NotifyProgramGBMRequest"
        namespace = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"
