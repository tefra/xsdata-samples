from __future__ import annotations

from travelport.models.passive_cancel_service_port_type_service_input import (
    PassiveCancelServicePortTypeServiceInput,
)
from travelport.models.passive_cancel_service_port_type_service_output import (
    PassiveCancelServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class PassiveCancelServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/PassiveService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/PassiveService"
    input = PassiveCancelServicePortTypeServiceInput
    output = PassiveCancelServicePortTypeServiceOutput
