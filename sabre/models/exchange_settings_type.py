from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.exchange_settings_type_reissue_exchange import (
    ExchangeSettingsTypeReissueExchange,
)
from sabre.models.exchange_settings_type_request_type import (
    ExchangeSettingsTypeRequestType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ExchangeSettingsType:
    """
    Attributes:
        reprice_current_itin: If set to ''false'', disables processing
            of Current Itin path.
        attach_exchange_info: If set to ''true'', adds exchange-specific
            information to the response. The information includes richer
            Tax elements, ReissueVsExchange attribute and currency
            conversion rates.
        reissue_exchange: Process Type Indicator for Primary Request
            Type
        branded_results: Enables branded results (if brands are
            available for returned options)
        miptimeout_threshold: Hints MIP that it should return options
            within this amount of time (in seconds)
        request_type: Used to specify if the request is an usual
            Exchange request (basic) or an Exchange Context Shopping
            request (context). When not specified, basic is assumed.
    """

    reprice_current_itin: bool = field(
        default=True,
        metadata={
            "name": "RepriceCurrentItin",
            "type": "Attribute",
        },
    )
    attach_exchange_info: bool = field(
        default=False,
        metadata={
            "name": "AttachExchangeInfo",
            "type": "Attribute",
        },
    )
    reissue_exchange: None | ExchangeSettingsTypeReissueExchange = field(
        default=None,
        metadata={
            "name": "ReissueExchange",
            "type": "Attribute",
        },
    )
    branded_results: None | bool = field(
        default=None,
        metadata={
            "name": "BrandedResults",
            "type": "Attribute",
        },
    )
    miptimeout_threshold: None | int = field(
        default=None,
        metadata={
            "name": "MIPTimeoutThreshold",
            "type": "Attribute",
        },
    )
    request_type: None | ExchangeSettingsTypeRequestType = field(
        default=None,
        metadata={
            "name": "RequestType",
            "type": "Attribute",
        },
    )
