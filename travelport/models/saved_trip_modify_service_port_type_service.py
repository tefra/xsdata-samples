from __future__ import annotations
from travelport.models.saved_trip_modify_service_port_type_service_input import SavedTripModifyServicePortTypeServiceInput
from travelport.models.saved_trip_modify_service_port_type_service_output import SavedTripModifyServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SavedTripModifyServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SavedTripModifyService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SavedTripModifyService"
    input = SavedTripModifyServicePortTypeServiceInput
    output = SavedTripModifyServicePortTypeServiceOutput
