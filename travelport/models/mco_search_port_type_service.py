from __future__ import annotations
from travelport.models.mco_search_port_type_service_input import (
    McoSearchPortTypeServiceInput,
)
from travelport.models.mco_search_port_type_service_output import (
    McoSearchPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class McoSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = McoSearchPortTypeServiceInput
    output = McoSearchPortTypeServiceOutput
