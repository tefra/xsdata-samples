from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveTemplateReq(BaseReq5):
    """Request to retrieve a profile template.

    If version exists, the response will not return the template unless
    there is a mismatch.

    Parameters
    ----------
    consuming_system
        Filter out actions and endpoints based on the consuming system(s)
    id
        Unique identifier of the template, defined by the system.
    version
        Version number of the template.
    return_override_fields_only
        Default=false.By default response will return aggregated structure
        of override plus default template.If passed true, only override
        fields will be returned.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    consuming_system: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ConsumingSystem",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 128,
        },
    )
    id: None | int = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    return_override_fields_only: bool = field(
        default=False,
        metadata={
            "name": "ReturnOverrideFieldsOnly",
            "type": "Attribute",
        },
    )
