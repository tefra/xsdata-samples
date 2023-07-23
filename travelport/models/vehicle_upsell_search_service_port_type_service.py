from __future__ import annotations
from travelport.models.vehicle_upsell_search_service_port_type_service_input import VehicleUpsellSearchServicePortTypeServiceInput
from travelport.models.vehicle_upsell_search_service_port_type_service_output import VehicleUpsellSearchServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class VehicleUpsellSearchServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/VehicleService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/VehicleService"
    input = VehicleUpsellSearchServicePortTypeServiceInput
    output = VehicleUpsellSearchServicePortTypeServiceOutput
