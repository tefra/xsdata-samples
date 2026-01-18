from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeTextElement:
    """
    Parameters
    ----------
    value
    type_value
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
        name = "typeTextElement"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    language_code: None | str = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
        },
    )
