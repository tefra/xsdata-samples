from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.client_data_list import ClientDataList
from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypeTckeyElement(TypeKeyElement1):
    class Meta:
        name = "typeTCKeyElement"

    client_data_list: list[ClientDataList] = field(
        default_factory=list,
        metadata={
            "name": "ClientDataList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            "max_occurs": 99,
        },
    )
