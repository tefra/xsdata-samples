from __future__ import annotations
from travelport.models.system_time_port_type_service_input import SystemTimePortTypeServiceInput
from travelport.models.system_time_port_type_service_output import SystemTimePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SystemTimePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SystemService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SystemService"
    input = SystemTimePortTypeServiceInput
    output = SystemTimePortTypeServiceOutput
