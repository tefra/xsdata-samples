from __future__ import annotations

from travelport.models.passive_reservation_service_port_type_service_input import (
    PassiveReservationServicePortTypeServiceInput,
)
from travelport.models.passive_reservation_service_port_type_service_output import (
    PassiveReservationServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class PassiveReservationServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/PassiveService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/PassiveService"
    input = PassiveReservationServicePortTypeServiceInput
    output = PassiveReservationServicePortTypeServiceOutput
