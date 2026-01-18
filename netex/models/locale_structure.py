from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal

from .language_usage_structure import LanguageUsageStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LocaleStructure:
    time_zone_offset: Decimal | None = field(
        default=None,
        metadata={
            "name": "TimeZoneOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_zone: str | None = field(
        default=None,
        metadata={
            "name": "TimeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    summer_time_zone_offset: Decimal | None = field(
        default=None,
        metadata={
            "name": "SummerTimeZoneOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    summer_time_zone: str | None = field(
        default=None,
        metadata={
            "name": "SummerTimeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_language: str | None = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    languages: LocaleStructure.Languages | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class Languages:
        language_usage: Iterable[LanguageUsageStructure] = field(
            default_factory=list,
            metadata={
                "name": "LanguageUsage",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
