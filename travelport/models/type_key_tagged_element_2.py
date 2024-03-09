from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.tag_ref_2 import TagRef2
from travelport.models.type_key_element_2 import TypeKeyElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeKeyTaggedElement2(TypeKeyElement2):
    """
    An Element with a Key and a list of Tags.
    """

    class Meta:
        name = "typeKeyTaggedElement"

    tag_ref: list[TagRef2] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        },
    )
