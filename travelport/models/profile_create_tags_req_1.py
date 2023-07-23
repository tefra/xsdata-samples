from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileCreateTagsReq1(BaseReq2):
    """
    Request to create tags for an agency.

    Parameters
    ----------
    create_tag
    agency_id
        The ID of the agency that the tags are created for.
    """
    class Meta:
        name = "ProfileCreateTagsReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    create_tag: list[ProfileCreateTagsReq1.CreateTag] = field(
        default_factory=list,
        metadata={
            "name": "CreateTag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        }
    )
    agency_id: None | int = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class CreateTag:
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
        """
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 128,
            }
        )
        label: None | str = field(
            default=None,
            metadata={
                "name": "Label",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 128,
            }
        )
        description: None | str = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 255,
            }
        )
        display_order: None | int = field(
            default=None,
            metadata={
                "name": "DisplayOrder",
                "type": "Attribute",
            }
        )
