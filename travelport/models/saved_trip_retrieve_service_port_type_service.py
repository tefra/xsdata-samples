from __future__ import annotations

from travelport.models.saved_trip_retrieve_service_port_type_service_input import (
    SavedTripRetrieveServicePortTypeServiceInput,
)
from travelport.models.saved_trip_retrieve_service_port_type_service_output import (
    SavedTripRetrieveServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SavedTripRetrieveServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SavedTripRetrieveService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SavedTripRetrieveService"
    input = SavedTripRetrieveServicePortTypeServiceInput
    output = SavedTripRetrieveServicePortTypeServiceOutput
