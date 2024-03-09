from __future__ import annotations

from travelport.models.air_fare_rules_port_type_service_input import (
    AirFareRulesPortTypeServiceInput,
)
from travelport.models.air_fare_rules_port_type_service_output import (
    AirFareRulesPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirFareRulesPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirFareRulesPortTypeServiceInput
    output = AirFareRulesPortTypeServiceOutput
