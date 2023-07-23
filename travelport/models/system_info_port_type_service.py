from __future__ import annotations
from travelport.models.system_info_port_type_service_input import SystemInfoPortTypeServiceInput
from travelport.models.system_info_port_type_service_output import SystemInfoPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SystemInfoPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SystemService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SystemService"
    input = SystemInfoPortTypeServiceInput
    output = SystemInfoPortTypeServiceOutput
