from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class TicketAdvisory:
    """
    Additional ticket information.

    Parameters
    ----------
    value
    key
    language_code
        ISO 639 two-character language codes are used to retrieve specific
        information in the requested language. For Rich Content and
        Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS
        (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese
        Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE,
        DECH can also be used. Only certain services support this attribute.
        Providers: ACH, RCH, 1G, 1V, 1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    language_code: None | str = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
        },
    )
