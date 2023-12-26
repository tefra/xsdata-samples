from __future__ import annotations
from travelport.models.mco_create_agency_fee_port_type_service_input import (
    McoCreateAgencyFeePortTypeServiceInput,
)
from travelport.models.mco_create_agency_fee_port_type_service_output import (
    McoCreateAgencyFeePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class McoCreateAgencyFeePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = McoCreateAgencyFeePortTypeServiceInput
    output = McoCreateAgencyFeePortTypeServiceOutput
