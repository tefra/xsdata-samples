from __future__ import annotations

from travelport.models.gds_next_on_queue_service_port_type_service_input import (
    GdsNextOnQueueServicePortTypeServiceInput,
)
from travelport.models.gds_next_on_queue_service_port_type_service_output import (
    GdsNextOnQueueServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class GdsNextOnQueueServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/GdsQueueService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/GdsQueueService"
    input = GdsNextOnQueueServicePortTypeServiceInput
    output = GdsNextOnQueueServicePortTypeServiceOutput
