from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbm.technical.v1.transmission_request_type import TransmissionRequestType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/technical/v1"


@dataclass
class TransmissionRequest(TransmissionRequestType):
    """
    <description xmlns="">The definition of the request message that supports
    retrieval of a agreement</description>
    """
    class Meta:
        namespace = "http://generali.com/enterprise-services/core/gbm/technical/v1"
