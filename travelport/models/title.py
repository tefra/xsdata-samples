from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_text_element import TypeTextElement

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Title(TypeTextElement):
    """
    The additional titles associated to the brand or optional service.

    Providers: ACH, RCH, 1G, 1V, 1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
