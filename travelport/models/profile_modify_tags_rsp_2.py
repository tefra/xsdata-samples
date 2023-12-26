from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_5 import BaseRsp5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyTagsRsp2(BaseRsp5):
    """
    Response with the modified tags.
    """

    class Meta:
        name = "ProfileModifyTagsRsp"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    tag: list[ProfileModifyTagsRsp2.Tag] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        },
    )

    @dataclass
    class Tag:
        """
        Parameters
        ----------
        name
            The name given to the tag
        label
            The alternate name given to the tag
        description
            The description of the tag
        display_order
            The display order of the tag
        id
            The unique identifier of the tag.
        agency_id
            The agency that owns the tag
        """

        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 128,
            },
        )
        label: None | str = field(
            default=None,
            metadata={
                "name": "Label",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 128,
            },
        )
        description: None | str = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 255,
            },
        )
        display_order: None | int = field(
            default=None,
            metadata={
                "name": "DisplayOrder",
                "type": "Attribute",
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "name": "ID",
                "type": "Attribute",
                "required": True,
            },
        )
        agency_id: None | int = field(
            default=None,
            metadata={
                "name": "AgencyID",
                "type": "Attribute",
                "required": True,
            },
        )
