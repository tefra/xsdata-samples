from __future__ import annotations
from travelport.models.calculate_tax_port_type_service_input import (
    CalculateTaxPortTypeServiceInput,
)
from travelport.models.calculate_tax_port_type_service_output import (
    CalculateTaxPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class CalculateTaxPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = CalculateTaxPortTypeServiceInput
    output = CalculateTaxPortTypeServiceOutput
