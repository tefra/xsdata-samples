from __future__ import annotations
from travelport.models.system_ping_port_type_service_input import (
    SystemPingPortTypeServiceInput,
)
from travelport.models.system_ping_port_type_service_output import (
    SystemPingPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SystemPingPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SystemService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SystemService"
    input = SystemPingPortTypeServiceInput
    output = SystemPingPortTypeServiceOutput
