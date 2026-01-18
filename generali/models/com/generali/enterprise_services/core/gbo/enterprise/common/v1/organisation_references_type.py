from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_reference_type import (
    OrganisationReferenceType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class OrganisationReferencesType:
    """
    :ivar organisation_reference: The ID of the organisation in external
        system, could be the Company VAT Number, the SiretNumber, could
        be D&amp;B number
    """

    organisation_reference: list[OrganisationReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationReference",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "min_occurs": 1,
        },
    )
