from __future__ import annotations

from travelport.models.vehicle_media_links_service_port_type_service_input import (
    VehicleMediaLinksServicePortTypeServiceInput,
)
from travelport.models.vehicle_media_links_service_port_type_service_output import (
    VehicleMediaLinksServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class VehicleMediaLinksServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/VehicleService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/VehicleService"
    input = VehicleMediaLinksServicePortTypeServiceInput
    output = VehicleMediaLinksServicePortTypeServiceOutput
