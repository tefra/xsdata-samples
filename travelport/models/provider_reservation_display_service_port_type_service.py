from __future__ import annotations
from travelport.models.provider_reservation_display_service_port_type_service_input import ProviderReservationDisplayServicePortTypeServiceInput
from travelport.models.provider_reservation_display_service_port_type_service_output import ProviderReservationDisplayServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProviderReservationDisplayServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/ProviderReservationDisplayService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/ProviderReservationDisplayService"
    input = ProviderReservationDisplayServicePortTypeServiceInput
    output = ProviderReservationDisplayServicePortTypeServiceOutput
