from __future__ import annotations

from travelport.models.saved_trip_create_service_port_type_service_input import (
    SavedTripCreateServicePortTypeServiceInput,
)
from travelport.models.saved_trip_create_service_port_type_service_output import (
    SavedTripCreateServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SavedTripCreateServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SavedTripCreateService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SavedTripCreateService"
    input = SavedTripCreateServicePortTypeServiceInput
    output = SavedTripCreateServicePortTypeServiceOutput
