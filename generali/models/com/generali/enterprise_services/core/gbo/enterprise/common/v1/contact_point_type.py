from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_simple_component_type import (
    BaseSimpleComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.email_address_full_type import (
    EmailAddressFullType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geography_type import (
    GeographyType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.telephone_number_type import (
    TelephoneNumberType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class ContactPointType(BaseSimpleComponentType):
    """<description xmlns="">A type defining a contact point.

    This is the address at which someone or something may be
    contacted.</description>

    :ivar email: <description xmlns="">The contact point is an Email
        Address.</description>
    :ivar telephone: <description xmlns="">Telephone as contact
        point</description>
    :ivar postal: <description xmlns="">Postal as contact
        point</description>
    :ivar sms: <description xmlns="">SMS as contact point</description>
    :ivar fax: <description xmlns="">SMS as contact point</description>
    """

    email: Optional[EmailAddressFullType] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    telephone: Optional[TelephoneNumberType] = field(
        default=None,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    postal: Optional[GeographyType] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    sms: Optional[TelephoneNumberType] = field(
        default=None,
        metadata={
            "name": "SMS",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    fax: Optional[TelephoneNumberType] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
