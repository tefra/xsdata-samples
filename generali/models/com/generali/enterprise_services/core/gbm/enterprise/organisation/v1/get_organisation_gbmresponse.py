from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbm.enterprise.organisation.v1.get_organisation_gbmresponse_type import (
    GetOrganisationGbmresponseType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v1"


@dataclass(kw_only=True)
class GetOrganisationGbmresponse(GetOrganisationGbmresponseType):
    """
    <description xmlns="">The definition of the response message that
    supports retrieval of an Organisation</description>.
    """

    class Meta:
        name = "GetOrganisationGBMResponse"
        namespace = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v1"
