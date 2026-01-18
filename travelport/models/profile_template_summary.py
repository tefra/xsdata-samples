from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileTemplateSummary:
    """
    Brief summary containing a template's name and ID.

    Parameters
    ----------
    id
        The ID of the template
    name
        The name of the template
    version
        Current version number of the template
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: int = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: object = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    version: object = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
