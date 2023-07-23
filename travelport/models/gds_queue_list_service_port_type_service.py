from __future__ import annotations
from travelport.models.gds_queue_list_service_port_type_service_input import GdsQueueListServicePortTypeServiceInput
from travelport.models.gds_queue_list_service_port_type_service_output import GdsQueueListServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class GdsQueueListServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/GdsQueueService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/GdsQueueService"
    input = GdsQueueListServicePortTypeServiceInput
    output = GdsQueueListServicePortTypeServiceOutput
