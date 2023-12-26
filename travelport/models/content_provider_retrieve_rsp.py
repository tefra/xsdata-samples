from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.content_provider import ContentProvider

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ContentProviderRetrieveRsp(BaseRsp1):
    """
    Response with all available providers with their suppliers.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    content_provider: list[ContentProvider] = field(
        default_factory=list,
        metadata={
            "name": "ContentProvider",
            "type": "Element",
            "max_occurs": 999,
        },
    )
