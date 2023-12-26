from __future__ import annotations
from travelport.models.vehicle_reservation_service_port_type_service_input import (
    VehicleReservationServicePortTypeServiceInput,
)
from travelport.models.vehicle_reservation_service_port_type_service_output import (
    VehicleReservationServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class VehicleReservationServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/VehicleService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/VehicleService"
    input = VehicleReservationServicePortTypeServiceInput
    output = VehicleReservationServicePortTypeServiceOutput
