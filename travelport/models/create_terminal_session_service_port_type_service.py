from __future__ import annotations

from travelport.models.create_terminal_session_service_port_type_service_input import (
    CreateTerminalSessionServicePortTypeServiceInput,
)
from travelport.models.create_terminal_session_service_port_type_service_output import (
    CreateTerminalSessionServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class CreateTerminalSessionServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/TerminalService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/TerminalService"
    input = CreateTerminalSessionServicePortTypeServiceInput
    output = CreateTerminalSessionServicePortTypeServiceOutput
