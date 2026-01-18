from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbm.technical.v1.payload_type import (
    PayloadType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmheader_type import (
    BaseGbmheaderType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/technical/v1"


@dataclass
class TransmissionRequestType(BaseGbmheaderType):
    """
    <description xmlns="">The definition of the message used to retrieve an
    agreement</description>.

    :ivar payload: <description xmlns="">The business object to
        retrieve</description>
    """

    payload: PayloadType | None = field(
        default=None,
        metadata={
            "name": "Payload",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/technical/v1",
            "required": True,
        },
    )
