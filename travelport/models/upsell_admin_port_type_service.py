from __future__ import annotations
from travelport.models.upsell_admin_port_type_service_input import UpsellAdminPortTypeServiceInput
from travelport.models.upsell_admin_port_type_service_output import UpsellAdminPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UpsellAdminPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UpsellAdminService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UpsellAdminService"
    input = UpsellAdminPortTypeServiceInput
    output = UpsellAdminPortTypeServiceOutput
