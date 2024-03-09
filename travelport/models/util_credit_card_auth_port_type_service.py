from __future__ import annotations

from travelport.models.util_credit_card_auth_port_type_service_input import (
    UtilCreditCardAuthPortTypeServiceInput,
)
from travelport.models.util_credit_card_auth_port_type_service_output import (
    UtilCreditCardAuthPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UtilCreditCardAuthPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/CreditCardAuthorizationService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = (
        "http://localhost:8080/kestrel/CreditCardAuthorizationService"
    )
    input = UtilCreditCardAuthPortTypeServiceInput
    output = UtilCreditCardAuthPortTypeServiceOutput
