from __future__ import annotations

from travelport.models.terminal_service_port_type_service_input import (
    TerminalServicePortTypeServiceInput,
)
from travelport.models.terminal_service_port_type_service_output import (
    TerminalServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class TerminalServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/TerminalService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/TerminalService"
    input = TerminalServicePortTypeServiceInput
    output = TerminalServicePortTypeServiceOutput
