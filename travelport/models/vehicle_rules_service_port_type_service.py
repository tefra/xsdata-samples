from __future__ import annotations
from travelport.models.vehicle_rules_service_port_type_service_input import (
    VehicleRulesServicePortTypeServiceInput,
)
from travelport.models.vehicle_rules_service_port_type_service_output import (
    VehicleRulesServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class VehicleRulesServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/VehicleService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/VehicleService"
    input = VehicleRulesServicePortTypeServiceInput
    output = VehicleRulesServicePortTypeServiceOutput
