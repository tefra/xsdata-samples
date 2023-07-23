from __future__ import annotations
from travelport.models.gds_queue_remove_service_port_type_service_input import GdsQueueRemoveServicePortTypeServiceInput
from travelport.models.gds_queue_remove_service_port_type_service_output import GdsQueueRemoveServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class GdsQueueRemoveServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/GdsQueueService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/GdsQueueService"
    input = GdsQueueRemoveServicePortTypeServiceInput
    output = GdsQueueRemoveServicePortTypeServiceOutput
