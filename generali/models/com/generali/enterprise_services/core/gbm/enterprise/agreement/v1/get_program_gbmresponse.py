from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.get_program_gbmresponse_type import GetProgramGbmresponseType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"


@dataclass
class GetProgramGbmresponse(GetProgramGbmresponseType):
    """
    <description xmlns="">The definition of the response message that supports
    retrieve of a program</description>
    """
    class Meta:
        name = "GetProgramGBMResponse"
        namespace = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"
