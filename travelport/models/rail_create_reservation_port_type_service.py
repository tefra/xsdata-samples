from __future__ import annotations
from travelport.models.rail_create_reservation_port_type_service_input import RailCreateReservationPortTypeServiceInput
from travelport.models.rail_create_reservation_port_type_service_output import RailCreateReservationPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class RailCreateReservationPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/RailService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/RailService"
    input = RailCreateReservationPortTypeServiceInput
    output = RailCreateReservationPortTypeServiceOutput
