from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_sub_key_1 import TypeSubKey1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class TypeKeyword1:
    """
    A complexType for keyword information.

    Parameters
    ----------
    sub_key
        A further breakdown of a keyword.
    text
        Information for a keyword.
    name
        The keyword name.
    number
        The number for this keyword.
    description
        A brief description of the keyword
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
        name = "typeKeyword"

    sub_key: list[TypeSubKey1] = field(
        default_factory=list,
        metadata={
            "name": "SubKey",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "max_length": 12,
        },
    )
    number: None | object = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
    description: None | object = field(
        default=None,
        metadata={
            "name": "Description",
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
