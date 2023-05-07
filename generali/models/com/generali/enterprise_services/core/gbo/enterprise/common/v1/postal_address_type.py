from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import Idtype
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class PostalAddressType:
    """
    <description xmlns=""> <description>A definition of a postal
    address.</description> </description>

    :ivar occupant_name_text: <description xmlns="">The occupant at this
        address</description>
    :ivar address_line1_text: <description xmlns="">The first line of
        the postal address</description>
    :ivar address_line2_text: <description xmlns="">The first line of
        the postal address</description>
    :ivar address_line3_text: <description xmlns="">The first line of
        the postal address</description>
    :ivar portal_door_text: <description xmlns="">The portal door number
        of the apartment or flat</description>
    :ivar portal_text: <description xmlns="">The portal name of the
        apartment or flat</description>
    :ivar floor_number_text: <description xmlns="">The floor number
        within a building</description>
    :ivar floor_type: <description xmlns="">A description of the level
        within a building where numbers are not used</description>
    :ivar building_number_text: <description xmlns="">The building
        number expressed as text, for this address. e.g. 38,
        55a</description>
    :ivar building_name_text: <description xmlns="">The building name,
        expressed as text, of this address</description>
    :ivar street_name_text: <description xmlns="">The street, expressed
        as text, of this address</description>
    :ivar street_suffix_text: <description xmlns="">A modifier to a
        street name often to denote a relative direction</description>
    :ivar street_type: <description xmlns="">The kind of thoroughfare.
        Example alley, avenue, boulevard, crescent etc</description>
    :ivar post_code_id: <description xmlns=""> <description>The PostCode
        or ZipCode of the postal address.</description> </description>
    :ivar county_text: <description xmlns="">Name of the county in which
        the city falls, where applicable</description>
    :ivar country_code_id: <description xmlns=""> <description>The
        ISO3166 country code for the address.</description>
        </description>
    :ivar country_name_text: <description xmlns=""> <description>The
        full name of the country.</description> </description>
    """
    occupant_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "OccupantNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    address_line1_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AddressLine1Text",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    address_line2_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AddressLine2Text",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    address_line3_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AddressLine3Text",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    portal_door_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "PortalDoorText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    portal_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "PortalText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    floor_number_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FloorNumberText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    floor_type: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "FloorType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    building_number_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "BuildingNumberText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    building_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "BuildingNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    street_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "StreetNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    street_suffix_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "StreetSuffixText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    street_type: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "StreetType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    post_code_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PostCodeID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    county_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CountyText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    country_code_id: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CountryCodeID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    country_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "CountryNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
