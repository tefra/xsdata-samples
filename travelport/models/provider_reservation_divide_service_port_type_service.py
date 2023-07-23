from __future__ import annotations
from travelport.models.provider_reservation_divide_service_port_type_service_input import ProviderReservationDivideServicePortTypeServiceInput
from travelport.models.provider_reservation_divide_service_port_type_service_output import ProviderReservationDivideServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProviderReservationDivideServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UniversalRecordService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UniversalRecordService"
    input = ProviderReservationDivideServicePortTypeServiceInput
    output = ProviderReservationDivideServicePortTypeServiceOutput
