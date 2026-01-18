from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbm.enterprise.agreement.v1.program_resp_app_data_type import (
    ProgramRespAppDataType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmtype import (
    BaseGbmtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.program_gbotype import (
    ProgramGbotype,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"
)


@dataclass
class GetProgramGbmresponseType(BaseGbmtype):
    """
    <description xmlns="">The definition of the response message that
    supports retrieve of a agreement</description>.

    :ivar app_data: A component of the GBM that allows application
        specific or pre-processing information to be added.
    :ivar program_gbo: <description xmlns="">The business object to
        retrieve</description>
    """

    class Meta:
        name = "GetProgramGBMResponseType"

    app_data: ProgramRespAppDataType | None = field(
        default=None,
        metadata={
            "name": "AppData",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
        },
    )
    program_gbo: ProgramGbotype | None = field(
        default=None,
        metadata={
            "name": "ProgramGBO",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
            "required": True,
        },
    )
