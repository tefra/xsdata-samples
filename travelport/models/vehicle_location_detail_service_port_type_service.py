from __future__ import annotations
from travelport.models.vehicle_location_detail_service_port_type_service_input import (
    VehicleLocationDetailServicePortTypeServiceInput,
)
from travelport.models.vehicle_location_detail_service_port_type_service_output import (
    VehicleLocationDetailServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class VehicleLocationDetailServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/VehicleService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/VehicleService"
    input = VehicleLocationDetailServicePortTypeServiceInput
    output = VehicleLocationDetailServicePortTypeServiceOutput
