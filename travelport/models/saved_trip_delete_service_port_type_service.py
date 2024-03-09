from __future__ import annotations

from travelport.models.saved_trip_delete_service_port_type_service_input import (
    SavedTripDeleteServicePortTypeServiceInput,
)
from travelport.models.saved_trip_delete_service_port_type_service_output import (
    SavedTripDeleteServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SavedTripDeleteServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SavedTripDeleteService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SavedTripDeleteService"
    input = SavedTripDeleteServicePortTypeServiceInput
    output = SavedTripDeleteServicePortTypeServiceOutput
