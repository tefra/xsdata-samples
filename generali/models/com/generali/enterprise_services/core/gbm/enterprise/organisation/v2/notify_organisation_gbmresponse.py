from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbm.enterprise.organisation.v2.notify_organisation_gbmresponse_type import (
    NotifyOrganisationGbmresponseType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v2"


@dataclass(kw_only=True)
class NotifyOrganisationGbmresponse(NotifyOrganisationGbmresponseType):
    """
    <description xmlns="">The definition of the response message that
    supports acknowledgement for an Organisation
    notification</description>.
    """

    class Meta:
        name = "NotifyOrganisationGBMResponse"
        namespace = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v2"
