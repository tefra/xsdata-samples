from __future__ import annotations
from travelport.models.mco_void_port_type_service_input import (
    McoVoidPortTypeServiceInput,
)
from travelport.models.mco_void_port_type_service_output import (
    McoVoidPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class McoVoidPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = McoVoidPortTypeServiceInput
    output = McoVoidPortTypeServiceOutput
