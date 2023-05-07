from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class TelephoneNumberCountryCodeType(TextType):
    """
    <description xmlns=""> <description>The definition Country Code part of a
    Telephone Number.</description> </description>
    """
