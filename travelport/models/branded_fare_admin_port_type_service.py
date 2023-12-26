from __future__ import annotations
from travelport.models.branded_fare_admin_port_type_service_input import (
    BrandedFareAdminPortTypeServiceInput,
)
from travelport.models.branded_fare_admin_port_type_service_output import (
    BrandedFareAdminPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BrandedFareAdminPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/BrandedFareService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/BrandedFareService"
    input = BrandedFareAdminPortTypeServiceInput
    output = BrandedFareAdminPortTypeServiceOutput
