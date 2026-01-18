from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmtype import (
    BaseGbmtype,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/technical/v1"


@dataclass
class TransmissionResponseType(BaseGbmtype):
    """
    <description xmlns="">The definition of the response message that
    supports retrieve of a agreement</description>.
    """

    status: str | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/technical/v1",
            "required": True,
        },
    )
    error_message: str | None = field(
        default=None,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/technical/v1",
        },
    )
