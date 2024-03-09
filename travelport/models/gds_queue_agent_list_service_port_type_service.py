from __future__ import annotations

from travelport.models.gds_queue_agent_list_service_port_type_service_input import (
    GdsQueueAgentListServicePortTypeServiceInput,
)
from travelport.models.gds_queue_agent_list_service_port_type_service_output import (
    GdsQueueAgentListServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class GdsQueueAgentListServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/GdsQueueAgentListService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/GdsQueueAgentListService"
    input = GdsQueueAgentListServicePortTypeServiceInput
    output = GdsQueueAgentListServicePortTypeServiceOutput
