from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmheader_type import (
    BaseGbmheaderType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.program_gbotype import (
    ProgramGbotype,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class NotifyProgramGbmrequestType(BaseGbmheaderType):
    """
    <description xmlns="">The definition of the message used to retrieve an
    agreement</description>.

    :ivar program_gbo: <description xmlns="">The business object to
        retrieve</description>
    """

    class Meta:
        name = "NotifyProgramGBMRequestType"

    program_gbo: ProgramGbotype = field(
        metadata={
            "name": "ProgramGBO",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/agreement/v1",
            "required": True,
        }
    )
