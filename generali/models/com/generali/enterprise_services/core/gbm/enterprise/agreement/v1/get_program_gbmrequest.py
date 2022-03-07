from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.get_program_gbmrequest_type import GetProgramGbmrequestType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"


@dataclass
class GetProgramGbmrequest(GetProgramGbmrequestType):
    """
    <description xmlns="">The definition of the request message that supports
    retrieval of a agreement</description>
    """
    class Meta:
        name = "GetProgramGBMRequest"
        namespace = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"
