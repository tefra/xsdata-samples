from __future__ import annotations
from dataclasses import dataclass, field
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

    header: None | AirAvailabilitySearchPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | AirAvailabilitySearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        availability_search_req: None | AvailabilitySearchReq = field(
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

    body: None | AirAvailabilitySearchPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        availability_search_rsp: None | AvailabilitySearchRsp = field(
            default=None,
            metadata={
                "name": "AvailabilitySearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirAvailabilitySearchPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirAvailabilitySearchPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirExchangeEligibilityPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_eligibility_req: None | AirExchangeEligibilityReq = field(
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

    body: None | AirExchangeEligibilityPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_eligibility_rsp: None | AirExchangeEligibilityRsp = field(
            default=None,
            metadata={
                "name": "AirExchangeEligibilityRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirExchangeEligibilityPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirExchangeEligibilityPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirExchangeMultiQuotePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_multi_quote_req: None | AirExchangeMultiQuoteReq = field(
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

    body: None | AirExchangeMultiQuotePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_multi_quote_rsp: None | AirExchangeMultiQuoteRsp = field(
            default=None,
            metadata={
                "name": "AirExchangeMultiQuoteRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirExchangeMultiQuotePortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirExchangeMultiQuotePortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirExchangeProcessPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_req: None | AirExchangeReq = field(
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

    body: None | AirExchangeProcessPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_rsp: None | AirExchangeRsp = field(
            default=None,
            metadata={
                "name": "AirExchangeRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirExchangeProcessPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirExchangeProcessPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirExchangeQuotePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_quote_req: None | AirExchangeQuoteReq = field(
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

    body: None | AirExchangeQuotePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_quote_rsp: None | AirExchangeQuoteRsp = field(
            default=None,
            metadata={
                "name": "AirExchangeQuoteRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirExchangeQuotePortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirExchangeQuotePortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    header: None | AirExchangeTicketingPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | AirExchangeTicketingPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        air_exchange_ticketing_req: None | AirExchangeTicketingReq = field(
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

    body: None | AirExchangeTicketingPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_exchange_ticketing_rsp: None | AirExchangeTicketingRsp = field(
            default=None,
            metadata={
                "name": "AirExchangeTicketingRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirExchangeTicketingPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirExchangeTicketingPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    header: None | AirFareDisplayPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | AirFareDisplayPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        air_fare_display_req: None | AirFareDisplayReq = field(
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

    body: None | AirFareDisplayPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_fare_display_rsp: None | AirFareDisplayRsp = field(
            default=None,
            metadata={
                "name": "AirFareDisplayRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirFareDisplayPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirFareDisplayPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    header: None | AirFareRulesPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | AirFareRulesPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        air_fare_rules_req: None | AirFareRulesReq = field(
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

    body: None | AirFareRulesPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_fare_rules_rsp: None | AirFareRulesRsp = field(
            default=None,
            metadata={
                "name": "AirFareRulesRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirFareRulesPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirFareRulesPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirLowFareSearchAsynchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        low_fare_search_asynch_req: None | LowFareSearchAsynchReq = field(
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

    body: None | AirLowFareSearchAsynchPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        low_fare_search_asynch_rsp: None | LowFareSearchAsynchRsp = field(
            default=None,
            metadata={
                "name": "LowFareSearchAsynchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirLowFareSearchAsynchPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirLowFareSearchAsynchPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    header: None | AirLowFareSearchPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | AirLowFareSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        low_fare_search_req: None | LowFareSearchReq = field(
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

    body: None | AirLowFareSearchPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        low_fare_search_rsp: None | LowFareSearchRsp = field(
            default=None,
            metadata={
                "name": "LowFareSearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirLowFareSearchPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirLowFareSearchPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirMerchandisingDetailsPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_merchandising_details_req: None | AirMerchandisingDetailsReq = field(
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

    body: None | AirMerchandisingDetailsPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_merchandising_details_rsp: None | AirMerchandisingDetailsRsp = field(
            default=None,
            metadata={
                "name": "AirMerchandisingDetailsRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirMerchandisingDetailsPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirMerchandisingDetailsPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirMerchandisingOfferAvailabilityPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_merchandising_offer_availability_req: None | AirMerchandisingOfferAvailabilityReq = field(
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

    body: None | AirMerchandisingOfferAvailabilityPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_merchandising_offer_availability_rsp: None | AirMerchandisingOfferAvailabilityRsp = field(
            default=None,
            metadata={
                "name": "AirMerchandisingOfferAvailabilityRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirMerchandisingOfferAvailabilityPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirMerchandisingOfferAvailabilityPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirPrePayPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_pre_pay_req: None | AirPrePayReq = field(
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

    body: None | AirPrePayPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_pre_pay_rsp: None | AirPrePayRsp = field(
            default=None,
            metadata={
                "name": "AirPrePayRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirPrePayPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirPrePayPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    header: None | AirPricePortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | AirPricePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        air_price_req: None | AirPriceReq = field(
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

    body: None | AirPricePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_price_rsp: None | AirPriceRsp = field(
            default=None,
            metadata={
                "name": "AirPriceRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirPricePortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirPricePortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirRefundQuotePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_quote_req: None | AirRefundQuoteReq = field(
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

    body: None | AirRefundQuotePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_quote_rsp: None | AirRefundQuoteRsp = field(
            default=None,
            metadata={
                "name": "AirRefundQuoteRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirRefundQuotePortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirRefundQuotePortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirRefundTicketPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_req: None | AirRefundReq = field(
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

    body: None | AirRefundTicketPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_refund_rsp: None | AirRefundRsp = field(
            default=None,
            metadata={
                "name": "AirRefundRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirRefundTicketPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirRefundTicketPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirRepriceSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_reprice_req: None | AirRepriceReq = field(
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

    body: None | AirRepriceSearchPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_reprice_rsp: None | AirRepriceRsp = field(
            default=None,
            metadata={
                "name": "AirRepriceRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirRepriceSearchPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirRepriceSearchPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirRetrieveDocumentPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_retrieve_document_req: None | AirRetrieveDocumentReq = field(
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

    body: None | AirRetrieveDocumentPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_retrieve_document_rsp: None | AirRetrieveDocumentRsp = field(
            default=None,
            metadata={
                "name": "AirRetrieveDocumentRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirRetrieveDocumentPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirRetrieveDocumentPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirRetrieveLowFareSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        retrieve_low_fare_search_req: None | RetrieveLowFareSearchReq = field(
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

    body: None | AirRetrieveLowFareSearchPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        retrieve_low_fare_search_rsp: None | RetrieveLowFareSearchRsp = field(
            default=None,
            metadata={
                "name": "RetrieveLowFareSearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirRetrieveLowFareSearchPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirRetrieveLowFareSearchPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirScheduleSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        schedule_search_req: None | ScheduleSearchReq = field(
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

    body: None | AirScheduleSearchPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        schedule_search_rsp: None | ScheduleSearchRsp = field(
            default=None,
            metadata={
                "name": "ScheduleSearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirScheduleSearchPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirScheduleSearchPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirTicketingPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_ticketing_req: None | AirTicketingReq = field(
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

    body: None | AirTicketingPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_ticketing_rsp: None | AirTicketingRsp = field(
            default=None,
            metadata={
                "name": "AirTicketingRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirTicketingPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirTicketingPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirUpsellSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_upsell_search_req: None | AirUpsellSearchReq = field(
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

    body: None | AirUpsellSearchPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_upsell_search_rsp: None | AirUpsellSearchRsp = field(
            default=None,
            metadata={
                "name": "AirUpsellSearchRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirUpsellSearchPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirUpsellSearchPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | AirVoidDocumentPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_void_document_req: None | AirVoidDocumentReq = field(
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

    body: None | AirVoidDocumentPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_void_document_rsp: None | AirVoidDocumentRsp = field(
            default=None,
            metadata={
                "name": "AirVoidDocumentRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | AirVoidDocumentPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | AirVoidDocumentPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | EmdissuancePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdissuance_req: None | EmdissuanceReq = field(
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

    body: None | EmdissuancePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdissuance_rsp: None | EmdissuanceRsp = field(
            default=None,
            metadata={
                "name": "EMDIssuanceRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | EmdissuancePortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | EmdissuancePortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | EmdretrievePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdretrieve_req: None | EmdretrieveReq = field(
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

    body: None | EmdretrievePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        emdretrieve_rsp: None | EmdretrieveRsp = field(
            default=None,
            metadata={
                "name": "EMDRetrieveRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | EmdretrievePortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | EmdretrievePortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | FlightDetailsPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_details_req: None | FlightDetailsReq = field(
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

    body: None | FlightDetailsPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_details_rsp: None | FlightDetailsRsp = field(
            default=None,
            metadata={
                "name": "FlightDetailsRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | FlightDetailsPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | FlightDetailsPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | FlightInfoPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_information_req: None | FlightInformationReq = field(
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

    body: None | FlightInfoPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_information_rsp: None | FlightInformationRsp = field(
            default=None,
            metadata={
                "name": "FlightInformationRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | FlightInfoPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | FlightInfoPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    body: None | FlightTimeTablePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_time_table_req: None | FlightTimeTableReq = field(
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

    body: None | FlightTimeTablePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        flight_time_table_rsp: None | FlightTimeTableRsp = field(
            default=None,
            metadata={
                "name": "FlightTimeTableRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | FlightTimeTablePortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | FlightTimeTablePortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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

    header: None | SeatMapPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | SeatMapPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass
    class Body:
        seat_map_req: None | SeatMapReq = field(
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

    body: None | SeatMapPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        seat_map_rsp: None | SeatMapRsp = field(
            default=None,
            metadata={
                "name": "SeatMapRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v48_0",
            }
        )
        fault: None | SeatMapPortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: None | SeatMapPortTypeServiceOutput.Body.Fault.Detail = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo = field(
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
