from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.type_profile_component_type_2 import (
    TypeProfileComponentType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileHistoryRetrieveCriteria2:
    """
    Specify one or more criteria used to filter the history data.

    Only history data matching all parameters will be returned.

    Parameters
    ----------
    agent_id
        The unique profile ID of the agent that made the change.
    start_date
        The earliest date that the change was made. Leave blank to define an
        open start date.
    end_date
        The latest date that the change was made. Leave blank to define an
        open end date.
    field_id
        To filter by a specific custom field, enter the field ID. To filter
        by a specific instance of a fixed field or field group, send the
        field or field group Key. Must also send the relevant FieldGroupType
        value.
    field_group_id
        To filter by a specific custom field group, enter the field group
        ID. Must also send the relevant FieldGroupType value.
    field_group_type
        To filter by a type of fixed field group or to filter for all custom
        field data or all custom field group data, send the appropriate
        field group type. To further refine the search by fixed field or
        group instance or by custom field or field group ID, also send
        FieldID or FieldGroupID.
    """

    class Meta:
        name = "ProfileHistoryRetrieveCriteria"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agent_id: None | int = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
        },
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        },
    )
    end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        },
    )
    field_id: None | str = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Attribute",
        },
    )
    field_group_id: None | str = field(
        default=None,
        metadata={
            "name": "FieldGroupID",
            "type": "Attribute",
        },
    )
    field_group_type: None | TypeProfileComponentType2 = field(
        default=None,
        metadata={
            "name": "FieldGroupType",
            "type": "Attribute",
        },
    )
