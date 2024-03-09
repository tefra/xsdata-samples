from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.country_gbotype import (
    CountryGbotype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geography_type_address import (
    GeographyTypeAddress,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class GeographyType:
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    name: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
    country: Optional[CountryGbotype] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    address: Optional[GeographyTypeAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
