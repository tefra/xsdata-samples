from __future__ import annotations
from travelport.models.util_currency_conversion_port_type_service_input import (
    UtilCurrencyConversionPortTypeServiceInput,
)
from travelport.models.util_currency_conversion_port_type_service_output import (
    UtilCurrencyConversionPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UtilCurrencyConversionPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/CurrencyConversionService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/CurrencyConversionService"
    input = UtilCurrencyConversionPortTypeServiceInput
    output = UtilCurrencyConversionPortTypeServiceOutput
