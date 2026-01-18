from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.email_address_domain_part_type import (
    EmailAddressDomainPartType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.email_address_full_type import (
    EmailAddressFullType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.email_address_local_part_type import (
    EmailAddressLocalPartType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class EmailAddressType:
    """
    <description xmlns="">A Email Address conforming to RFC5321 and
    RFC5322.</description>.

    :ivar full_address_text: <description xmlns="">The full email
        address e.g. peter.jackson@vodafone.com</description>
    :ivar domain_part_text: <description xmlns="">The domain e.g.
        vodafone.com, without the @ symbol.</description>
    :ivar local_part_text: <description xmlns="">The username e.g.
        peter.jackson</description>
    """

    full_address_text: None | EmailAddressFullType = field(
        default=None,
        metadata={
            "name": "FullAddressText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
    domain_part_text: None | EmailAddressDomainPartType = field(
        default=None,
        metadata={
            "name": "DomainPartText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    local_part_text: None | EmailAddressLocalPartType = field(
        default=None,
        metadata={
            "name": "LocalPartText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
