from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TemplateInfoUpdate:
    """
    Alllow the editing of certain data of the template.

    Parameters
    ----------
    name
        Name of the template.
    description
        Description of the template.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: object = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    description: None | object = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
