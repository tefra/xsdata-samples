from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.departure_or_arrival import DepartureOrArrival
from sabre.models.outbound_or_inbound import OutboundOrInbound

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class DiversityControlType:
    """
    These parameters control how IntellSell should select itineraries based
    not necessarily on cheapest price, but also on other criteria that
    guarantee a diverse response.
    """

    low_fare_bucket: DiversityControlType.LowFareBucket = field(
        metadata={
            "name": "LowFareBucket",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    dimensions: DiversityControlType.Dimensions = field(
        metadata={
            "name": "Dimensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class LowFareBucket:
        options: None | str = field(
            default=None,
            metadata={
                "name": "Options",
                "type": "Attribute",
                "pattern": r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%",
            },
        )
        fare_cut_off: None | str = field(
            default=None,
            metadata={
                "name": "FareCutOff",
                "type": "Attribute",
                "pattern": r"(0|100|[1-9][0-9]?)%",
            },
        )

    @dataclass(kw_only=True)
    class Dimensions:
        travel_time: None | DiversityControlType.Dimensions.TravelTime = field(
            default=None,
            metadata={
                "name": "TravelTime",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        carrier: None | DiversityControlType.Dimensions.Carrier = field(
            default=None,
            metadata={
                "name": "Carrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        operating_duplicate: (
            None | DiversityControlType.Dimensions.OperatingDuplicate
        ) = field(
            default=None,
            metadata={
                "name": "OperatingDuplicate",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        inbound_outbound_pairing: (
            None | DiversityControlType.Dimensions.InboundOutboundPairing
        ) = field(
            default=None,
            metadata={
                "name": "InboundOutboundPairing",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        time_of_day: None | DiversityControlType.Dimensions.TimeOfDay = field(
            default=None,
            metadata={
                "name": "TimeOfDay",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        stops_number: None | DiversityControlType.Dimensions.StopsNumber = (
            field(
                default=None,
                metadata={
                    "name": "StopsNumber",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        price_weight: int = field(
            default=10,
            metadata={
                "name": "PriceWeight",
                "type": "Attribute",
                "min_inclusive": 0,
                "max_inclusive": 10,
            },
        )

        @dataclass(kw_only=True)
        class TravelTime:
            weight: int = field(
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )

        @dataclass(kw_only=True)
        class Carrier:
            default: None | DiversityControlType.Dimensions.Carrier.Default = (
                field(
                    default=None,
                    metadata={
                        "name": "Default",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
            )
            override: list[
                DiversityControlType.Dimensions.Carrier.Override
            ] = field(
                default_factory=list,
                metadata={
                    "name": "Override",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            weight: int = field(
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )
            online_indicator: bool = field(
                default=False,
                metadata={
                    "name": "OnlineIndicator",
                    "type": "Attribute",
                },
            )

            @dataclass(kw_only=True)
            class Default:
                options: str = field(
                    metadata={
                        "name": "Options",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%",
                    }
                )

            @dataclass(kw_only=True)
            class Override:
                code: str = field(
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9A-Z]{2,3}",
                    }
                )
                options: str = field(
                    metadata={
                        "name": "Options",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%",
                    }
                )

        @dataclass(kw_only=True)
        class OperatingDuplicate:
            preferred_carrier: list[
                DiversityControlType.Dimensions.OperatingDuplicate.PreferredCarrier
            ] = field(
                default_factory=list,
                metadata={
                    "name": "PreferredCarrier",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            weight: int = field(
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )

            @dataclass(kw_only=True)
            class PreferredCarrier:
                code: str = field(
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9A-Z]{2,3}",
                    }
                )

        @dataclass(kw_only=True)
        class InboundOutboundPairing:
            weight: int = field(
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )
            duplicates: int = field(
                default=1,
                metadata={
                    "name": "Duplicates",
                    "type": "Attribute",
                },
            )

        @dataclass(kw_only=True)
        class TimeOfDay:
            """
            Attributes:
                distribution: Exactly one attribute: either Direction or
                    Leg must be provided
                weight:
            """

            distribution: list[
                DiversityControlType.Dimensions.TimeOfDay.Distribution
            ] = field(
                default_factory=list,
                metadata={
                    "name": "Distribution",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            weight: int = field(
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )

            @dataclass(kw_only=True)
            class Distribution:
                range: list[
                    DiversityControlType.Dimensions.TimeOfDay.Distribution.Range
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "Range",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "max_occurs": 4,
                    },
                )
                direction: None | OutboundOrInbound = field(
                    default=None,
                    metadata={
                        "name": "Direction",
                        "type": "Attribute",
                    },
                )
                leg: None | int = field(
                    default=None,
                    metadata={
                        "name": "Leg",
                        "type": "Attribute",
                    },
                )
                endpoint: DepartureOrArrival = field(
                    default=DepartureOrArrival.DEPARTURE,
                    metadata={
                        "name": "Endpoint",
                        "type": "Attribute",
                    },
                )

                @dataclass(kw_only=True)
                class Range:
                    """
                    Either all Range elements shall contain attribute
                    Options or none.

                    Ranges shall not overlap.
                    """

                    begin: str = field(
                        metadata={
                            "name": "Begin",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]",
                        }
                    )
                    end: str = field(
                        metadata={
                            "name": "End",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]",
                        }
                    )
                    options: None | str = field(
                        default=None,
                        metadata={
                            "name": "Options",
                            "type": "Attribute",
                            "pattern": r"[1-9][0-9]*|0%?|100%|[1-9][0-9]?%",
                        },
                    )

        @dataclass(kw_only=True)
        class StopsNumber:
            weight: int = field(
                metadata={
                    "name": "Weight",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                }
            )
