from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v1"


@dataclass
class NotifyOrganisationGbmresponseType:
    """
    <description xmlns="">The definition of the response message that
    supports acknowledgement for an Organisation
    notification</description>.
    """

    class Meta:
        name = "NotifyOrganisationGBMResponseType"

    acknowledgement: None | str = field(
        default=None,
        metadata={
            "name": "Acknowledgement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v1",
            "required": True,
            "pattern": r"uuid:[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
