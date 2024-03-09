from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.telephone_number_country_code_type import (
    TelephoneNumberCountryCodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.telephone_number_identification_code_type import (
    TelephoneNumberIdentificationCodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.telephone_number_subscriber_number_type import (
    TelephoneNumberSubscriberNumberType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class TelephoneNumberType:
    """
    <description xmlns="">A definition of a land line telephone number or
    MSISDN.</description>

    :ivar full_number_text: <description xmlns=""> <description>The full
        telephone number, e.g. +44 0790 028 2454</description>
        </description>
    :ivar country_code_text: <description xmlns=""> <description>The
        Country Code of the Telephone Number, 1-3 digits.</description>
        </description>
    :ivar identification_code_text: <description xmlns="">
        <description>The Identification Code or Destination Code of the
        Telephone Number, 1-3 digits.</description> </description>
    :ivar subscriber_number_text: <description xmlns="">
        <description>The Subscriber Number of the Telephone Number, 1-3
        digits.</description> </description>
    """

    full_number_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FullNumberText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
    country_code_text: Optional[TelephoneNumberCountryCodeType] = field(
        default=None,
        metadata={
            "name": "CountryCodeText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    identification_code_text: Optional[
        TelephoneNumberIdentificationCodeType
    ] = field(
        default=None,
        metadata={
            "name": "IdentificationCodeText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    subscriber_number_text: Optional[TelephoneNumberSubscriberNumberType] = (
        field(
            default=None,
            metadata={
                "name": "SubscriberNumberText",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            },
        )
    )
