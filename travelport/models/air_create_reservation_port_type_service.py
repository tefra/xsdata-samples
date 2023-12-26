from __future__ import annotations
from travelport.models.air_create_reservation_port_type_service_input import (
    AirCreateReservationPortTypeServiceInput,
)
from travelport.models.air_create_reservation_port_type_service_output import (
    AirCreateReservationPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirCreateReservationPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirCreateReservationPortTypeServiceInput
    output = AirCreateReservationPortTypeServiceOutput
