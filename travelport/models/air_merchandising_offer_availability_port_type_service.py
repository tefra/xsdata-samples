from __future__ import annotations

from travelport.models.air_merchandising_offer_availability_port_type_service_input import (
    AirMerchandisingOfferAvailabilityPortTypeServiceInput,
)
from travelport.models.air_merchandising_offer_availability_port_type_service_output import (
    AirMerchandisingOfferAvailabilityPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirMerchandisingOfferAvailabilityPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirMerchandisingOfferAvailabilityPortTypeServiceInput
    output = AirMerchandisingOfferAvailabilityPortTypeServiceOutput
