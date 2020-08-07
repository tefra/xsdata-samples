from dataclasses import dataclass, field
from typing import Optional
from travelport.models.travelport_com_schema_air_v48_0 import (
    AirExchangeEligibilityReq,
    AirExchangeEligibilityRsp,
    AirExchangeMultiQuoteReq,
    AirExchangeMultiQuoteRsp,
    AirExchangeQuoteReq,
    AirExchangeQuoteRsp,
    AirExchangeReq,
    AirExchangeRsp,
    AirExchangeTicketingReq,
    AirExchangeTicketingRsp,
    AirFareDisplayReq,
    AirFareDisplayRsp,
    AirFareRulesReq,
    AirFareRulesRsp,
    AirMerchandisingDetailsReq,
    AirMerchandisingDetailsRsp,
    AirMerchandisingOfferAvailabilityReq,
    AirMerchandisingOfferAvailabilityRsp,
    AirPrePayReq,
    AirPrePayRsp,
    AirPriceReq,
    AirPriceRsp,
    AirRefundQuoteReq,
    AirRefundQuoteRsp,
    AirRefundReq,
    AirRefundRsp,
    AirRepriceReq,
    AirRepriceRsp,
    AirRetrieveDocumentReq,
    AirRetrieveDocumentRsp,
    AirTicketingReq,
    AirTicketingRsp,
    AirUpsellSearchReq,
    AirUpsellSearchRsp,
    AirVoidDocumentReq,
    AirVoidDocumentRsp,
    AvailabilitySearchReq,
    AvailabilitySearchRsp,
    EmdissuanceReq,
    EmdissuanceRsp,
    EmdretrieveReq,
    EmdretrieveRsp,
    FlightDetailsReq,
    FlightDetailsRsp,
    FlightInformationReq,
    FlightInformationRsp,
    FlightTimeTableReq,
    FlightTimeTableRsp,
    LowFareSearchAsynchReq,
    LowFareSearchAsynchRsp,
    LowFareSearchReq,
    LowFareSearchRsp,
    RetrieveLowFareSearchReq,
    RetrieveLowFareSearchRsp,
    ScheduleSearchReq,
    ScheduleSearchRsp,
    SeatMapReq,
    SeatMapRsp,
)
from travelport.models.travelport_com_soa_common_security_session_context_v1 import SessionContext

__NAMESPACE__ = "http://www.travelport.com/service/air_v48_0"


