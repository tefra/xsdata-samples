from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmheader_type import BaseGbmheaderType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.organisation_gbotype import OrganisationGbotype

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v2"


@dataclass
class NotifyOrganisationGbmrequestType(BaseGbmheaderType):
    """
    <description xmlns="">The definition of the request message that supports
    notifying on an Organisation</description>

    :ivar organisation_gbo: <description xmlns="">The business object to
        notify on</description>
    """
    class Meta:
        name = "NotifyOrganisationGBMRequestType"

    organisation_gbo: Optional[OrganisationGbotype] = field(
        default=None,
        metadata={
            "name": "OrganisationGBO",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v2",
            "required": True,
        }
    )
