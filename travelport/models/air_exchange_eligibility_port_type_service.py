from __future__ import annotations
from travelport.models.air_exchange_eligibility_port_type_service_input import (
    AirExchangeEligibilityPortTypeServiceInput,
)
from travelport.models.air_exchange_eligibility_port_type_service_output import (
    AirExchangeEligibilityPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirExchangeEligibilityPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirExchangeEligibilityPortTypeServiceInput
    output = AirExchangeEligibilityPortTypeServiceOutput
