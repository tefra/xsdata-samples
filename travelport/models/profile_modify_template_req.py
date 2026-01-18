from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.template_modify_cmd import TemplateModifyCmd

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileModifyTemplateReq(BaseReq5):
    """
    Request to modify template.

    Parameters
    ----------
    template_modify_cmd
    id
        Unique identifier of the template, defined by the system.
    version
        Version number of the template. Required with every modify request.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    template_modify_cmd: list[TemplateModifyCmd] = field(
        default_factory=list,
        metadata={
            "name": "TemplateModifyCmd",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    id: int = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    version: int = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
