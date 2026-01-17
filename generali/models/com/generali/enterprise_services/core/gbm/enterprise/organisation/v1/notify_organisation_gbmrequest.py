from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbm.enterprise.organisation.v1.notify_organisation_gbmrequest_type import (
    NotifyOrganisationGbmrequestType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v1"


@dataclass
class NotifyOrganisationGbmrequest(NotifyOrganisationGbmrequestType):
    """
    <description xmlns="">The definition of the response message that
    supports notifying on an Organisation</description>.
    """

    class Meta:
        name = "NotifyOrganisationGBMRequest"
        namespace = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v1"
