from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.address_type import AddressType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.country_gbotype import CountryGbotype
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geo_coded_address_type import GeoCodedAddressType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class GeographyType:
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    name: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
    country: Optional[CountryGbotype] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    address: Optional["GeographyType.Address"] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )

    @dataclass
    class Address:
        address: Optional[AddressType] = field(
            default=None,
            metadata={
                "name": "Address",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )
        geocoded_address: Optional[GeoCodedAddressType] = field(
            default=None,
            metadata={
                "name": "GeocodedAddress",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )
