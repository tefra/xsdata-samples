from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.program_req_app_data_type import ProgramReqAppDataType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmtype import BaseGbmtype
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbotype import BaseGbotype

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"


@dataclass
class GetProgramGbmrequestType(BaseGbmtype):
    """
    <description xmlns="">The definition of the message used to retrieve an
    agreement</description>

    :ivar app_data: A component of the GBM that allows application
        specific or pre-processing information to be added.
    :ivar program_gbo: <description xmlns="">The business object to
        retrieve</description>
    """
    class Meta:
        name = "GetProgramGBMRequestType"

    app_data: Optional[ProgramReqAppDataType] = field(
        default=None,
        metadata={
            "name": "AppData",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
        }
    )
    program_gbo: Optional[BaseGbotype] = field(
        default=None,
        metadata={
            "name": "ProgramGBO",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
            "required": True,
        }
    )
