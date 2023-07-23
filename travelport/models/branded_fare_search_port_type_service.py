from __future__ import annotations
from travelport.models.branded_fare_search_port_type_service_input import BrandedFareSearchPortTypeServiceInput
from travelport.models.branded_fare_search_port_type_service_output import BrandedFareSearchPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BrandedFareSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/BrandedFareService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/BrandedFareService"
    input = BrandedFareSearchPortTypeServiceInput
    output = BrandedFareSearchPortTypeServiceOutput
