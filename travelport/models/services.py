from dataclasses import dataclass, field
from typing import Optional
from travelport.models.air import (
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
from travelport.models.common import ErrorInfo
from travelport.models.session import SessionContext

__NAMESPACE__ = "http://www.travelport.com/service/air_v48_0"


@dataclass
class AirAvailabilitySearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirAvailabilitySearchPortTypeServiceInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["AirAvailabilitySearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        availability_search_req: Optional[AvailabilitySearchReq] = field(
            default=None,
            metadata={
                "name": "AvailabilitySearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirAvailabilitySearchPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirAvailabilitySearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        availability_search_rsp: Optional[AvailabilitySearchRsp] = field(
            default=None,
            metadata={
                "name": "AvailabilitySearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirAvailabilitySearchPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirAvailabilitySearchPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirExchangeEligibilityPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeEligibilityPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_eligibility_req: Optional[AirExchangeEligibilityReq] = field(
            default=None,
            metadata={
                "name": "AirExchangeEligibilityReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirExchangeEligibilityPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeEligibilityPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_eligibility_rsp: Optional[AirExchangeEligibilityRsp] = field(
            default=None,
            metadata={
                "name": "AirExchangeEligibilityRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirExchangeEligibilityPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirExchangeEligibilityPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirExchangeMultiQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeMultiQuotePortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_multi_quote_req: Optional[AirExchangeMultiQuoteReq] = field(
            default=None,
            metadata={
                "name": "AirExchangeMultiQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirExchangeMultiQuotePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeMultiQuotePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_multi_quote_rsp: Optional[AirExchangeMultiQuoteRsp] = field(
            default=None,
            metadata={
                "name": "AirExchangeMultiQuoteRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirExchangeMultiQuotePortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirExchangeMultiQuotePortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirExchangeProcessPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeProcessPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_req: Optional[AirExchangeReq] = field(
            default=None,
            metadata={
                "name": "AirExchangeReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirExchangeProcessPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeProcessPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_rsp: Optional[AirExchangeRsp] = field(
            default=None,
            metadata={
                "name": "AirExchangeRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirExchangeProcessPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirExchangeProcessPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirExchangeQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeQuotePortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_quote_req: Optional[AirExchangeQuoteReq] = field(
            default=None,
            metadata={
                "name": "AirExchangeQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirExchangeQuotePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeQuotePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_quote_rsp: Optional[AirExchangeQuoteRsp] = field(
            default=None,
            metadata={
                "name": "AirExchangeQuoteRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirExchangeQuotePortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirExchangeQuotePortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirExchangeTicketingPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirExchangeTicketingPortTypeServiceInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["AirExchangeTicketingPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        air_exchange_ticketing_req: Optional[AirExchangeTicketingReq] = field(
            default=None,
            metadata={
                "name": "AirExchangeTicketingReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirExchangeTicketingPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirExchangeTicketingPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_ticketing_rsp: Optional[AirExchangeTicketingRsp] = field(
            default=None,
            metadata={
                "name": "AirExchangeTicketingRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirExchangeTicketingPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirExchangeTicketingPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirFareDisplayPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirFareDisplayPortTypeServiceInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["AirFareDisplayPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        air_fare_display_req: Optional[AirFareDisplayReq] = field(
            default=None,
            metadata={
                "name": "AirFareDisplayReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirFareDisplayPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirFareDisplayPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_fare_display_rsp: Optional[AirFareDisplayRsp] = field(
            default=None,
            metadata={
                "name": "AirFareDisplayRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirFareDisplayPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirFareDisplayPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirFareRulesPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirFareRulesPortTypeServiceInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["AirFareRulesPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        air_fare_rules_req: Optional[AirFareRulesReq] = field(
            default=None,
            metadata={
                "name": "AirFareRulesReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirFareRulesPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirFareRulesPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_fare_rules_rsp: Optional[AirFareRulesRsp] = field(
            default=None,
            metadata={
                "name": "AirFareRulesRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirFareRulesPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirFareRulesPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirLowFareSearchAsynchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirLowFareSearchAsynchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        low_fare_search_asynch_req: Optional[LowFareSearchAsynchReq] = field(
            default=None,
            metadata={
                "name": "LowFareSearchAsynchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirLowFareSearchAsynchPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirLowFareSearchAsynchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        low_fare_search_asynch_rsp: Optional[LowFareSearchAsynchRsp] = field(
            default=None,
            metadata={
                "name": "LowFareSearchAsynchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirLowFareSearchAsynchPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirLowFareSearchAsynchPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirLowFareSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirLowFareSearchPortTypeServiceInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["AirLowFareSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        low_fare_search_req: Optional[LowFareSearchReq] = field(
            default=None,
            metadata={
                "name": "LowFareSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirLowFareSearchPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirLowFareSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        low_fare_search_rsp: Optional[LowFareSearchRsp] = field(
            default=None,
            metadata={
                "name": "LowFareSearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirLowFareSearchPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirLowFareSearchPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirMerchandisingDetailsPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirMerchandisingDetailsPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_merchandising_details_req: Optional[AirMerchandisingDetailsReq] = field(
            default=None,
            metadata={
                "name": "AirMerchandisingDetailsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirMerchandisingDetailsPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirMerchandisingDetailsPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_merchandising_details_rsp: Optional[AirMerchandisingDetailsRsp] = field(
            default=None,
            metadata={
                "name": "AirMerchandisingDetailsRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirMerchandisingDetailsPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirMerchandisingDetailsPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirMerchandisingOfferAvailabilityPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirMerchandisingOfferAvailabilityPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_merchandising_offer_availability_req: Optional[AirMerchandisingOfferAvailabilityReq] = field(
            default=None,
            metadata={
                "name": "AirMerchandisingOfferAvailabilityReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirMerchandisingOfferAvailabilityPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirMerchandisingOfferAvailabilityPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_merchandising_offer_availability_rsp: Optional[AirMerchandisingOfferAvailabilityRsp] = field(
            default=None,
            metadata={
                "name": "AirMerchandisingOfferAvailabilityRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirMerchandisingOfferAvailabilityPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirMerchandisingOfferAvailabilityPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirPrePayPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirPrePayPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_pre_pay_req: Optional[AirPrePayReq] = field(
            default=None,
            metadata={
                "name": "AirPrePayReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirPrePayPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirPrePayPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_pre_pay_rsp: Optional[AirPrePayRsp] = field(
            default=None,
            metadata={
                "name": "AirPrePayRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirPrePayPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirPrePayPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirPricePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["AirPricePortTypeServiceInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["AirPricePortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        air_price_req: Optional[AirPriceReq] = field(
            default=None,
            metadata={
                "name": "AirPriceReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirPricePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirPricePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_price_rsp: Optional[AirPriceRsp] = field(
            default=None,
            metadata={
                "name": "AirPriceRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirPricePortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirPricePortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirRefundQuotePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRefundQuotePortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_quote_req: Optional[AirRefundQuoteReq] = field(
            default=None,
            metadata={
                "name": "AirRefundQuoteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirRefundQuotePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRefundQuotePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_quote_rsp: Optional[AirRefundQuoteRsp] = field(
            default=None,
            metadata={
                "name": "AirRefundQuoteRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirRefundQuotePortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirRefundQuotePortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirRefundTicketPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRefundTicketPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_req: Optional[AirRefundReq] = field(
            default=None,
            metadata={
                "name": "AirRefundReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirRefundTicketPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRefundTicketPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_rsp: Optional[AirRefundRsp] = field(
            default=None,
            metadata={
                "name": "AirRefundRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirRefundTicketPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirRefundTicketPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirRepriceSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRepriceSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_reprice_req: Optional[AirRepriceReq] = field(
            default=None,
            metadata={
                "name": "AirRepriceReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirRepriceSearchPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRepriceSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_reprice_rsp: Optional[AirRepriceRsp] = field(
            default=None,
            metadata={
                "name": "AirRepriceRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirRepriceSearchPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirRepriceSearchPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirRetrieveDocumentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRetrieveDocumentPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_retrieve_document_req: Optional[AirRetrieveDocumentReq] = field(
            default=None,
            metadata={
                "name": "AirRetrieveDocumentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirRetrieveDocumentPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRetrieveDocumentPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_retrieve_document_rsp: Optional[AirRetrieveDocumentRsp] = field(
            default=None,
            metadata={
                "name": "AirRetrieveDocumentRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirRetrieveDocumentPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirRetrieveDocumentPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirRetrieveLowFareSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRetrieveLowFareSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        retrieve_low_fare_search_req: Optional[RetrieveLowFareSearchReq] = field(
            default=None,
            metadata={
                "name": "RetrieveLowFareSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirRetrieveLowFareSearchPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirRetrieveLowFareSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        retrieve_low_fare_search_rsp: Optional[RetrieveLowFareSearchRsp] = field(
            default=None,
            metadata={
                "name": "RetrieveLowFareSearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirRetrieveLowFareSearchPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirRetrieveLowFareSearchPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirScheduleSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirScheduleSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        schedule_search_req: Optional[ScheduleSearchReq] = field(
            default=None,
            metadata={
                "name": "ScheduleSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirScheduleSearchPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirScheduleSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        schedule_search_rsp: Optional[ScheduleSearchRsp] = field(
            default=None,
            metadata={
                "name": "ScheduleSearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirScheduleSearchPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirScheduleSearchPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirTicketingPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirTicketingPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_ticketing_req: Optional[AirTicketingReq] = field(
            default=None,
            metadata={
                "name": "AirTicketingReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirTicketingPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirTicketingPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_ticketing_rsp: Optional[AirTicketingRsp] = field(
            default=None,
            metadata={
                "name": "AirTicketingRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirTicketingPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirTicketingPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirUpsellSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirUpsellSearchPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_upsell_search_req: Optional[AirUpsellSearchReq] = field(
            default=None,
            metadata={
                "name": "AirUpsellSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirUpsellSearchPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirUpsellSearchPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_upsell_search_rsp: Optional[AirUpsellSearchRsp] = field(
            default=None,
            metadata={
                "name": "AirUpsellSearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirUpsellSearchPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirUpsellSearchPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class AirVoidDocumentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirVoidDocumentPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_void_document_req: Optional[AirVoidDocumentReq] = field(
            default=None,
            metadata={
                "name": "AirVoidDocumentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class AirVoidDocumentPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["AirVoidDocumentPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_void_document_rsp: Optional[AirVoidDocumentRsp] = field(
            default=None,
            metadata={
                "name": "AirVoidDocumentRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["AirVoidDocumentPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["AirVoidDocumentPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class EmdissuancePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EmdissuancePortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdissuance_req: Optional[EmdissuanceReq] = field(
            default=None,
            metadata={
                "name": "EMDIssuanceReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class EmdissuancePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EmdissuancePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdissuance_rsp: Optional[EmdissuanceRsp] = field(
            default=None,
            metadata={
                "name": "EMDIssuanceRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["EmdissuancePortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EmdissuancePortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class EmdretrievePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EmdretrievePortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdretrieve_req: Optional[EmdretrieveReq] = field(
            default=None,
            metadata={
                "name": "EMDRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class EmdretrievePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["EmdretrievePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdretrieve_rsp: Optional[EmdretrieveRsp] = field(
            default=None,
            metadata={
                "name": "EMDRetrieveRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["EmdretrievePortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["EmdretrievePortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class FlightDetailsPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightDetailsPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_details_req: Optional[FlightDetailsReq] = field(
            default=None,
            metadata={
                "name": "FlightDetailsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class FlightDetailsPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightDetailsPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_details_rsp: Optional[FlightDetailsRsp] = field(
            default=None,
            metadata={
                "name": "FlightDetailsRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["FlightDetailsPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["FlightDetailsPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class FlightInfoPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightInfoPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_information_req: Optional[FlightInformationReq] = field(
            default=None,
            metadata={
                "name": "FlightInformationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class FlightInfoPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightInfoPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_information_rsp: Optional[FlightInformationRsp] = field(
            default=None,
            metadata={
                "name": "FlightInformationRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["FlightInfoPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["FlightInfoPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class FlightTimeTablePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightTimeTablePortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_time_table_req: Optional[FlightTimeTableReq] = field(
            default=None,
            metadata={
                "name": "FlightTimeTableReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class FlightTimeTablePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FlightTimeTablePortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_time_table_rsp: Optional[FlightTimeTableRsp] = field(
            default=None,
            metadata={
                "name": "FlightTimeTableRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["FlightTimeTablePortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["FlightTimeTablePortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
                )


@dataclass
class SeatMapPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["SeatMapPortTypeServiceInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["SeatMapPortTypeServiceInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: Optional[SessionContext] = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        seat_map_req: Optional[SeatMapReq] = field(
            default=None,
            metadata={
                "name": "SeatMapReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )


@dataclass
class SeatMapPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["SeatMapPortTypeServiceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        seat_map_rsp: Optional[SeatMapRsp] = field(
            default=None,
            metadata={
                "name": "SeatMapRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: Optional["SeatMapPortTypeServiceOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["SeatMapPortTypeServiceOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: Optional[ErrorInfo] = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v48_0",
                    }
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
