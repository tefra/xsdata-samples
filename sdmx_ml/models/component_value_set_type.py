from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.member_selection_type import MemberSelectionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class ComponentValueSetType(MemberSelectionType):
    """
    ComponentValueSetType defines the structure for providing values for a
    data attributes, measures, or metadata attributes.

    If no values are provided, the component is implied to include/excluded
    from the region in which it is defined, with no regard to the value of
    the component. Note that for metadata attributes which occur within
    other metadata attributes, a nested identifier can be provided. For
    example, a value of CONTACT.ADDRESS.STREET refers to the metadata
    attribute with the identifier STREET which exists in the ADDRESS
    metadata attribute in the CONTACT metadata attribute, which is defined
    at the root of the report structure.
    """

    valid_from: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    valid_to: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
