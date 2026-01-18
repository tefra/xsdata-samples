from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.company_name_type import CompanyNameType
from sabre.models.complex_processing_message_type import (
    ComplexProcessingMessageType,
)
from sabre.models.errors_type import ErrorsType
from sabre.models.one_way_processing_message_type import (
    OneWayProcessingMessageType,
)
from sabre.models.ota_air_low_fare_search_rs_target import (
    OtaAirLowFareSearchRsTarget,
)
from sabre.models.ota_air_low_fare_search_rs_transaction_status_code import (
    OtaAirLowFareSearchRsTransactionStatusCode,
)
from sabre.models.priced_itinerary_type import PricedItineraryType
from sabre.models.success_type import SuccessType
from sabre.models.warnings_type import WarningsType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class OtaAirLowFareSearchRs:
    """
    The Low Fare Search Response message contains a number of .Priced
    Itinerary. options.

    Each includes: - A set of available flights matching the client.s
    request. - Pricing information including taxes and full fare breakdown
    for each passenger type - Ticketing information - Fare Basis Codes and
    the information necessary to make a rules entry. This message contains
    similar information to a standard airline CRS or GDS Low Fare Search
    Response message.

    Attributes:
        errors: In case of failure errors are returned.
        success: In case of success this element is returned.
        warnings: In case of any warnings this element is returned.
        priced_itineraries: Low Fare priced itineraries container.
        one_way_itineraries: Successfull Low Fare priced itineraries in
            response to a Simplified One Way request.
        departed_itineraries: Departed Itineraries
        sold_out_itineraries: Sold Out Itineraries
        available_itineraries: Available Itineraries
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        echo_token: A sequence number for additional message
            identification, assigned by the requesting host system. When
            a request message includes an echo token the corresponding
            response message MUST include an echo token with an
            identical value.
        time_stamp: Indicates the creation date and time of the message
            in UTC using the following format specified by ISO 8601;
            YYYY-MM-DDThh:mm:ssZ with time values using the 24 hour
            clock (e.g. 20 November 2003, 1:59:38 pm UTC becomes
            2003-11-20T13:59:38Z).
        target: Used to indicate whether the request is for the Test or
            Production system.
        version: For all OTA versioned messages, the version of the
            message is indicated by a decimal value.
        transaction_identifier: A unique identifier to relate all
            messages within a transaction (e.g. this would be sent in
            all request and response messages that are part of an on-
            going transaction).
        sequence_nmbr: Used to identify the sequence number of the
            transaction as assigned by the sending system; allows for an
            application to process messages in a certain order or to
            request a resynchronization of messages in the event that a
            system has been off-line and needs to retrieve messages that
            were missed.
        transaction_status_code: This indicates where this message falls
            within a sequence of messages.
        primary_lang_id: Identifes the primary language preference for
            the form of travel represented in a collection. The human
            language is identified by ISO 639 codes.
        alt_lang_id:
        priced_itin_count: Itinerary count for Priced Round-Trip
            itineraries
        branded_one_way_itin_count: Itinerary count for Branded One-Way
            itineraries
        simple_one_way_itin_count: Itinerary count for Simple One-Way
            itineraries
        departed_itin_count: Itinerary count for departed itineraries
            returned
        sold_out_itin_count: Itinerary count for sold out itineraries
            returned
        available_itin_count: Itinerary count for available itineraries
            returned
    """

    class Meta:
        name = "OTA_AirLowFareSearchRS"
        namespace = "http://www.opentravel.org/OTA/2003/05"

    errors: None | ErrorsType = field(
        default=None,
        metadata={
            "name": "Errors",
            "type": "Element",
        },
    )
    success: None | SuccessType = field(
        default=None,
        metadata={
            "name": "Success",
            "type": "Element",
        },
    )
    warnings: None | WarningsType = field(
        default=None,
        metadata={
            "name": "Warnings",
            "type": "Element",
        },
    )
    priced_itineraries: None | OtaAirLowFareSearchRs.PricedItineraries = field(
        default=None,
        metadata={
            "name": "PricedItineraries",
            "type": "Element",
        },
    )
    one_way_itineraries: None | OtaAirLowFareSearchRs.OneWayItineraries = (
        field(
            default=None,
            metadata={
                "name": "OneWayItineraries",
                "type": "Element",
            },
        )
    )
    departed_itineraries: None | OtaAirLowFareSearchRs.DepartedItineraries = (
        field(
            default=None,
            metadata={
                "name": "DepartedItineraries",
                "type": "Element",
            },
        )
    )
    sold_out_itineraries: None | OtaAirLowFareSearchRs.SoldOutItineraries = (
        field(
            default=None,
            metadata={
                "name": "SoldOutItineraries",
                "type": "Element",
            },
        )
    )
    available_itineraries: (
        None | OtaAirLowFareSearchRs.AvailableItineraries
    ) = field(
        default=None,
        metadata={
            "name": "AvailableItineraries",
            "type": "Element",
        },
    )
    tpa_extensions: None | OtaAirLowFareSearchRs.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
        },
    )
    echo_token: None | str = field(
        default=None,
        metadata={
            "name": "EchoToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    time_stamp: None | str = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
        },
    )
    target: OtaAirLowFareSearchRsTarget = field(
        default=OtaAirLowFareSearchRsTarget.PRODUCTION,
        metadata={
            "name": "Target",
            "type": "Attribute",
        },
    )
    version: str = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
    transaction_identifier: None | str = field(
        default=None,
        metadata={
            "name": "TransactionIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    sequence_nmbr: None | int | bool = field(
        default=None,
        metadata={
            "name": "SequenceNmbr",
            "type": "Attribute",
        },
    )
    transaction_status_code: (
        None | OtaAirLowFareSearchRsTransactionStatusCode
    ) = field(
        default=None,
        metadata={
            "name": "TransactionStatusCode",
            "type": "Attribute",
        },
    )
    primary_lang_id: None | str = field(
        default=None,
        metadata={
            "name": "PrimaryLangID",
            "type": "Attribute",
        },
    )
    alt_lang_id: None | str = field(
        default=None,
        metadata={
            "name": "AltLangID",
            "type": "Attribute",
        },
    )
    priced_itin_count: None | int = field(
        default=None,
        metadata={
            "name": "PricedItinCount",
            "type": "Attribute",
        },
    )
    branded_one_way_itin_count: None | int = field(
        default=None,
        metadata={
            "name": "BrandedOneWayItinCount",
            "type": "Attribute",
        },
    )
    simple_one_way_itin_count: None | int = field(
        default=None,
        metadata={
            "name": "SimpleOneWayItinCount",
            "type": "Attribute",
        },
    )
    departed_itin_count: None | int = field(
        default=None,
        metadata={
            "name": "DepartedItinCount",
            "type": "Attribute",
        },
    )
    sold_out_itin_count: None | int = field(
        default=None,
        metadata={
            "name": "SoldOutItinCount",
            "type": "Attribute",
        },
    )
    available_itin_count: None | int = field(
        default=None,
        metadata={
            "name": "AvailableItinCount",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class PricedItineraries:
        """
        Attributes:
            tpa_extensions:
            priced_itinerary: Successfull Low Fare priced itineraries in
                response to a Low Fare Search request.
        """

        tpa_extensions: (
            None | OtaAirLowFareSearchRs.PricedItineraries.TpaExtensions
        ) = field(
            default=None,
            metadata={
                "name": "TPA_Extensions",
                "type": "Element",
            },
        )
        priced_itinerary: list[PricedItineraryType] = field(
            default_factory=list,
            metadata={
                "name": "PricedItinerary",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class TpaExtensions:
            """
            Attributes:
                processing_message: Container for itinerary message
                    type.
            """

            processing_message: list[ComplexProcessingMessageType] = field(
                default_factory=list,
                metadata={
                    "name": "ProcessingMessage",
                    "type": "Element",
                },
            )

    @dataclass(kw_only=True)
    class OneWayItineraries:
        """
        Attributes:
            branded_one_way_itineraries: Container for priced
                itineraries assigned to particular leg.
            simple_one_way_itineraries: Container for priced itineraries
                assigned to particular leg.
        """

        branded_one_way_itineraries: list[
            OtaAirLowFareSearchRs.OneWayItineraries.BrandedOneWayItineraries
        ] = field(
            default_factory=list,
            metadata={
                "name": "BrandedOneWayItineraries",
                "type": "Element",
                "max_occurs": 10,
            },
        )
        simple_one_way_itineraries: list[
            OtaAirLowFareSearchRs.OneWayItineraries.SimpleOneWayItineraries
        ] = field(
            default_factory=list,
            metadata={
                "name": "SimpleOneWayItineraries",
                "type": "Element",
                "max_occurs": 10,
            },
        )

        @dataclass(kw_only=True)
        class BrandedOneWayItineraries:
            """
            Attributes:
                tpa_extensions:
                priced_itinerary: Container for priced itinerary type.
                rph: Leg ID from request.
            """

            tpa_extensions: (
                None
                | OtaAirLowFareSearchRs.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions
            ) = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                },
            )
            priced_itinerary: list[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                },
            )
            rph: str = field(
                metadata={
                    "name": "RPH",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{1,8}",
                }
            )

            @dataclass(kw_only=True)
            class TpaExtensions:
                """
                Attributes:
                    processing_message: Container for itinerary message
                        type.
                """

                processing_message: list[OneWayProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    },
                )

        @dataclass(kw_only=True)
        class SimpleOneWayItineraries:
            """
            Attributes:
                tpa_extensions:
                priced_itinerary: Container for priced itinerary type.
                rph: Leg ID from request.
            """

            tpa_extensions: (
                None
                | OtaAirLowFareSearchRs.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions
            ) = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                },
            )
            priced_itinerary: list[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                },
            )
            rph: str = field(
                metadata={
                    "name": "RPH",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{1,8}",
                }
            )

            @dataclass(kw_only=True)
            class TpaExtensions:
                """
                Attributes:
                    processing_message: Container for itinerary message
                        type.
                """

                processing_message: list[OneWayProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    },
                )

    @dataclass(kw_only=True)
    class DepartedItineraries:
        """
        Attributes:
            priced_itineraries: Low Fare priced itineraries container.
            one_way_itineraries: Successfull Low Fare priced itineraries
                in response to a Simplified One Way request.
        """

        priced_itineraries: (
            None | OtaAirLowFareSearchRs.DepartedItineraries.PricedItineraries
        ) = field(
            default=None,
            metadata={
                "name": "PricedItineraries",
                "type": "Element",
            },
        )
        one_way_itineraries: (
            None | OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries
        ) = field(
            default=None,
            metadata={
                "name": "OneWayItineraries",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class PricedItineraries:
            """
            Attributes:
                tpa_extensions:
                priced_itinerary: Successfull Low Fare priced
                    itineraries in response to a Low Fare Search
                    request.
            """

            tpa_extensions: (
                None
                | OtaAirLowFareSearchRs.DepartedItineraries.PricedItineraries.TpaExtensions
            ) = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                },
            )
            priced_itinerary: list[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class TpaExtensions:
                """
                Attributes:
                    processing_message: Container for itinerary message
                        type.
                """

                processing_message: list[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    },
                )

        @dataclass(kw_only=True)
        class OneWayItineraries:
            """
            Attributes:
                branded_one_way_itineraries: Container for priced
                    itineraries assigned to particular leg.
                simple_one_way_itineraries: Container for priced
                    itineraries assigned to particular leg.
            """

            branded_one_way_itineraries: list[
                OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.BrandedOneWayItineraries
            ] = field(
                default_factory=list,
                metadata={
                    "name": "BrandedOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                },
            )
            simple_one_way_itineraries: list[
                OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.SimpleOneWayItineraries
            ] = field(
                default_factory=list,
                metadata={
                    "name": "SimpleOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                },
            )

            @dataclass(kw_only=True)
            class BrandedOneWayItineraries:
                """
                Attributes:
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary
                        type.
                    rph: Leg ID from request.
                """

                tpa_extensions: (
                    None
                    | OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions
                ) = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    },
                )
                priced_itinerary: list[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    },
                )
                rph: str = field(
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass(kw_only=True)
                class TpaExtensions:
                    """
                    Attributes:
                        processing_message: Container for itinerary
                            message type.
                    """

                    processing_message: list[OneWayProcessingMessageType] = (
                        field(
                            default_factory=list,
                            metadata={
                                "name": "ProcessingMessage",
                                "type": "Element",
                            },
                        )
                    )

            @dataclass(kw_only=True)
            class SimpleOneWayItineraries:
                """
                Attributes:
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary
                        type.
                    rph: Leg ID from request.
                """

                tpa_extensions: (
                    None
                    | OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions
                ) = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    },
                )
                priced_itinerary: list[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    },
                )
                rph: str = field(
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass(kw_only=True)
                class TpaExtensions:
                    """
                    Attributes:
                        processing_message: Container for itinerary
                            message type.
                    """

                    processing_message: list[OneWayProcessingMessageType] = (
                        field(
                            default_factory=list,
                            metadata={
                                "name": "ProcessingMessage",
                                "type": "Element",
                            },
                        )
                    )

    @dataclass(kw_only=True)
    class SoldOutItineraries:
        """
        Attributes:
            priced_itineraries: Low Fare priced itineraries container.
            one_way_itineraries: Successfull Low Fare priced itineraries
                in response to a Simplified One Way request.
        """

        priced_itineraries: (
            None | OtaAirLowFareSearchRs.SoldOutItineraries.PricedItineraries
        ) = field(
            default=None,
            metadata={
                "name": "PricedItineraries",
                "type": "Element",
            },
        )
        one_way_itineraries: (
            None | OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries
        ) = field(
            default=None,
            metadata={
                "name": "OneWayItineraries",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class PricedItineraries:
            """
            Attributes:
                tpa_extensions:
                priced_itinerary: Successfull Low Fare priced
                    itineraries in response to a Low Fare Search
                    request.
            """

            tpa_extensions: (
                None
                | OtaAirLowFareSearchRs.SoldOutItineraries.PricedItineraries.TpaExtensions
            ) = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                },
            )
            priced_itinerary: list[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class TpaExtensions:
                """
                Attributes:
                    processing_message: Container for itinerary message
                        type.
                """

                processing_message: list[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    },
                )

        @dataclass(kw_only=True)
        class OneWayItineraries:
            """
            Attributes:
                branded_one_way_itineraries: Container for priced
                    itineraries assigned to particular leg.
                simple_one_way_itineraries: Container for priced
                    itineraries assigned to particular leg.
            """

            branded_one_way_itineraries: list[
                OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.BrandedOneWayItineraries
            ] = field(
                default_factory=list,
                metadata={
                    "name": "BrandedOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                },
            )
            simple_one_way_itineraries: list[
                OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.SimpleOneWayItineraries
            ] = field(
                default_factory=list,
                metadata={
                    "name": "SimpleOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                },
            )

            @dataclass(kw_only=True)
            class BrandedOneWayItineraries:
                """
                Attributes:
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary
                        type.
                    rph: Leg ID from request.
                """

                tpa_extensions: (
                    None
                    | OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions
                ) = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    },
                )
                priced_itinerary: list[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    },
                )
                rph: str = field(
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass(kw_only=True)
                class TpaExtensions:
                    """
                    Attributes:
                        processing_message: Container for itinerary
                            message type.
                    """

                    processing_message: list[OneWayProcessingMessageType] = (
                        field(
                            default_factory=list,
                            metadata={
                                "name": "ProcessingMessage",
                                "type": "Element",
                            },
                        )
                    )

            @dataclass(kw_only=True)
            class SimpleOneWayItineraries:
                """
                Attributes:
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary
                        type.
                    rph: Leg ID from request.
                """

                tpa_extensions: (
                    None
                    | OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions
                ) = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    },
                )
                priced_itinerary: list[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    },
                )
                rph: str = field(
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass(kw_only=True)
                class TpaExtensions:
                    """
                    Attributes:
                        processing_message: Container for itinerary
                            message type.
                    """

                    processing_message: list[OneWayProcessingMessageType] = (
                        field(
                            default_factory=list,
                            metadata={
                                "name": "ProcessingMessage",
                                "type": "Element",
                            },
                        )
                    )

    @dataclass(kw_only=True)
    class AvailableItineraries:
        """
        Attributes:
            priced_itineraries: Low Fare priced itineraries container.
            one_way_itineraries: Successfull Low Fare priced itineraries
                in response to a Simplified One Way request.
        """

        priced_itineraries: (
            None | OtaAirLowFareSearchRs.AvailableItineraries.PricedItineraries
        ) = field(
            default=None,
            metadata={
                "name": "PricedItineraries",
                "type": "Element",
            },
        )
        one_way_itineraries: (
            None | OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries
        ) = field(
            default=None,
            metadata={
                "name": "OneWayItineraries",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class PricedItineraries:
            """
            Attributes:
                tpa_extensions:
                priced_itinerary: Successfull Low Fare priced
                    itineraries in response to a Low Fare Search
                    request.
            """

            tpa_extensions: (
                None
                | OtaAirLowFareSearchRs.AvailableItineraries.PricedItineraries.TpaExtensions
            ) = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                },
            )
            priced_itinerary: list[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class TpaExtensions:
                """
                Attributes:
                    processing_message: Container for itinerary message
                        type.
                """

                processing_message: list[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    },
                )

        @dataclass(kw_only=True)
        class OneWayItineraries:
            """
            Attributes:
                branded_one_way_itineraries: Container for priced
                    itineraries assigned to particular leg.
                simple_one_way_itineraries: Container for priced
                    itineraries assigned to particular leg.
            """

            branded_one_way_itineraries: list[
                OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.BrandedOneWayItineraries
            ] = field(
                default_factory=list,
                metadata={
                    "name": "BrandedOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                },
            )
            simple_one_way_itineraries: list[
                OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.SimpleOneWayItineraries
            ] = field(
                default_factory=list,
                metadata={
                    "name": "SimpleOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                },
            )

            @dataclass(kw_only=True)
            class BrandedOneWayItineraries:
                """
                Attributes:
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary
                        type.
                    rph: Leg ID from request.
                """

                tpa_extensions: (
                    None
                    | OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions
                ) = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    },
                )
                priced_itinerary: list[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    },
                )
                rph: str = field(
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass(kw_only=True)
                class TpaExtensions:
                    """
                    Attributes:
                        processing_message: Container for itinerary
                            message type.
                    """

                    processing_message: list[OneWayProcessingMessageType] = (
                        field(
                            default_factory=list,
                            metadata={
                                "name": "ProcessingMessage",
                                "type": "Element",
                            },
                        )
                    )

            @dataclass(kw_only=True)
            class SimpleOneWayItineraries:
                """
                Attributes:
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary
                        type.
                    rph: Leg ID from request.
                """

                tpa_extensions: (
                    None
                    | OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions
                ) = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    },
                )
                priced_itinerary: list[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    },
                )
                rph: str = field(
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass(kw_only=True)
                class TpaExtensions:
                    """
                    Attributes:
                        processing_message: Container for itinerary
                            message type.
                    """

                    processing_message: list[OneWayProcessingMessageType] = (
                        field(
                            default_factory=list,
                            metadata={
                                "name": "ProcessingMessage",
                                "type": "Element",
                            },
                        )
                    )

    @dataclass(kw_only=True)
    class TpaExtensions:
        airline_order_list: (
            None | OtaAirLowFareSearchRs.TpaExtensions.AirlineOrderList
        ) = field(
            default=None,
            metadata={
                "name": "AirlineOrderList",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class AirlineOrderList:
            """
            Attributes:
                airline_order: The airline that filed the fare(s).
            """

            airline_order: list[
                OtaAirLowFareSearchRs.TpaExtensions.AirlineOrderList.AirlineOrder
            ] = field(
                default_factory=list,
                metadata={
                    "name": "AirlineOrder",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class AirlineOrder(CompanyNameType):
                sequence_number: int = field(
                    metadata={
                        "name": "SequenceNumber",
                        "type": "Attribute",
                        "required": True,
                    }
                )
