from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmheader_type import (
    BaseGbmheaderType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.organisation_gbotype import (
    OrganisationGbotype,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v1"


@dataclass
class GetOrganisationGbmresponseType(BaseGbmheaderType):
    """
    <description xmlns="">The definition of the response message that supports
    retrieval of an Organisation</description>

    :ivar organisation_gbo: <description xmlns="">The business object to
        retrieve</description>
    """

    class Meta:
        name = "GetOrganisationGBMResponseType"

    organisation_gbo: Optional[OrganisationGbotype] = field(
        default=None,
        metadata={
            "name": "OrganisationGBO",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbm/enterprise/organisation/v1",
            "required": True,
        },
    )
