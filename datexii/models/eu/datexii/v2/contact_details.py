from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.contact import Contact
from datexii.models.eu.datexii.v2.country_enum import CountryEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.ownership_type_enum import OwnershipTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ContactDetails(Contact):
    """
    Details for some person, service or the parking site itself, especially
    address information.

    :ivar contact_organisation_name: Name of the organisation or
        service. Do not use this attribute in combination with role
        "parkingSiteAddress".
    :ivar contact_person_name: Name of the contact person.
    :ivar contact_person_first_name: First name of the contact person.
    :ivar contact_person_position: The position of the contact person.
    :ivar contact_details_language: Language(s) this contact is able to
        speak resp. understand.
    :ivar contact_details_address: Complete address of the contact.
        Alternatively use the separate fields to describe the address.
    :ivar contact_details_street: Street of the contact.
    :ivar contact_details_house_number: House number of the contact.
        Supports a multiplicity up to two, to specify lower and upper
        numbers.
    :ivar contact_details_postcode: Postcode of the contact.
    :ivar contact_details_city: City of the contact.
    :ivar country: ISO 3166-1 two character country code.
    :ivar contact_details_telephone_number: Telephone Number of contact.
    :ivar contact_details_fax: Fax of the contact.
    :ivar contact_details_email: E-Mail address of the contact.
    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar contact_details_logo_url: Url to define a logo of this
        contact.
    :ivar available24hours: Specifies if the availability is 24 hours a
        day. If omitted, this information is unknown or heterogeneous.
    :ivar contact_details_responsibility: Specification of what service
        or equipment the contact is responsible for.
    :ivar contact_details_more_info: Additional information relating to
        the contact.
    :ivar publishing_agreement: Indication, whether the contact accepted
        publishing its contact information.
    :ivar contact_details_ownership: Information if the contact in
        question is a private or public institution.
    :ivar group_of_locations:
    :ivar contact_details_extension:
    :ivar id:
    :ivar version:
    """

    contact_organisation_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "contactOrganisationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_person_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactPersonName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    contact_person_first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactPersonFirstName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    contact_person_position: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "contactPersonPosition",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "contactDetailsLanguage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_address: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "contactDetailsAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_street: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsStreet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    contact_details_house_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "contactDetailsHouseNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
            "max_length": 1024,
        },
    )
    contact_details_postcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsPostcode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    contact_details_city: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "contactDetailsCity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_telephone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsTelephoneNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    contact_details_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsFax",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    contact_details_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsEMail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_logo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactDetailsLogoUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    available24hours: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_responsibility: list[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "contactDetailsResponsibility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_more_info: list[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "contactDetailsMoreInfo",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    publishing_agreement: Optional[bool] = field(
        default=None,
        metadata={
            "name": "publishingAgreement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_ownership: Optional[OwnershipTypeEnum] = field(
        default=None,
        metadata={
            "name": "contactDetailsOwnership",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    contact_details_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "contactDetailsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
