from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_text_element import TypeTextElement

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Text(TypeTextElement):
    """
    Type of Text, Eg-'Upsell','Marketing Agent','Marketing
    Consumer','Strapline','Rule'.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
