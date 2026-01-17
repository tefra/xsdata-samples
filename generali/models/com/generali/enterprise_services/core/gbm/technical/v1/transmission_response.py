from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbm.technical.v1.transmission_response_type import (
    TransmissionResponseType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/technical/v1"


@dataclass
class TransmissionResponse(TransmissionResponseType):
    """
    <description xmlns="">The definition of the response message that
    supports retrieve of a program</description>.
    """

    class Meta:
        namespace = (
            "http://generali.com/enterprise-services/core/gbm/technical/v1"
        )
