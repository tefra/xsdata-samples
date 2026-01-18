from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.language_option import LanguageOption

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TermConditions:
    """
    The terms and conditions to be included in Fax details.

    Parameters
    ----------
    language_option
    include_term_conditions
        Specifies whether Term and Conditions included in the Fax or not .
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    language_option: list[LanguageOption] = field(
        default_factory=list,
        metadata={
            "name": "LanguageOption",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    include_term_conditions: bool = field(
        metadata={
            "name": "IncludeTermConditions",
            "type": "Attribute",
            "required": True,
        }
    )
