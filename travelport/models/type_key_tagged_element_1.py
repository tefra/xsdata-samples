from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.tag_ref_1 import TagRef1
from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypeKeyTaggedElement1(TypeKeyElement1):
    """
    An Element with a Key and a list of Tags.
    """

    class Meta:
        name = "typeKeyTaggedElement"

    tag_ref: list[TagRef1] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
