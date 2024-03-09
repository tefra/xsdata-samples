from __future__ import annotations

from travelport.models.find_employees_on_flight_service_port_type_service_input import (
    FindEmployeesOnFlightServicePortTypeServiceInput,
)
from travelport.models.find_employees_on_flight_service_port_type_service_output import (
    FindEmployeesOnFlightServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class FindEmployeesOnFlightServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/FindEmployeesOnFlightService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/FindEmployeesOnFlightService"
    input = FindEmployeesOnFlightServicePortTypeServiceInput
    output = FindEmployeesOnFlightServicePortTypeServiceOutput
