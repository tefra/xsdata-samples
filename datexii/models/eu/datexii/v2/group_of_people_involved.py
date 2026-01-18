from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.injury_status_type_enum import (
    InjuryStatusTypeEnum,
)
from datexii.models.eu.datexii.v2.involvement_roles_enum import (
    InvolvementRolesEnum,
)
from datexii.models.eu.datexii.v2.person_category_enum import (
    PersonCategoryEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class GroupOfPeopleInvolved:
    """
    Group of people involved in the event having common characteristics
    and/or status.

    :ivar number_of_people: The number of people of this group that are
        involved.
    :ivar injury_status: The injury status of the people involved.
    :ivar involvement_role: The involvement role of the people.
    :ivar category_of_people_involved: The category of persons involved.
    :ivar group_of_people_involved_extension:
    """

    number_of_people: None | int = field(
        default=None,
        metadata={
            "name": "numberOfPeople",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    injury_status: None | InjuryStatusTypeEnum = field(
        default=None,
        metadata={
            "name": "injuryStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    involvement_role: None | InvolvementRolesEnum = field(
        default=None,
        metadata={
            "name": "involvementRole",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    category_of_people_involved: None | PersonCategoryEnum = field(
        default=None,
        metadata={
            "name": "categoryOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_people_involved_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "groupOfPeopleInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
