from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
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

        @dataclass(kw_only=True)
        class Score:
            value: int = field(
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )
            carrier: str = field(
                metadata={
                    "name": "Carrier",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class FrequentFlyer:
            tier: int = field(
                metadata={
                    "name": "Tier",
                    "type": "Attribute",
                    "required": True,
                }
            )
            carrier: str = field(
                metadata={
                    "name": "Carrier",
                    "type": "Attribute",
                    "required": True,
                }
            )
