from __future__ import annotations
from travelport.models.gds_queue_count_service_port_type_service_input import (
    GdsQueueCountServicePortTypeServiceInput,
)
from travelport.models.gds_queue_count_service_port_type_service_output import (
    GdsQueueCountServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class GdsQueueCountServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/GdsQueueService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/GdsQueueService"
    input = GdsQueueCountServicePortTypeServiceInput
    output = GdsQueueCountServicePortTypeServiceOutput
