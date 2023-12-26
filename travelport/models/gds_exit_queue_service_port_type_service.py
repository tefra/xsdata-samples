from __future__ import annotations
from travelport.models.gds_exit_queue_service_port_type_service_input import (
    GdsExitQueueServicePortTypeServiceInput,
)
from travelport.models.gds_exit_queue_service_port_type_service_output import (
    GdsExitQueueServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class GdsExitQueueServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/GdsQueueService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/GdsQueueService"
    input = GdsExitQueueServicePortTypeServiceInput
    output = GdsExitQueueServicePortTypeServiceOutput
