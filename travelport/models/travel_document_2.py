from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from xsdata.models.datatype import XmlDate
from travelport.models.travel_document_height_unit_2 import (
    TravelDocumentHeightUnit2,
)
from travelport.models.travel_document_weight_unit_2 import (
    TravelDocumentWeightUnit2,
)
from travelport.models.type_geo_political_area_type_2 import (
    TypeGeoPoliticalAreaType2,
)
from travelport.models.type_key_tagged_element_2 import TypeKeyTaggedElement2
from travelport.models.type_travel_document_address_2 import (
    TypeTravelDocumentAddress2,
)
from travelport.models.type_travel_document_type_2 import (
    TypeTravelDocumentType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TravelDocument2(TypeKeyTaggedElement2):
    """
    Information about travel-related documents (e.g., passports, driver's license,
    travel visas, military ID cards).

    Parameters
    ----------
    address
        Address specifed for the Travel Document
    type_value
        The Travel Document type
    document_number
        The Travel Document type
    issued_date
        The date the travel document was issue - YYYY-MM-DD
    expiration_date
        The date the travel document expires - YYYY-MM-DD
    location_issued_description
        The description of the location of issuance
    given_name
        Given name as specified on the travel document.
    middle_name
        Middle name as specified on the travel document.
    surname
        Surname as specified on the travel document.
    gender
        Util: ReferenceDataRetrieveReq, TypeCode PersonGenderType
    national_identifier
        The national or personal number or alphanumeric code that appears on
        the travel document or identification.  This is a different number
        than the document number.
    birth_date
        Date of birth as given on this document - YYYY-MM-DD
    place_of_birth
        Place of birth as given on this document
    nationality
        The nationality of record given on this document
    citizenship
        Country of citizenship. Util: ReferenceDataRetrieveReq, TypeCode
        Country
    issued_by_country
        Country this document was issued in. Util: ReferenceDataRetrieveReq,
        TypeCode Country
    issued_by_other_country_name
        Another name description of the Issued By Country
    height
        A numeric quantity for a traveler's height, as it appears on a
        travel document or identification.
    height_unit
        The unit of measurement for calculating height.
    weight
        A numeric quantity for a traveler's weight, as it appears on a
        travel document or identification.
    weight_unit
        The unit of measurement for calculating weight.
    residence
        The residence that appears on the travel document or identification.
    eye_color
        The eye color(s) that appear on the travel document or
        identification.
    military_status
        The military status that appears on the travel document or
        identification.
    priority_order
        Priority order associated with this TravelDocument.
    issued_for_geo_political_area_type
        The type of the geographical location.
    issued_for_geo_political_area_code
        The location code of the geographical location.
    """

    class Meta:
        name = "TravelDocument"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: None | TypeTravelDocumentAddress2 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    type_value: None | TypeTravelDocumentType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    document_number: None | str = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    issued_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "IssuedDate",
            "type": "Attribute",
        },
    )
    expiration_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
        },
    )
    location_issued_description: None | str = field(
        default=None,
        metadata={
            "name": "LocationIssuedDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    middle_name: None | str = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    gender: None | str = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
    national_identifier: None | str = field(
        default=None,
        metadata={
            "name": "NationalIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    birth_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        },
    )
    place_of_birth: None | str = field(
        default=None,
        metadata={
            "name": "PlaceOfBirth",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    nationality: None | str = field(
        default=None,
        metadata={
            "name": "Nationality",
            "type": "Attribute",
            "length": 2,
        },
    )
    citizenship: None | str = field(
        default=None,
        metadata={
            "name": "Citizenship",
            "type": "Attribute",
            "length": 2,
        },
    )
    issued_by_country: None | str = field(
        default=None,
        metadata={
            "name": "IssuedByCountry",
            "type": "Attribute",
            "length": 2,
        },
    )
    issued_by_other_country_name: None | str = field(
        default=None,
        metadata={
            "name": "IssuedByOtherCountryName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    height: None | Decimal = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Attribute",
            "total_digits": 12,
            "fraction_digits": 2,
        },
    )
    height_unit: None | TravelDocumentHeightUnit2 = field(
        default=None,
        metadata={
            "name": "HeightUnit",
            "type": "Attribute",
        },
    )
    weight: None | Decimal = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "total_digits": 12,
            "fraction_digits": 2,
        },
    )
    weight_unit: None | TravelDocumentWeightUnit2 = field(
        default=None,
        metadata={
            "name": "WeightUnit",
            "type": "Attribute",
        },
    )
    residence: None | str = field(
        default=None,
        metadata={
            "name": "Residence",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    eye_color: None | str = field(
        default=None,
        metadata={
            "name": "EyeColor",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    military_status: None | str = field(
        default=None,
        metadata={
            "name": "MilitaryStatus",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    issued_for_geo_political_area_type: None | TypeGeoPoliticalAreaType2 = (
        field(
            default=None,
            metadata={
                "name": "IssuedForGeoPoliticalAreaType",
                "type": "Attribute",
            },
        )
    )
    issued_for_geo_political_area_code: None | str = field(
        default=None,
        metadata={
            "name": "IssuedForGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        },
    )
