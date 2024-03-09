from __future__ import annotations

from travelport.models.rail_exchange_create_reservation_port_type_service_input import (
    RailExchangeCreateReservationPortTypeServiceInput,
)
from travelport.models.rail_exchange_create_reservation_port_type_service_output import (
    RailExchangeCreateReservationPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class RailExchangeCreateReservationPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/RailService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/RailService"
    input = RailExchangeCreateReservationPortTypeServiceInput
    output = RailExchangeCreateReservationPortTypeServiceOutput
