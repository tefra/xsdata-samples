from __future__ import annotations
from travelport.models.end_terminal_session_service_port_type_service_input import EndTerminalSessionServicePortTypeServiceInput
from travelport.models.end_terminal_session_service_port_type_service_output import EndTerminalSessionServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class EndTerminalSessionServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/TerminalService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/TerminalService"
    input = EndTerminalSessionServicePortTypeServiceInput
    output = EndTerminalSessionServicePortTypeServiceOutput
