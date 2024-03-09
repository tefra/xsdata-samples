from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_template_summary import ProfileTemplateSummary
from travelport.models.type_error_info_5 import TypeErrorInfo5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class FieldModifyErrorInfo(TypeErrorInfo5):
    """
    When field or field groups cannot be modified, we see the templates that use
    the fields and field groups.

    Parameters
    ----------
    profile_template_summary
        The summary of templates that are in use that have the fields or
        field groups.
    template_count
        The number of templates using the custom field. The attribute is
        returned if there are more than 100 templates.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_template_summary: list[ProfileTemplateSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileTemplateSummary",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
    template_count: None | int = field(
        default=None,
        metadata={
            "name": "TemplateCount",
            "type": "Attribute",
        },
    )
