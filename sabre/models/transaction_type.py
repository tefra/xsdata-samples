from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.company_name_pref_type import CompanyNamePrefType
from sabre.models.seat_status_sim_type import SeatStatusSimType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class TransactionType:
    """
    IntelliSell Type.

    Attributes:
        request_type: Identifier of the type of request.
        service_tag: Identifier of the transaction path.
        purchase_type: A target available for user, that can be used to
            create specific rules. For example, if the client wants to
            target preferred customer request, we can use this element
            to achieve this.
        sabre_ath: Sabre authentication ID (ATH) - passed into the
            request to keep session information when communicating with
            TPF. The use of this element had been deprecated and is
            achieved by session pooling mechanism in Intellisell.
        tran_id: Transaction ID.
        client_session_id: A unique identifier to relate all
            transactions within a single session. Used by AirShop/LFE
            transactions.
        branch: Attribute of the Rule that can be passed in to
            selectively target a rule. This has been deprecated.
        compress_response: Decides if the response should be compressed.
        fare_overrides: Contains a sequence of fare overrides.
        diagnostics: For internal use
        subagent_data: Subagent data for LFE transactions.
        response_sorting: Settings for IntelliSell merchandising
        seat_status_sim:
        available_level:
        atsetest: Allows ATSE Team to test new features. This element
            and its content is meant to never be published.
        debug: Turns on or off debug mode.
        debug_key: Key unlocking disabled debug mode.
        config_set: Alternative configuration selector.
        disable_cache: Disables itinerary cache for this request (if it
            is enabled in this service).
        chunk_number: Helps Forwarder in keeping track of response parts
            generated as a result of request processing (AB only).
        show_itin_source: If enabled, Intellisell will return source for
            each itinerary.
    """

    request_type: None | TransactionType.RequestType = field(
        default=None,
        metadata={
            "name": "RequestType",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    service_tag: None | TransactionType.ServiceTag = field(
        default=None,
        metadata={
            "name": "ServiceTag",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    purchase_type: None | TransactionType.PurchaseType = field(
        default=None,
        metadata={
            "name": "PurchaseType",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    sabre_ath: None | TransactionType.SabreAth = field(
        default=None,
        metadata={
            "name": "SabreAth",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    tran_id: None | TransactionType.TranId = field(
        default=None,
        metadata={
            "name": "TranID",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    client_session_id: None | TransactionType.ClientSessionId = field(
        default=None,
        metadata={
            "name": "ClientSessionID",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    branch: None | TransactionType.Branch = field(
        default=None,
        metadata={
            "name": "Branch",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    compress_response: None | TransactionType.CompressResponse = field(
        default=None,
        metadata={
            "name": "CompressResponse",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    fare_overrides: None | TransactionType.FareOverrides = field(
        default=None,
        metadata={
            "name": "FareOverrides",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    diagnostics: None | TransactionType.Diagnostics = field(
        default=None,
        metadata={
            "name": "Diagnostics",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    subagent_data: None | TransactionType.SubagentData = field(
        default=None,
        metadata={
            "name": "SubagentData",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    response_sorting: None | TransactionType.ResponseSorting = field(
        default=None,
        metadata={
            "name": "ResponseSorting",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    seat_status_sim: None | SeatStatusSimType = field(
        default=None,
        metadata={
            "name": "SeatStatusSim",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    available_level: None | TransactionType.AvailableLevel = field(
        default=None,
        metadata={
            "name": "AvailableLevel",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    atsetest: None | TransactionType.Atsetest = field(
        default=None,
        metadata={
            "name": "ATSETest",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    debug: None | bool = field(
        default=None,
        metadata={
            "name": "Debug",
            "type": "Attribute",
        },
    )
    debug_key: None | str = field(
        default=None,
        metadata={
            "name": "DebugKey",
            "type": "Attribute",
        },
    )
    config_set: None | str = field(
        default=None,
        metadata={
            "name": "ConfigSet",
            "type": "Attribute",
        },
    )
    disable_cache: None | bool = field(
        default=None,
        metadata={
            "name": "DisableCache",
            "type": "Attribute",
        },
    )
    chunk_number: None | str = field(
        default=None,
        metadata={
            "name": "ChunkNumber",
            "type": "Attribute",
        },
    )
    show_itin_source: None | bool = field(
        default=None,
        metadata={
            "name": "ShowItinSource",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class RequestType:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class ServiceTag:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class PurchaseType:
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class SabreAth:
        value: None | str = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
            },
        )
        binary_sec_token: None | str = field(
            default=None,
            metadata={
                "name": "BinarySecToken",
                "type": "Attribute",
            },
        )
        conversation_id: None | str = field(
            default=None,
            metadata={
                "name": "ConversationID",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class TranId:
        value: None | str = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class ClientSessionId:
        value: None | str = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class Branch:
        name: str = field(
            default="Main",
            metadata={
                "name": "Name",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class CompressResponse:
        value: bool = field(
            default=False,
            metadata={
                "name": "Value",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class FareOverrides:
        """
        Attributes:
            fare_override: Contains attributes of the FareGroup
                functionality used during shopping and pricing. If
                passed in this request, it will override setting in the
                rule.
        """

        fare_override: list[TransactionType.FareOverrides.FareOverride] = (
            field(
                default_factory=list,
                metadata={
                    "name": "FareOverride",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                    "max_occurs": 4,
                },
            )
        )

        @dataclass(kw_only=True)
        class FareOverride:
            """
            Attributes:
                vendor_pref: Specify vendors to include and exclude from
                    the response.
                tpa_extensions: This is a place holder for additional
                    elements.
                fare_type: Attribute of FareGroup functionality, used in
                    search of fares during shopping.
                pseudo_city_code:
                corporate_id: Attribute of FareGroup functionality, used
                    in search of fares during shopping.
                callable: Indicator to enable/disable this FareOverride.
            """

            vendor_pref: list[CompanyNamePrefType] = field(
                default_factory=list,
                metadata={
                    "name": "VendorPref",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            tpa_extensions: None | str = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            fare_type: str = field(
                metadata={
                    "name": "FareType",
                    "type": "Attribute",
                    "required": True,
                }
            )
            pseudo_city_code: None | str = field(
                default=None,
                metadata={
                    "name": "PseudoCityCode",
                    "type": "Attribute",
                },
            )
            corporate_id: None | str = field(
                default=None,
                metadata={
                    "name": "CorporateID",
                    "type": "Attribute",
                },
            )
            callable: str = field(
                default="true",
                metadata={
                    "name": "Callable",
                    "type": "Attribute",
                },
            )

    @dataclass(kw_only=True)
    class Diagnostics:
        """
        Attributes:
            diagnostic: Specify diagnostic code and which service to
                sent it to.
        """

        diagnostic: list[TransactionType.Diagnostics.Diagnostic] = field(
            default_factory=list,
            metadata={
                "name": "Diagnostic",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Diagnostic:
            """
            Attributes:
                diagnostic_argument: Name-value pairs to be used as
                    arguments for the diagnostic.
                tpa_extensions: This is a place holder for additional
                    elements.
                target:
                code:
            """

            diagnostic_argument: list[
                TransactionType.Diagnostics.Diagnostic.DiagnosticArgument
            ] = field(
                default_factory=list,
                metadata={
                    "name": "DiagnosticArgument",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            tpa_extensions: None | str = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            target: None | str = field(
                default=None,
                metadata={
                    "name": "Target",
                    "type": "Attribute",
                },
            )
            code: str = field(
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[A-Za-z0-9_]+(/[A-Za-z0-9_]+)*",
                }
            )

            @dataclass(kw_only=True)
            class DiagnosticArgument:
                name: str = field(
                    metadata={
                        "name": "Name",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                value: None | str = field(
                    default=None,
                    metadata={
                        "name": "Value",
                        "type": "Attribute",
                    },
                )

    @dataclass(kw_only=True)
    class SubagentData:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class ResponseSorting:
        enable_chronological_sorting: None | bool = field(
            default=None,
            metadata={
                "name": "EnableChronologicalSorting",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class AvailableLevel:
        value: str = field(
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Atsetest:
        """
        Attributes:
            feature: Meaning of that attribute is dependent on MIP Team,
                ISell sends it in all ShoppingRequests when specified.
        """

        feature: None | str = field(
            default=None,
            metadata={
                "name": "Feature",
                "type": "Attribute",
            },
        )
