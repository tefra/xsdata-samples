from __future__ import annotations
from travelport.models.vehicle_retrieve_service_port_type_service_input import VehicleRetrieveServicePortTypeServiceInput
from travelport.models.vehicle_retrieve_service_port_type_service_output import VehicleRetrieveServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class VehicleRetrieveServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/VehicleService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/VehicleService"
    input = VehicleRetrieveServicePortTypeServiceInput
    output = VehicleRetrieveServicePortTypeServiceOutput
