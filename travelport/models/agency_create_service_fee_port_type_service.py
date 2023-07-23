from __future__ import annotations
from travelport.models.agency_create_service_fee_port_type_service_input import AgencyCreateServiceFeePortTypeServiceInput
from travelport.models.agency_create_service_fee_port_type_service_output import AgencyCreateServiceFeePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AgencyCreateServiceFeePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AgencyFeeService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AgencyFeeService"
    input = AgencyCreateServiceFeePortTypeServiceInput
    output = AgencyCreateServiceFeePortTypeServiceOutput