@dataclass
class AirAvailabilitySearchPortTypeServiceInput:
    """
    :ivar header:
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirAvailabilitySearchPortTypeServiceInput.Header"] = field(
        default=None,
        metadata=dict(
            name="Header",
            type="Element"
        )
    )
    body: Optional["AirAvailabilitySearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Header:
        """
        :ivar session_context:
        """
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata=dict(
                name="SessionContext",
                type="Element",
                namespace="http://www.travelport.com/soa/common/security/SessionContext_v1"
            )
        )

    @dataclass
    class Body:
        """
        :ivar availability_search_req:
        """
        availability_search_req: Optional[AvailabilitySearchReq] = field(
            default=None,
            metadata=dict(
                name="AvailabilitySearchReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirAvailabilitySearchPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirAvailabilitySearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar availability_search_rsp:
        """
        availability_search_rsp: Optional[AvailabilitySearchRsp] = field(
            default=None,
            metadata=dict(
                name="AvailabilitySearchRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeEligibilityPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeEligibilityPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_eligibility_req:
        """
        air_exchange_eligibility_req: Optional[AirExchangeEligibilityReq] = field(
            default=None,
            metadata=dict(
                name="AirExchangeEligibilityReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeEligibilityPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeEligibilityPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_eligibility_rsp:
        """
        air_exchange_eligibility_rsp: Optional[AirExchangeEligibilityRsp] = field(
            default=None,
            metadata=dict(
                name="AirExchangeEligibilityRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeMultiQuotePortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeMultiQuotePortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_multi_quote_req:
        """
        air_exchange_multi_quote_req: Optional[AirExchangeMultiQuoteReq] = field(
            default=None,
            metadata=dict(
                name="AirExchangeMultiQuoteReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeMultiQuotePortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeMultiQuotePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_multi_quote_rsp:
        """
        air_exchange_multi_quote_rsp: Optional[AirExchangeMultiQuoteRsp] = field(
            default=None,
            metadata=dict(
                name="AirExchangeMultiQuoteRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeProcessPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeProcessPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_req:
        """
        air_exchange_req: Optional[AirExchangeReq] = field(
            default=None,
            metadata=dict(
                name="AirExchangeReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeProcessPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeProcessPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_rsp:
        """
        air_exchange_rsp: Optional[AirExchangeRsp] = field(
            default=None,
            metadata=dict(
                name="AirExchangeRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeQuotePortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeQuotePortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_quote_req:
        """
        air_exchange_quote_req: Optional[AirExchangeQuoteReq] = field(
            default=None,
            metadata=dict(
                name="AirExchangeQuoteReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeQuotePortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeQuotePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_quote_rsp:
        """
        air_exchange_quote_rsp: Optional[AirExchangeQuoteRsp] = field(
            default=None,
            metadata=dict(
                name="AirExchangeQuoteRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeTicketingPortTypeServiceInput:
    """
    :ivar header:
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirExchangeTicketingPortTypeServiceInput.Header"] = field(
        default=None,
        metadata=dict(
            name="Header",
            type="Element"
        )
    )
    body: Optional["AirExchangeTicketingPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Header:
        """
        :ivar session_context:
        """
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata=dict(
                name="SessionContext",
                type="Element",
                namespace="http://www.travelport.com/soa/common/security/SessionContext_v1"
            )
        )

    @dataclass
    class Body:
        """
        :ivar air_exchange_ticketing_req:
        """
        air_exchange_ticketing_req: Optional[AirExchangeTicketingReq] = field(
            default=None,
            metadata=dict(
                name="AirExchangeTicketingReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirExchangeTicketingPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeTicketingPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_exchange_ticketing_rsp:
        """
        air_exchange_ticketing_rsp: Optional[AirExchangeTicketingRsp] = field(
            default=None,
            metadata=dict(
                name="AirExchangeTicketingRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirFareDisplayPortTypeServiceInput:
    """
    :ivar header:
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirFareDisplayPortTypeServiceInput.Header"] = field(
        default=None,
        metadata=dict(
            name="Header",
            type="Element"
        )
    )
    body: Optional["AirFareDisplayPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Header:
        """
        :ivar session_context:
        """
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata=dict(
                name="SessionContext",
                type="Element",
                namespace="http://www.travelport.com/soa/common/security/SessionContext_v1"
            )
        )

    @dataclass
    class Body:
        """
        :ivar air_fare_display_req:
        """
        air_fare_display_req: Optional[AirFareDisplayReq] = field(
            default=None,
            metadata=dict(
                name="AirFareDisplayReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirFareDisplayPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirFareDisplayPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_fare_display_rsp:
        """
        air_fare_display_rsp: Optional[AirFareDisplayRsp] = field(
            default=None,
            metadata=dict(
                name="AirFareDisplayRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirFareRulesPortTypeServiceInput:
    """
    :ivar header:
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirFareRulesPortTypeServiceInput.Header"] = field(
        default=None,
        metadata=dict(
            name="Header",
            type="Element"
        )
    )
    body: Optional["AirFareRulesPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Header:
        """
        :ivar session_context:
        """
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata=dict(
                name="SessionContext",
                type="Element",
                namespace="http://www.travelport.com/soa/common/security/SessionContext_v1"
            )
        )

    @dataclass
    class Body:
        """
        :ivar air_fare_rules_req:
        """
        air_fare_rules_req: Optional[AirFareRulesReq] = field(
            default=None,
            metadata=dict(
                name="AirFareRulesReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirFareRulesPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirFareRulesPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_fare_rules_rsp:
        """
        air_fare_rules_rsp: Optional[AirFareRulesRsp] = field(
            default=None,
            metadata=dict(
                name="AirFareRulesRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirLowFareSearchAsynchPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirLowFareSearchAsynchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar low_fare_search_asynch_req:
        """
        low_fare_search_asynch_req: Optional[LowFareSearchAsynchReq] = field(
            default=None,
            metadata=dict(
                name="LowFareSearchAsynchReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirLowFareSearchAsynchPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirLowFareSearchAsynchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar low_fare_search_asynch_rsp:
        """
        low_fare_search_asynch_rsp: Optional[LowFareSearchAsynchRsp] = field(
            default=None,
            metadata=dict(
                name="LowFareSearchAsynchRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirLowFareSearchPortTypeServiceInput:
    """
    :ivar header:
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirLowFareSearchPortTypeServiceInput.Header"] = field(
        default=None,
        metadata=dict(
            name="Header",
            type="Element"
        )
    )
    body: Optional["AirLowFareSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Header:
        """
        :ivar session_context:
        """
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata=dict(
                name="SessionContext",
                type="Element",
                namespace="http://www.travelport.com/soa/common/security/SessionContext_v1"
            )
        )

    @dataclass
    class Body:
        """
        :ivar low_fare_search_req:
        """
        low_fare_search_req: Optional[LowFareSearchReq] = field(
            default=None,
            metadata=dict(
                name="LowFareSearchReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirLowFareSearchPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirLowFareSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar low_fare_search_rsp:
        """
        low_fare_search_rsp: Optional[LowFareSearchRsp] = field(
            default=None,
            metadata=dict(
                name="LowFareSearchRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirMerchandisingDetailsPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirMerchandisingDetailsPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_merchandising_details_req:
        """
        air_merchandising_details_req: Optional[AirMerchandisingDetailsReq] = field(
            default=None,
            metadata=dict(
                name="AirMerchandisingDetailsReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirMerchandisingDetailsPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirMerchandisingDetailsPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_merchandising_details_rsp:
        """
        air_merchandising_details_rsp: Optional[AirMerchandisingDetailsRsp] = field(
            default=None,
            metadata=dict(
                name="AirMerchandisingDetailsRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirMerchandisingOfferAvailabilityPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirMerchandisingOfferAvailabilityPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_merchandising_offer_availability_req:
        """
        air_merchandising_offer_availability_req: Optional[AirMerchandisingOfferAvailabilityReq] = field(
            default=None,
            metadata=dict(
                name="AirMerchandisingOfferAvailabilityReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirMerchandisingOfferAvailabilityPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirMerchandisingOfferAvailabilityPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_merchandising_offer_availability_rsp:
        """
        air_merchandising_offer_availability_rsp: Optional[AirMerchandisingOfferAvailabilityRsp] = field(
            default=None,
            metadata=dict(
                name="AirMerchandisingOfferAvailabilityRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirPrePayPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirPrePayPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_pre_pay_req:
        """
        air_pre_pay_req: Optional[AirPrePayReq] = field(
            default=None,
            metadata=dict(
                name="AirPrePayReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirPrePayPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirPrePayPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_pre_pay_rsp:
        """
        air_pre_pay_rsp: Optional[AirPrePayRsp] = field(
            default=None,
            metadata=dict(
                name="AirPrePayRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirPricePortTypeServiceInput:
    """
    :ivar header:
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirPricePortTypeServiceInput.Header"] = field(
        default=None,
        metadata=dict(
            name="Header",
            type="Element"
        )
    )
    body: Optional["AirPricePortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Header:
        """
        :ivar session_context:
        """
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata=dict(
                name="SessionContext",
                type="Element",
                namespace="http://www.travelport.com/soa/common/security/SessionContext_v1"
            )
        )

    @dataclass
    class Body:
        """
        :ivar air_price_req:
        """
        air_price_req: Optional[AirPriceReq] = field(
            default=None,
            metadata=dict(
                name="AirPriceReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirPricePortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirPricePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_price_rsp:
        """
        air_price_rsp: Optional[AirPriceRsp] = field(
            default=None,
            metadata=dict(
                name="AirPriceRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRefundQuotePortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRefundQuotePortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_refund_quote_req:
        """
        air_refund_quote_req: Optional[AirRefundQuoteReq] = field(
            default=None,
            metadata=dict(
                name="AirRefundQuoteReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRefundQuotePortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRefundQuotePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_refund_quote_rsp:
        """
        air_refund_quote_rsp: Optional[AirRefundQuoteRsp] = field(
            default=None,
            metadata=dict(
                name="AirRefundQuoteRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRefundTicketPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRefundTicketPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_refund_req:
        """
        air_refund_req: Optional[AirRefundReq] = field(
            default=None,
            metadata=dict(
                name="AirRefundReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRefundTicketPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRefundTicketPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_refund_rsp:
        """
        air_refund_rsp: Optional[AirRefundRsp] = field(
            default=None,
            metadata=dict(
                name="AirRefundRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRepriceSearchPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRepriceSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_reprice_req:
        """
        air_reprice_req: Optional[AirRepriceReq] = field(
            default=None,
            metadata=dict(
                name="AirRepriceReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRepriceSearchPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRepriceSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_reprice_rsp:
        """
        air_reprice_rsp: Optional[AirRepriceRsp] = field(
            default=None,
            metadata=dict(
                name="AirRepriceRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRetrieveDocumentPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRetrieveDocumentPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_retrieve_document_req:
        """
        air_retrieve_document_req: Optional[AirRetrieveDocumentReq] = field(
            default=None,
            metadata=dict(
                name="AirRetrieveDocumentReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRetrieveDocumentPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRetrieveDocumentPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_retrieve_document_rsp:
        """
        air_retrieve_document_rsp: Optional[AirRetrieveDocumentRsp] = field(
            default=None,
            metadata=dict(
                name="AirRetrieveDocumentRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRetrieveLowFareSearchPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRetrieveLowFareSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar retrieve_low_fare_search_req:
        """
        retrieve_low_fare_search_req: Optional[RetrieveLowFareSearchReq] = field(
            default=None,
            metadata=dict(
                name="RetrieveLowFareSearchReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirRetrieveLowFareSearchPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRetrieveLowFareSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar retrieve_low_fare_search_rsp:
        """
        retrieve_low_fare_search_rsp: Optional[RetrieveLowFareSearchRsp] = field(
            default=None,
            metadata=dict(
                name="RetrieveLowFareSearchRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirScheduleSearchPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirScheduleSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar schedule_search_req:
        """
        schedule_search_req: Optional[ScheduleSearchReq] = field(
            default=None,
            metadata=dict(
                name="ScheduleSearchReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirScheduleSearchPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirScheduleSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar schedule_search_rsp:
        """
        schedule_search_rsp: Optional[ScheduleSearchRsp] = field(
            default=None,
            metadata=dict(
                name="ScheduleSearchRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirTicketingPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirTicketingPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_ticketing_req:
        """
        air_ticketing_req: Optional[AirTicketingReq] = field(
            default=None,
            metadata=dict(
                name="AirTicketingReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirTicketingPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirTicketingPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_ticketing_rsp:
        """
        air_ticketing_rsp: Optional[AirTicketingRsp] = field(
            default=None,
            metadata=dict(
                name="AirTicketingRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirUpsellSearchPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirUpsellSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_upsell_search_req:
        """
        air_upsell_search_req: Optional[AirUpsellSearchReq] = field(
            default=None,
            metadata=dict(
                name="AirUpsellSearchReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirUpsellSearchPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirUpsellSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_upsell_search_rsp:
        """
        air_upsell_search_rsp: Optional[AirUpsellSearchRsp] = field(
            default=None,
            metadata=dict(
                name="AirUpsellSearchRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirVoidDocumentPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirVoidDocumentPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_void_document_req:
        """
        air_void_document_req: Optional[AirVoidDocumentReq] = field(
            default=None,
            metadata=dict(
                name="AirVoidDocumentReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class AirVoidDocumentPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirVoidDocumentPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar air_void_document_rsp:
        """
        air_void_document_rsp: Optional[AirVoidDocumentRsp] = field(
            default=None,
            metadata=dict(
                name="AirVoidDocumentRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class EmdissuancePortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EmdissuancePortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar emdissuance_req:
        """
        emdissuance_req: Optional[EmdissuanceReq] = field(
            default=None,
            metadata=dict(
                name="EMDIssuanceReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class EmdissuancePortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EmdissuancePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar emdissuance_rsp:
        """
        emdissuance_rsp: Optional[EmdissuanceRsp] = field(
            default=None,
            metadata=dict(
                name="EMDIssuanceRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class EmdretrievePortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EmdretrievePortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar emdretrieve_req:
        """
        emdretrieve_req: Optional[EmdretrieveReq] = field(
            default=None,
            metadata=dict(
                name="EMDRetrieveReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class EmdretrievePortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EmdretrievePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar emdretrieve_rsp:
        """
        emdretrieve_rsp: Optional[EmdretrieveRsp] = field(
            default=None,
            metadata=dict(
                name="EMDRetrieveRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class FlightDetailsPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightDetailsPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar flight_details_req:
        """
        flight_details_req: Optional[FlightDetailsReq] = field(
            default=None,
            metadata=dict(
                name="FlightDetailsReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class FlightDetailsPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightDetailsPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar flight_details_rsp:
        """
        flight_details_rsp: Optional[FlightDetailsRsp] = field(
            default=None,
            metadata=dict(
                name="FlightDetailsRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class FlightInfoPortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightInfoPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar flight_information_req:
        """
        flight_information_req: Optional[FlightInformationReq] = field(
            default=None,
            metadata=dict(
                name="FlightInformationReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class FlightInfoPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightInfoPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar flight_information_rsp:
        """
        flight_information_rsp: Optional[FlightInformationRsp] = field(
            default=None,
            metadata=dict(
                name="FlightInformationRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class FlightTimeTablePortTypeServiceInput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightTimeTablePortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar flight_time_table_req:
        """
        flight_time_table_req: Optional[FlightTimeTableReq] = field(
            default=None,
            metadata=dict(
                name="FlightTimeTableReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class FlightTimeTablePortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightTimeTablePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar flight_time_table_rsp:
        """
        flight_time_table_rsp: Optional[FlightTimeTableRsp] = field(
            default=None,
            metadata=dict(
                name="FlightTimeTableRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class SeatMapPortTypeServiceInput:
    """
    :ivar header:
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["SeatMapPortTypeServiceInput.Header"] = field(
        default=None,
        metadata=dict(
            name="Header",
            type="Element"
        )
    )
    body: Optional["SeatMapPortTypeServiceInput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Header:
        """
        :ivar session_context:
        """
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata=dict(
                name="SessionContext",
                type="Element",
                namespace="http://www.travelport.com/soa/common/security/SessionContext_v1"
            )
        )

    @dataclass
    class Body:
        """
        :ivar seat_map_req:
        """
        seat_map_req: Optional[SeatMapReq] = field(
            default=None,
            metadata=dict(
                name="SeatMapReq",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


@dataclass
class SeatMapPortTypeServiceOutput:
    """
    :ivar body:
    """
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["SeatMapPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata=dict(
            name="Body",
            type="Element"
        )
    )

    @dataclass
    class Body:
        """
        :ivar seat_map_rsp:
        """
        seat_map_rsp: Optional[SeatMapRsp] = field(
            default=None,
            metadata=dict(
                name="SeatMapRsp",
                type="Element",
                namespace="http://www.travelport.com/schema/air_v48_0"
            )
        )


class AirAvailabilitySearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirAvailabilitySearchPortTypeServiceInput
    output = AirAvailabilitySearchPortTypeServiceOutput


class AirExchangeEligibilityPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirExchangeEligibilityPortTypeServiceInput
    output = AirExchangeEligibilityPortTypeServiceOutput


class AirExchangeMultiQuotePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirExchangeMultiQuotePortTypeServiceInput
    output = AirExchangeMultiQuotePortTypeServiceOutput


class AirExchangeProcessPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirExchangeProcessPortTypeServiceInput
    output = AirExchangeProcessPortTypeServiceOutput


class AirExchangeQuotePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirExchangeQuotePortTypeServiceInput
    output = AirExchangeQuotePortTypeServiceOutput


class AirExchangeTicketingPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirExchangeTicketingPortTypeServiceInput
    output = AirExchangeTicketingPortTypeServiceOutput


class AirFareDisplayPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirFareDisplayPortTypeServiceInput
    output = AirFareDisplayPortTypeServiceOutput


class AirFareRulesPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirFareRulesPortTypeServiceInput
    output = AirFareRulesPortTypeServiceOutput


class AirLowFareSearchAsynchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirLowFareSearchAsynchPortTypeServiceInput
    output = AirLowFareSearchAsynchPortTypeServiceOutput


class AirLowFareSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirLowFareSearchPortTypeServiceInput
    output = AirLowFareSearchPortTypeServiceOutput


class AirMerchandisingDetailsPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirMerchandisingDetailsPortTypeServiceInput
    output = AirMerchandisingDetailsPortTypeServiceOutput


class AirMerchandisingOfferAvailabilityPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirMerchandisingOfferAvailabilityPortTypeServiceInput
    output = AirMerchandisingOfferAvailabilityPortTypeServiceOutput


class AirPrePayPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirPrePayPortTypeServiceInput
    output = AirPrePayPortTypeServiceOutput


class AirPricePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirPricePortTypeServiceInput
    output = AirPricePortTypeServiceOutput


class AirRefundQuotePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirRefundQuotePortTypeServiceInput
    output = AirRefundQuotePortTypeServiceOutput


class AirRefundTicketPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirRefundTicketPortTypeServiceInput
    output = AirRefundTicketPortTypeServiceOutput


class AirRepriceSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirRepriceSearchPortTypeServiceInput
    output = AirRepriceSearchPortTypeServiceOutput


class AirRetrieveDocumentPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirRetrieveDocumentPortTypeServiceInput
    output = AirRetrieveDocumentPortTypeServiceOutput


class AirRetrieveLowFareSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirRetrieveLowFareSearchPortTypeServiceInput
    output = AirRetrieveLowFareSearchPortTypeServiceOutput


class AirScheduleSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirScheduleSearchPortTypeServiceInput
    output = AirScheduleSearchPortTypeServiceOutput


class AirTicketingPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirTicketingPortTypeServiceInput
    output = AirTicketingPortTypeServiceOutput


class AirUpsellSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirUpsellSearchPortTypeServiceInput
    output = AirUpsellSearchPortTypeServiceOutput


class AirVoidDocumentPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirVoidDocumentPortTypeServiceInput
    output = AirVoidDocumentPortTypeServiceOutput


class EmdissuancePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = EmdissuancePortTypeServiceInput
    output = EmdissuancePortTypeServiceOutput


class EmdretrievePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = EmdretrievePortTypeServiceInput
    output = EmdretrievePortTypeServiceOutput


class FlightDetailsPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/FlightService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/FlightService"
    input = FlightDetailsPortTypeServiceInput
    output = FlightDetailsPortTypeServiceOutput


class FlightInfoPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/FlightService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/FlightService"
    input = FlightInfoPortTypeServiceInput
    output = FlightInfoPortTypeServiceOutput


class FlightTimeTablePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = FlightTimeTablePortTypeServiceInput
    output = FlightTimeTablePortTypeServiceOutput


class SeatMapPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = SeatMapPortTypeServiceInput
    output = SeatMapPortTypeServiceOutput
