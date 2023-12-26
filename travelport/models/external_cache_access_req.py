from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_3 import BaseReq3

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class ExternalCacheAccessReq(BaseReq3):
    """
    This is to delete/retrieve an entry from external cache.

    Parameters
    ----------
    retrieve_entry
        To retrieve a cache entry
    delete_entry
        To delete a cache entry
    cache_name
        Target Cache Name
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    retrieve_entry: list[ExternalCacheAccessReq.RetrieveEntry] = field(
        default_factory=list,
        metadata={
            "name": "RetrieveEntry",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    delete_entry: list[ExternalCacheAccessReq.DeleteEntry] = field(
        default_factory=list,
        metadata={
            "name": "DeleteEntry",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    cache_name: None | str = field(
        default=None,
        metadata={
            "name": "CacheName",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class RetrieveEntry:
        """
        Parameters
        ----------
        key
            Cache entry key
        """

        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DeleteEntry:
        """
        Parameters
        ----------
        key
            Cache entry key
        """

        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            },
        )
