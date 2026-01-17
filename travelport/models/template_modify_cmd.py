from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.custom_field_add import CustomFieldAdd
from travelport.models.custom_field_delete import CustomFieldDelete
from travelport.models.custom_field_group_add import CustomFieldGroupAdd
from travelport.models.custom_field_group_delete import CustomFieldGroupDelete
from travelport.models.custom_field_group_update import CustomFieldGroupUpdate
from travelport.models.custom_field_update import CustomFieldUpdate
from travelport.models.endpoint_add import EndpointAdd
from travelport.models.endpoint_remove import EndpointRemove
from travelport.models.fixed_field_update import FixedFieldUpdate
from travelport.models.fixed_group_update import FixedGroupUpdate
from travelport.models.template_info_update import TemplateInfoUpdate

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TemplateModifyCmd:
    """
    Wrapper for a set of modification commands to be applied to this
    template.

    Parameters
    ----------
    template_info_update
    fixed_field_update
        Update allowed attributes for fixed field.  The attributes will not
        be updated if not specified.
    fixed_group_update
        Update allowed attributes for  the fixed group data.  The attributes
        will not be updated if not specified.
    custom_field_add
    custom_field_update
    custom_field_group_add
    custom_field_group_update
    endpoint_add
        Add an endpoint to  a particular field or field group
    endpoint_remove
        Removes an endpoint from a particular field or field group
    custom_field_delete
    custom_field_group_delete
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    template_info_update: None | TemplateInfoUpdate = field(
        default=None,
        metadata={
            "name": "TemplateInfoUpdate",
            "type": "Element",
        },
    )
    fixed_field_update: None | FixedFieldUpdate = field(
        default=None,
        metadata={
            "name": "FixedFieldUpdate",
            "type": "Element",
        },
    )
    fixed_group_update: None | FixedGroupUpdate = field(
        default=None,
        metadata={
            "name": "FixedGroupUpdate",
            "type": "Element",
        },
    )
    custom_field_add: None | CustomFieldAdd = field(
        default=None,
        metadata={
            "name": "CustomFieldAdd",
            "type": "Element",
        },
    )
    custom_field_update: None | CustomFieldUpdate = field(
        default=None,
        metadata={
            "name": "CustomFieldUpdate",
            "type": "Element",
        },
    )
    custom_field_group_add: None | CustomFieldGroupAdd = field(
        default=None,
        metadata={
            "name": "CustomFieldGroupAdd",
            "type": "Element",
        },
    )
    custom_field_group_update: None | CustomFieldGroupUpdate = field(
        default=None,
        metadata={
            "name": "CustomFieldGroupUpdate",
            "type": "Element",
        },
    )
    endpoint_add: None | EndpointAdd = field(
        default=None,
        metadata={
            "name": "EndpointAdd",
            "type": "Element",
        },
    )
    endpoint_remove: None | EndpointRemove = field(
        default=None,
        metadata={
            "name": "EndpointRemove",
            "type": "Element",
        },
    )
    custom_field_delete: None | CustomFieldDelete = field(
        default=None,
        metadata={
            "name": "CustomFieldDelete",
            "type": "Element",
        },
    )
    custom_field_group_delete: None | CustomFieldGroupDelete = field(
        default=None,
        metadata={
            "name": "CustomFieldGroupDelete",
            "type": "Element",
        },
    )
