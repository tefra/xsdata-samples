from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TravelerInfoSummaryTpaExtensionsType:
    """
    Attributes:
        traveler_rating: Customer Value Scores and Frequent Flyer Tiers
            for one traveler. It can influence Availability results when
            provided.
    """

    class Meta:
        name = "TravelerInfoSummary_TPA_ExtensionsType"

    traveler_rating: list[
        TravelerInfoSummaryTpaExtensionsType.TravelerRating
    ] = field(
        default_factory=list,
        metadata={
            "name": "TravelerRating",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )

    @dataclass
    class TravelerRating:
        score: list[
            TravelerInfoSummaryTpaExtensionsType.TravelerRating.Score
        ] = field(
            default_factory=list,
            metadata={
                "name": "Score",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        frequent_flyer: list[
            TravelerInfoSummaryTpaExtensionsType.TravelerRating.FrequentFlyer
        ] = field(
            default_factory=list,
            metadata={
                "name": "FrequentFlyer",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass
        class Score:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )
            carrier: None | str = field(
                default=None,
                metadata={
                    "name": "Carrier",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class FrequentFlyer:
            tier: None | int = field(
                default=None,
                metadata={
                    "name": "Tier",
                    "type": "Attribute",
                    "required": True,
                },
            )
            carrier: None | str = field(
                default=None,
                metadata={
                    "name": "Carrier",
                    "type": "Attribute",
                    "required": True,
                },
            )
