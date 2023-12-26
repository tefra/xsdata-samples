from __future__ import annotations
from travelport.models.saved_trip_search_service_port_type_service_input import (
    SavedTripSearchServicePortTypeServiceInput,
)
from travelport.models.saved_trip_search_service_port_type_service_output import (
    SavedTripSearchServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SavedTripSearchServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SavedTripSearchService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SavedTripSearchService"
    input = SavedTripSearchServicePortTypeServiceInput
    output = SavedTripSearchServicePortTypeServiceOutput
