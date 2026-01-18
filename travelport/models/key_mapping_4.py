from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class KeyMapping4:
    """
    Element for which mapping key sent in the request is different from the
    mapping key comes in the response.

    Parameters
    ----------
    element_name
        Name of the element.
    original_key
        The mapping key which is sent in the request.
    new_key
        The mapping key that comes in the response.
    """

    class Meta:
        name = "KeyMapping"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    element_name: str = field(
        metadata={
            "name": "ElementName",
            "type": "Attribute",
            "required": True,
        }
    )
    original_key: str = field(
        metadata={
            "name": "OriginalKey",
            "type": "Attribute",
            "required": True,
        }
    )
    new_key: str = field(
        metadata={
            "name": "NewKey",
            "type": "Attribute",
            "required": True,
        }
    )
