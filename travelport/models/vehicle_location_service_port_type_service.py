from __future__ import annotations

from travelport.models.vehicle_location_service_port_type_service_input import (
    VehicleLocationServicePortTypeServiceInput,
)
from travelport.models.vehicle_location_service_port_type_service_output import (
    VehicleLocationServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class VehicleLocationServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/VehicleService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/VehicleService"
    input = VehicleLocationServicePortTypeServiceInput
    output = VehicleLocationServicePortTypeServiceOutput
