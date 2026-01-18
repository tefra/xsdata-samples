from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_person_type import (
    ContactPersonType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_point_type import (
    ContactPointType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass(kw_only=True)
class ContactInvolvement:
    """
    :ivar contact_person: A contact person for the organisation.
    :ivar contact_point:
    :ivar cover_name:
    """

    contact_person: None | ContactPersonType = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    contact_point: None | ContactPointType = field(
        default=None,
        metadata={
            "name": "ContactPoint",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    cover_name: None | str = field(
        default=None,
        metadata={
            "name": "CoverName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
