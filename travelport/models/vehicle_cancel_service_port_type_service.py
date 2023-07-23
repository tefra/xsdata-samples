from __future__ import annotations
from travelport.models.vehicle_cancel_service_port_type_service_input import VehicleCancelServicePortTypeServiceInput
from travelport.models.vehicle_cancel_service_port_type_service_output import VehicleCancelServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class VehicleCancelServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/VehicleService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/VehicleService"
    input = VehicleCancelServicePortTypeServiceInput
    output = VehicleCancelServicePortTypeServiceOutput
