from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from common_types.models.hl7_v3.ne2008.core.voc import (
    AddressPartType,
    CompressionAlgorithm,
    EntityNamePartQualifier,
    EntityNamePartType,
    EntityNameUse,
    IntegrityCheckAlgorithm,
    NullFlavor,
    PostalAddressUse,
    SetOperator,
    TelecommunicationAddressUse,
    TimingEvent,
)

__NAMESPACE__ = "urn:hl7-org:v3"


class BinaryDataEncoding(Enum):
    B64 = "B64"
    TXT = "TXT"


@dataclass
class AdxpExplicit:
    """A character string that may have a type-tag signifying its role in the
    address.

    Typical parts that exist in about every address are street, house
    number, or post box, postal code, city, country but other roles may
    be defined regionally, nationally, or on an enterprise level (e.g.
    in military addresses). Addresses are usually broken up into lines,
    which are indicated by special line-breaking delimiter elements
    (e.g., DEL).

    :ivar content:
    :ivar part_type: Specifies whether an address part names the street,
        city, country, postal code, post box, etc. If the type is NULL
        the address part is unclassified and would simply appear on an
        address label as is.
    """
    class Meta:
        name = "ADXP_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: Optional[AddressPartType] = field(
        default=None,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class Any:
    """Defines the basic properties of every data value.

    This is an abstract type, meaning that no value can be just a data
    value without belonging to any concrete type. Every concrete type is
    a specialization of this general abstract DataValue type.

    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    """
    class Meta:
        name = "ANY"

    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )


@dataclass
class EnxpExplicit:
    """A character string token representing a part of a name.

    May have a type code signifying the role of the part in the whole
    entity name, and a qualifier code for more detail about the name
    part type. Typical name parts for person names are given names, and
    family names, titles, etc.

    :ivar content:
    :ivar part_type: Indicates whether the name part is a given name,
        family name, prefix, suffix, etc.
    :ivar qualifier: is a set of codes each of which specifies
        a certain subcategory of the name part in addition to
        the main name part type. For example, a given name may
        be flagged as a nickname, a family name may be a
        pseudonym or a name of public records.
    """
    class Meta:
        name = "ENXP_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: Optional[EntityNamePartType] = field(
        default=None,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
    qualifier: List[EntityNamePartQualifier] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class IvxbTsExplicit:
    """
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar value:
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """
    class Meta:
        name = "IVXB_TS_explicit"

    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}|([0-9]{9,14}|[0-9]{14,14}\.[0-9]+)([+\-][0-9]{1,4})?",
        }
    )
    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class SxcmTsExplicit:
    """
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar value:
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """
    class Meta:
        name = "SXCM_TS_explicit"

    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}|([0-9]{9,14}|[0-9]{14,14}\.[0-9]+)([+\-][0-9]{1,4})?",
        }
    )
    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TsExplicit:
    """A quantity specifying a point on the axis of natural time.

    A point in time is most often represented as a calendar expression.

    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar value:
    """
    class Meta:
        name = "TS_explicit"

    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}|([0-9]{9,14}|[0-9]{14,14}\.[0-9]+)([+\-][0-9]{1,4})?",
        }
    )


@dataclass
class EnExplicitDelimiter:
    class Meta:
        name = "en_explicit.delimiter"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.DEL_VALUE,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
    qualifier: List[EntityNamePartQualifier] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class EnExplicitFamily:
    class Meta:
        name = "en_explicit.family"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.FAM,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
    qualifier: List[EntityNamePartQualifier] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class EnExplicitGiven:
    class Meta:
        name = "en_explicit.given"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.GIV,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
    qualifier: List[EntityNamePartQualifier] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class EnExplicitPrefix:
    class Meta:
        name = "en_explicit.prefix"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.PFX,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
    qualifier: List[EntityNamePartQualifier] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class EnExplicitSuffix:
    class Meta:
        name = "en_explicit.suffix"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.SFX,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
    qualifier: List[EntityNamePartQualifier] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class AnynonNull(Any):
    """The BooleanNonNull type is used where a Boolean cannot have a null
    value.

    A Boolean value can be either true or false.
    """
    class Meta:
        name = "ANYNonNull"


@dataclass
class Bin(Any):
    """Binary data is a raw block of bits.

    Binary data is a protected type that MUST not be used outside the
    data type specification.

    :ivar content:
    :ivar representation: Specifies the representation of the binary
        data that is the content of the binary data value.
    """
    class Meta:
        name = "BIN"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    representation: BinaryDataEncoding = field(
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Bl(Any):
    """The Boolean type stands for the values of two-valued logic.

    A Boolean value can be either true or false, or, as any other value
    may be NULL.
    """
    class Meta:
        name = "BL"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class Cr(Any):
    """A concept qualifier code with optionally named role.

    Both qualifier role and value codes must be defined by the coding
    system.  For example, if SNOMED RT defines a concept "leg", a role
    relation "has-laterality", and another concept "left", the concept
    role relation allows to add the qualifier "has-laterality: left" to
    a primary code "leg" to construct the meaning "left leg".

    :ivar name: Specifies the manner in which the concept role value
        contributes to the meaning of a code phrase.  For example, if
        SNOMED RT defines a concept "leg", a role relation "has-
        laterality", and another concept "left", the concept role
        relation allows to add the qualifier "has-laterality: left" to a
        primary code "leg" to construct the meaning "left leg".  In this
        example "has-laterality" is .
    :ivar value: The concept that modifies the primary code of a code
        phrase through the role relation.  For example, if SNOMED RT
        defines a concept "leg", a role relation "has-laterality", and
        another concept "left", the concept role relation allows adding
        the qualifier "has-laterality: left" to a primary code "leg" to
        construct the meaning "left leg".  In this example "left" is .
    :ivar inverted: Indicates if the sense of the role name is inverted.
        This can be used in cases where the underlying code system
        defines inversion but does not provide reciprocal pairs of role
        names. By default, inverted is false.
    """
    class Meta:
        name = "CR"

    name: Optional["Cv"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional["Cd"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    inverted: str = field(
        default="false",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class Ii(Any):
    """An identifier that uniquely identifies a thing or object.

    Examples are object identifier for HL7 RIM objects, medical record
    number, order id, service catalog item id, Vehicle Identification
    Number (VIN), etc. Instance identifiers are defined based on ISO
    object identifiers.

    :ivar root: A unique identifier that guarantees the global
        uniqueness of the instance identifier. The root alone may be the
        entire instance identifier.
    :ivar extension: A character string as a unique identifier within
        the scope of the identifier root.
    :ivar assigning_authority_name: A human readable name or mnemonic
        for the assigning authority. This name may be provided solely
        for the convenience of unaided humans interpreting an  value and
        can have no computational meaning. Note: no automated processing
        must depend on the assigning authority name to be present in any
        form.
    :ivar displayable: Specifies if the identifier is intended for human
        display and data entry (displayable = true) as opposed to pure
        machine interoperation (displayable = false).
    """
    class Meta:
        name = "II"

    root: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        }
    )
    assigning_authority_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigningAuthorityName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    displayable: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class Qty(Any):
    """is an abstract generalization for all data types (1) whose value set has
    an order relation (less-or-equal) and (2) where difference is defined in
    all of the data type's totally ordered value subsets.

    The quantity type abstraction is needed in defining certain other
    types, such as the interval and the probability distribution.
    """
    class Meta:
        name = "QTY"


@dataclass
class TelExplicit:
    """A telephone number (voice or fax), e-mail address, or other locator for
    a resource (information or service) mediated by telecommunication
    equipment.

    The address is specified as a URL qualified by time specification
    and use codes that help in deciding which address to use for a given
    time and purpose.

    :ivar useable_period: Specifies the periods of time during which the
        telecommunication address can be used.  For a telephone number,
        this can indicate the time of day in which the party can be
        reached on that telephone. For a web address, it may specify a
        time range in which the web content is promised to be available
        under the given address.
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar value:
    :ivar use: One or more codes advising a system or user which
        telecommunication address in a set of like addresses to select
        for a given telecommunication need.
    """
    class Meta:
        name = "TEL_explicit"

    useable_period: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "useablePeriod",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    use: List[TelecommunicationAddressUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Url(Any):
    """A telecommunications address  specified according to Internet standard
    RFC 1738.

    [http://www.ietf.org/rfc/rfc1738.txt]. The URL specifies the
    protocol and the contact point defined by that protocol for the
    resource.  Notable uses of the telecommunication address data type
    are for telephone and telefax numbers, e-mail addresses, Hypertext
    references, FTP references, etc.
    """
    class Meta:
        name = "URL"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitAdditionalLocator(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.additionalLocator"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.ADL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitBuildingNumberSuffix(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.buildingNumberSuffix"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.BNS,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitCareOf(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.careOf"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CAR,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitCensusTract(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.censusTract"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CEN,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitCity(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.city"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CTY,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitCountry(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.country"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CNT,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitCounty(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.county"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CPA,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitDelimiter(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.delimiter"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DEL_VALUE,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitDeliveryAddressLine(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.deliveryAddressLine"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DAL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitDeliveryInstallationArea(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.deliveryInstallationArea"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DINSTA,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitDeliveryInstallationQualifier(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.deliveryInstallationQualifier"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DINSTQ,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitDeliveryInstallationType(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.deliveryInstallationType"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DINST,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitDeliveryMode(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.deliveryMode"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DMOD,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitDeliveryModeIdentifier(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.deliveryModeIdentifier"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DMODID,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitDirection(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.direction"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DIR,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitHouseNumber(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.houseNumber"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.BNR,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitHouseNumberNumeric(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.houseNumberNumeric"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.BNN,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitPostBox(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.postBox"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.POB,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitPostalCode(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.postalCode"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.ZIP,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitPrecinct(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.precinct"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.PRE,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitState(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.state"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STA,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitStreetAddressLine(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.streetAddressLine"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.SAL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitStreetName(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.streetName"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STR_VALUE,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitStreetNameBase(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.streetNameBase"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STB,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitStreetNameType1(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.streetNameType1"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STTYP,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitUnitId(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.unitID"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.UNID,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpExplicitUnitType(AdxpExplicit):
    class Meta:
        name = "adxp_explicit.unitType"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.UNIT,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdExplicit:
    """Mailing and home or office addresses.

    A sequence of address parts, such as street or post office Box,
    city, postal code, country, etc.

    :ivar content:
    :ivar delimiter:
    :ivar country:
    :ivar state:
    :ivar county:
    :ivar city:
    :ivar postal_code:
    :ivar street_address_line:
    :ivar house_number:
    :ivar house_number_numeric:
    :ivar direction:
    :ivar street_name:
    :ivar street_name_base:
    :ivar street_name_type:
    :ivar additional_locator:
    :ivar unit_id:
    :ivar unit_type:
    :ivar care_of:
    :ivar census_tract:
    :ivar delivery_address_line:
    :ivar delivery_installation_type:
    :ivar delivery_installation_area:
    :ivar delivery_installation_qualifier:
    :ivar delivery_mode:
    :ivar delivery_mode_identifier:
    :ivar building_number_suffix:
    :ivar post_box:
    :ivar precinct:
    :ivar useable_period: A GTS specifying the periods of time during
        which the address can be used. This is used to specify different
        addresses for different times of the year or to refer to
        historical addresses.
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar use: A set of codes advising a system or user which address in
        a set of like addresses to select for a given purpose.
    :ivar is_not_ordered: A boolean value specifying whether the order
        of the address parts is known or not. While the address parts
        are always a Sequence, the order in which they are presented may
        or may not be known. Where this matters,  can be used to convey
        this information.
    """
    class Meta:
        name = "AD_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    delimiter: List[AdxpExplicitDelimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    country: List[AdxpExplicitCountry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    state: List[AdxpExplicitState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    county: List[AdxpExplicitCounty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    city: List[AdxpExplicitCity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    postal_code: List[AdxpExplicitPostalCode] = field(
        default_factory=list,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    street_address_line: List[AdxpExplicitStreetAddressLine] = field(
        default_factory=list,
        metadata={
            "name": "streetAddressLine",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    house_number: List[AdxpExplicitHouseNumber] = field(
        default_factory=list,
        metadata={
            "name": "houseNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    house_number_numeric: List[AdxpExplicitHouseNumberNumeric] = field(
        default_factory=list,
        metadata={
            "name": "houseNumberNumeric",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    direction: List[AdxpExplicitDirection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    street_name: List[AdxpExplicitStreetName] = field(
        default_factory=list,
        metadata={
            "name": "streetName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    street_name_base: List[AdxpExplicitStreetNameBase] = field(
        default_factory=list,
        metadata={
            "name": "streetNameBase",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    street_name_type: List[AdxpExplicitStreetNameType1] = field(
        default_factory=list,
        metadata={
            "name": "streetNameType",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    additional_locator: List[AdxpExplicitAdditionalLocator] = field(
        default_factory=list,
        metadata={
            "name": "additionalLocator",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    unit_id: List[AdxpExplicitUnitId] = field(
        default_factory=list,
        metadata={
            "name": "unitID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    unit_type: List[AdxpExplicitUnitType] = field(
        default_factory=list,
        metadata={
            "name": "unitType",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    care_of: List[AdxpExplicitCareOf] = field(
        default_factory=list,
        metadata={
            "name": "careOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    census_tract: List[AdxpExplicitCensusTract] = field(
        default_factory=list,
        metadata={
            "name": "censusTract",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_address_line: List[AdxpExplicitDeliveryAddressLine] = field(
        default_factory=list,
        metadata={
            "name": "deliveryAddressLine",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_installation_type: List[AdxpExplicitDeliveryInstallationType] = field(
        default_factory=list,
        metadata={
            "name": "deliveryInstallationType",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_installation_area: List[AdxpExplicitDeliveryInstallationArea] = field(
        default_factory=list,
        metadata={
            "name": "deliveryInstallationArea",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_installation_qualifier: List[AdxpExplicitDeliveryInstallationQualifier] = field(
        default_factory=list,
        metadata={
            "name": "deliveryInstallationQualifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_mode: List[AdxpExplicitDeliveryMode] = field(
        default_factory=list,
        metadata={
            "name": "deliveryMode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_mode_identifier: List[AdxpExplicitDeliveryModeIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "deliveryModeIdentifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    building_number_suffix: List[AdxpExplicitBuildingNumberSuffix] = field(
        default_factory=list,
        metadata={
            "name": "buildingNumberSuffix",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    post_box: List[AdxpExplicitPostBox] = field(
        default_factory=list,
        metadata={
            "name": "postBox",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    precinct: List[AdxpExplicitPrecinct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    useable_period: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "useablePeriod",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    use: List[PostalAddressUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    is_not_ordered: Optional[str] = field(
        default=None,
        metadata={
            "name": "isNotOrdered",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class Bn(AnynonNull):
    """The BooleanNonNull type is used where a Boolean cannot have a null
    value.

    A Boolean value can be either true or false.
    """
    class Meta:
        name = "BN"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class IntType(Qty):
    """Integer numbers (-1,0,1,2, 100, 3398129, etc.) are precise numbers that
    are results of counting and enumerating.

    Integer numbers are discrete, the set of integers is infinite but
    countable.  No arbitrary limit is imposed on the range of integer
    numbers. Two NULL flavors are defined for the positive and negative
    infinity.
    """
    class Meta:
        name = "INT"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Mo(Qty):
    """A monetary amount is a quantity expressing the amount of money in some
    currency.

    Currencies are the units in which monetary amounts are denominated
    in different economic regions. While the monetary amount is a single
    kind of quantity (money) the exchange rates between the different
    units are variable.  This is the principle difference between
    physical quantity and monetary amounts, and the reason why currency
    units are not physical units.

    :ivar value: The magnitude of the monetary amount in terms of the
        currency unit.
    :ivar currency: The currency unit as defined in ISO 4217.
    """
    class Meta:
        name = "MO"

    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class Real(Qty):
    """Fractional numbers.

    Typically used whenever quantities are measured, estimated, or
    computed from other real numbers.  The typical representation is
    decimal, where the number of significant decimal digits is known as
    the precision. Real numbers are needed beyond integers whenever
    quantities of the real world are measured, estimated, or computed
    from other real numbers. The term "Real number" in this
    specification is used to mean that fractional values are covered
    without necessarily implying the full set of the mathematical real
    numbers.
    """
    class Meta:
        name = "REAL"

    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RtoQtyQty(Qty):
    """
    :ivar numerator: The quantity that is being divided in the ratio.
        The default is the integer number 1 (one).
    :ivar denominator: The quantity that devides the numerator in the
        ratio. The default is the integer number 1 (one). The
        denominator must not be zero.
    """
    class Meta:
        name = "RTO_QTY_QTY"

    numerator: Optional[Qty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    denominator: Optional[Qty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )


@dataclass
class Ts(Qty):
    """A quantity specifying a point on the axis of natural time.

    A point in time is most often represented as a calendar expression.
    """
    class Meta:
        name = "TS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}|([0-9]{9,14}|[0-9]{14,14}\.[0-9]+)([+\-][0-9]{1,4})?",
        }
    )


@dataclass
class ThumbnailExplicit:
    """A thumbnail is an abbreviated rendition of the full data.

    A thumbnail requires significantly fewer resources than the full
    data, while still maintaining some distinctive similarity with the
    full data. A thumbnail is typically used with by-reference
    encapsulated data. It allows a user to select data more efficiently
    before actually downloading through the reference.

    :ivar content:
    :ivar reference:
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar representation: Specifies the representation of the binary
        data that is the content of the binary data value.
    :ivar media_type: Identifies the type of the encapsulated data and
        identifies a method to interpret or render the data.
    :ivar language: For character based information the language
        property specifies the human language of the text.
    :ivar compression: Indicates whether the raw byte data is
        compressed, and what compression algorithm was used.
    :ivar integrity_check: The integrity check is a short binary value
        representing a cryptographically strong checksum that is
        calculated over the binary data. The purpose of this property,
        when communicated with a reference is for anyone to validate
        later whether the reference still resolved to the same data that
        the reference resolved to when the encapsulated data value with
        reference was created.
    :ivar integrity_check_algorithm: Specifies the algorithm used to
        compute the integrityCheck value.
    """
    class Meta:
        name = "thumbnail_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    reference: Optional[TelExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    representation: BinaryDataEncoding = field(
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        }
    )
    media_type: str = field(
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    compression: Optional[CompressionAlgorithm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    integrity_check: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "integrityCheck",
            "type": "Attribute",
            "format": "base64",
        }
    )
    integrity_check_algorithm: IntegrityCheckAlgorithm = field(
        default=IntegrityCheckAlgorithm.SHA_1,
        metadata={
            "name": "integrityCheckAlgorithm",
            "type": "Attribute",
        }
    )


@dataclass
class EdExplicit:
    """Data that is primarily intended for human interpretation or for further
    machine processing is outside the scope of HL7.

    This includes unformatted or formatted written language, multimedia
    data, or structured information as defined by a different standard
    (e.g., XML-signatures.)  Instead of the data itself, an ED may
    contain only a reference (see TEL.) Note that the ST data type is a
    specialization of when the  is text/plain.

    :ivar content:
    :ivar reference: A telecommunication address (TEL), such as a URL
        for HTTP or FTP, which will resolve to precisely the same binary
        data that could as well have been provided as inline data.
    :ivar thumbnail:
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar representation: Specifies the representation of the binary
        data that is the content of the binary data value.
    :ivar media_type: Identifies the type of the encapsulated data and
        identifies a method to interpret or render the data.
    :ivar language: For character based information the language
        property specifies the human language of the text.
    :ivar compression: Indicates whether the raw byte data is
        compressed, and what compression algorithm was used.
    :ivar integrity_check: The integrity check is a short binary value
        representing a cryptographically strong checksum that is
        calculated over the binary data. The purpose of this property,
        when communicated with a reference is for anyone to validate
        later whether the reference still resolved to the same data that
        the reference resolved to when the encapsulated data value with
        reference was created.
    :ivar integrity_check_algorithm: Specifies the algorithm used to
        compute the integrityCheck value.
    """
    class Meta:
        name = "ED_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    reference: Optional[TelExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    thumbnail: Optional[ThumbnailExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    representation: BinaryDataEncoding = field(
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        }
    )
    media_type: str = field(
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    compression: Optional[CompressionAlgorithm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    integrity_check: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "integrityCheck",
            "type": "Attribute",
            "format": "base64",
        }
    )
    integrity_check_algorithm: IntegrityCheckAlgorithm = field(
        default=IntegrityCheckAlgorithm.SHA_1,
        metadata={
            "name": "integrityCheckAlgorithm",
            "type": "Attribute",
        }
    )


@dataclass
class IvxbTs(Ts):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """
    class Meta:
        name = "IVXB_TS"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class Rto(RtoQtyQty):
    """A quantity constructed as the quotient of a numerator quantity divided
    by a denominator quantity.

    Common factors in the numerator and denominator are not
    automatically cancelled out.   supports titers (e.g., "1:128") and
    other quantities produced by laboratories that truly represent
    ratios. Ratios are not simply "structured numerics", particularly
    blood pressure measurements (e.g. "120/60") are not ratios. In many
    cases REAL should be used instead of .
    """
    class Meta:
        name = "RTO"


@dataclass
class ScExplicit:
    """An ST that optionally may have a code attached.

    The text must always be present if a code is present. The code is
    often a local code.

    :ivar content:
    :ivar reference: A telecommunication address (TEL), such as a URL
        for HTTP or FTP, which will resolve to precisely the same binary
        data that could as well have been provided as inline data.
    :ivar thumbnail:
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar representation: Specifies the representation of the binary
        data that is the content of the binary data value.
    :ivar media_type: Identifies the type of the encapsulated data and
        identifies a method to interpret or render the data.
    :ivar language: For character based information the language
        property specifies the human language of the text.
    :ivar compression: Indicates whether the raw byte data is
        compressed, and what compression algorithm was used.
    :ivar integrity_check: The integrity check is a short binary value
        representing a cryptographically strong checksum that is
        calculated over the binary data. The purpose of this property,
        when communicated with a reference is for anyone to validate
        later whether the reference still resolved to the same data that
        the reference resolved to when the encapsulated data value with
        reference was created.
    :ivar integrity_check_algorithm: Specifies the algorithm used to
        compute the integrityCheck value.
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    """
    class Meta:
        name = "SC_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    reference: Optional[TelExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    thumbnail: Optional[ThumbnailExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    representation: BinaryDataEncoding = field(
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        }
    )
    media_type: str = field(
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    compression: Optional[CompressionAlgorithm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    integrity_check: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "integrityCheck",
            "type": "Attribute",
            "format": "base64",
        }
    )
    integrity_check_algorithm: IntegrityCheckAlgorithm = field(
        default=IntegrityCheckAlgorithm.SHA_1,
        metadata={
            "name": "integrityCheckAlgorithm",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )


@dataclass
class StExplicit:
    """
    The character string data type stands for text data, primarily intended for
    machine processing (e.g., sorting, querying, indexing, etc.) Used for
    names, symbols, and formal expressions.

    :ivar content:
    :ivar reference: A telecommunication address (TEL), such as a URL
        for HTTP or FTP, which will resolve to precisely the same binary
        data that could as well have been provided as inline data.
    :ivar thumbnail:
    :ivar representation: Specifies the representation of the binary
        data that is the content of the binary data value.
    :ivar media_type: Identifies the type of the encapsulated data and
        identifies a method to interpret or render the data.
    :ivar language: For character based information the language
        property specifies the human language of the text.
    :ivar compression: Indicates whether the raw byte data is
        compressed, and what compression algorithm was used.
    :ivar integrity_check: The integrity check is a short binary value
        representing a cryptographically strong checksum that is
        calculated over the binary data. The purpose of this property,
        when communicated with a reference is for anyone to validate
        later whether the reference still resolved to the same data that
        the reference resolved to when the encapsulated data value with
        reference was created.
    :ivar integrity_check_algorithm: Specifies the algorithm used to
        compute the integrityCheck value.
    """
    class Meta:
        name = "ST_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    reference: Optional[TelExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    thumbnail: Optional[ThumbnailExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    representation: BinaryDataEncoding = field(
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        }
    )
    media_type: str = field(
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    compression: Optional[CompressionAlgorithm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    integrity_check: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "integrityCheck",
            "type": "Attribute",
            "format": "base64",
        }
    )
    integrity_check_algorithm: IntegrityCheckAlgorithm = field(
        default=IntegrityCheckAlgorithm.SHA_1,
        metadata={
            "name": "integrityCheckAlgorithm",
            "type": "Attribute",
        }
    )


@dataclass
class SxcmTs(Ts):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """
    class Meta:
        name = "SXCM_TS"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PqrExplicit:
    """A representation of a physical quantity in a unit from any code system.

    Used to show alternative representation for a physical quantity.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value: The magnitude of the measurement value in terms of the
        unit specified in the code.
    """
    class Meta:
        name = "PQR_explicit"

    original_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Tel(Url):
    """A telephone number (voice or fax), e-mail address, or other locator for
    a resource (information or service) mediated by telecommunication
    equipment.

    The address is specified as a URL qualified by time specification
    and use codes that help in deciding which address to use for a given
    time and purpose.

    :ivar useable_period: Specifies the periods of time during which the
        telecommunication address can be used.  For a telephone number,
        this can indicate the time of day in which the party can be
        reached on that telephone. For a web address, it may specify a
        time range in which the web content is promised to be available
        under the given address.
    :ivar use: One or more codes advising a system or user which
        telecommunication address in a set of like addresses to select
        for a given telecommunication need.
    """
    class Meta:
        name = "TEL"

    useable_period: List[SxcmTs] = field(
        default_factory=list,
        metadata={
            "name": "useablePeriod",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    use: List[TelecommunicationAddressUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Ed(Bin):
    """Data that is primarily intended for human interpretation or for further
    machine processing is outside the scope of HL7.

    This includes unformatted or formatted written language, multimedia
    data, or structured information as defined by a different standard
    (e.g., XML-signatures.)  Instead of the data itself, an ED may
    contain only a reference (see TEL.) Note that the ST data type is a
    specialization of when the  is text/plain.

    :ivar reference: A telecommunication address (TEL), such as a URL
        for HTTP or FTP, which will resolve to precisely the same binary
        data that could as well have been provided as inline data.
    :ivar thumbnail:
    :ivar media_type: Identifies the type of the encapsulated data and
        identifies a method to interpret or render the data.
    :ivar language: For character based information the language
        property specifies the human language of the text.
    :ivar compression: Indicates whether the raw byte data is
        compressed, and what compression algorithm was used.
    :ivar integrity_check: The integrity check is a short binary value
        representing a cryptographically strong checksum that is
        calculated over the binary data. The purpose of this property,
        when communicated with a reference is for anyone to validate
        later whether the reference still resolved to the same data that
        the reference resolved to when the encapsulated data value with
        reference was created.
    :ivar integrity_check_algorithm: Specifies the algorithm used to
        compute the integrityCheck value.
    """
    class Meta:
        name = "ED"

    reference: Optional[Tel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    thumbnail: Optional["Thumbnail"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    media_type: str = field(
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    compression: Optional[CompressionAlgorithm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    integrity_check: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "integrityCheck",
            "type": "Attribute",
            "format": "base64",
        }
    )
    integrity_check_algorithm: IntegrityCheckAlgorithm = field(
        default=IntegrityCheckAlgorithm.SHA_1,
        metadata={
            "name": "integrityCheckAlgorithm",
            "type": "Attribute",
        }
    )


@dataclass
class PqExplicit:
    """
    A dimensioned quantity expressing the result of a measurement act.

    :ivar translation: An alternative representation of the same
        physical quantity expressed in a different unit, of a different
        unit code system and possibly with a different value.
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar value: The magnitude of the quantity measured in terms of the
        unit.
    :ivar unit: The unit of measure specified in the Unified Code for
        Units of Measure (UCUM) [http://aurora.rg.iupui.edu/UCUM].
    """
    class Meta:
        name = "PQ_explicit"

    translation: List[PqrExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    unit: str = field(
        default="1",
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class Cd(Any):
    """A concept descriptor represents any kind of concept usually by giving a
    code defined in a code system.

    A concept descriptor can contain the original text or phrase that
    served as the basis of the coding and one or more translations into
    different coding systems. A concept descriptor can also contain
    qualifiers to describe, e.g., the concept of a "left foot" as a
    postcoordinated term built from the primary code "FOOT" and the
    qualifier "LEFT". In exceptional cases, the concept descriptor need
    not contain a code but only the original text describing that
    concept.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar qualifier: Specifies additional codes that increase the
        specificity of the primary code.
    :ivar translation: A set of other concept descriptors that translate
        this concept descriptor into other code systems.
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value_set:
    :ivar value_set_version:
    """
    class Meta:
        name = "CD"

    original_text: Optional[Ed] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    qualifier: List[Cr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    translation: List["Cd"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        }
    )


@dataclass
class IvlTsExplicit:
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar value:
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """
    class Meta:
        name = "IVL_TS_explicit"

    low: Optional[IvxbTsExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    width: List[PqExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    high: List[IvxbTsExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    center: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}|([0-9]{9,14}|[0-9]{14,14}\.[0-9]+)([+\-][0-9]{1,4})?",
        }
    )
    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class St:
    """
    The character string data type stands for text data, primarily intended for
    machine processing (e.g., sorting, querying, indexing, etc.) Used for
    names, symbols, and formal expressions.

    :ivar content:
    :ivar reference:
    :ivar thumbnail:
    :ivar representation:
    :ivar media_type:
    :ivar compression: Indicates whether the raw byte data is
        compressed, and what compression algorithm was used.
    :ivar integrity_check: The integrity check is a short binary value
        representing a cryptographically strong checksum that is
        calculated over the binary data. The purpose of this property,
        when communicated with a reference is for anyone to validate
        later whether the reference still resolved to the same data that
        the reference resolved to when the encapsulated data value with
        reference was created.
    :ivar integrity_check_algorithm: Specifies the algorithm used to
        compute the integrityCheck value.
    :ivar language:
    """
    class Meta:
        name = "ST"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    reference: Optional[Tel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    thumbnail: Optional[Ed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    representation: BinaryDataEncoding = field(
        init=False,
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        }
    )
    media_type: str = field(
        init=False,
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    compression: Optional[CompressionAlgorithm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    integrity_check: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "integrityCheck",
            "type": "Attribute",
            "format": "base64",
        }
    )
    integrity_check_algorithm: IntegrityCheckAlgorithm = field(
        default=IntegrityCheckAlgorithm.SHA_1,
        metadata={
            "name": "integrityCheckAlgorithm",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class Thumbnail(Ed):
    """A thumbnail is an abbreviated rendition of the full data.

    A thumbnail requires significantly fewer resources than the full
    data, while still maintaining some distinctive similarity with the
    full data. A thumbnail is typically used with by-reference
    encapsulated data. It allows a user to select data more efficiently
    before actually downloading through the reference.
    """
    class Meta:
        name = "thumbnail"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    thumbnail: Optional["Thumbnail"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )


@dataclass
class Adxp(St):
    """A character string that may have a type-tag signifying its role in the
    address.

    Typical parts that exist in about every address are street, house
    number, or post box, postal code, city, country but other roles may
    be defined regionally, nationally, or on an enterprise level (e.g.
    in military addresses). Addresses are usually broken up into lines,
    which are indicated by special line-breaking delimiter elements
    (e.g., DEL).

    :ivar part_type: Specifies whether an address part names the street,
        city, country, postal code, post box, etc. If the type is NULL
        the address part is unclassified and would simply appear on an
        address label as is.
    """
    class Meta:
        name = "ADXP"

    part_type: Optional[AddressPartType] = field(
        default=None,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class CdExplicit(Any):
    """A concept descriptor represents any kind of concept usually by giving a
    code defined in a code system.

    A concept descriptor can contain the original text or phrase that
    served as the basis of the coding and one or more translations into
    different coding systems. A concept descriptor can also contain
    qualifiers to describe, e.g., the concept of a "left foot" as a
    postcoordinated term built from the primary code "FOOT" and the
    qualifier "LEFT". In exceptional cases, the concept descriptor need
    not contain a code but only the original text describing that
    concept.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar qualifier: Specifies additional codes that increase the
        specificity of the primary code.
    :ivar translation: A set of other concept descriptors that translate
        this concept descriptor into other code systems.
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value_set:
    :ivar value_set_version:
    """
    class Meta:
        name = "CD_explicit"

    original_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    qualifier: List[Cr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    translation: List[Cd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        }
    )


@dataclass
class Ce:
    """Coded data, consists of a coded value (CV) and, optionally, coded
    value(s) from other coding systems that identify the same concept.

    Used when alternative codes may exist.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar qualifier:
    :ivar translation: A set of other concept descriptors that translate
        this concept descriptor into other code systems.
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value_set:
    :ivar value_set_version:
    """
    class Meta:
        name = "CE"

    original_text: Optional[Ed] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    qualifier: Optional[Cr] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    translation: List[Cd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        }
    )


@dataclass
class CeExplicit:
    """Coded data, consists of a coded value (CV) and, optionally, coded
    value(s) from other coding systems that identify the same concept.

    Used when alternative codes may exist.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar qualifier:
    :ivar translation: A set of other concept descriptors that translate
        this concept descriptor into other code systems.
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value_set:
    :ivar value_set_version:
    """
    class Meta:
        name = "CE_explicit"

    original_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    qualifier: Optional[Cr] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    translation: List[Cd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        }
    )


@dataclass
class Cs:
    """Coded data, consists of a code, display name, code system, and original
    text.

    Used when a single code value must be sent.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar qualifier:
    :ivar translation:
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value_set:
    :ivar value_set_version:
    """
    class Meta:
        name = "CS"

    original_text: Optional[Ed] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    qualifier: Optional[Cr] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    translation: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        }
    )


@dataclass
class Cv:
    """Coded data, consists of a code, display name, code system, and original
    text.

    Used when a single code value must be sent.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar qualifier:
    :ivar translation:
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value_set:
    :ivar value_set_version:
    """
    class Meta:
        name = "CV"

    original_text: Optional[Ed] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    qualifier: Optional[Cr] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    translation: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        }
    )


@dataclass
class EivlEvent:
    """
    A code for a common (periodical) activity of daily living based on which
    the event related periodic interval is specified.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar qualifier:
    :ivar translation: A set of other concept descriptors that translate
        this concept descriptor into other code systems.
    :ivar code:
    :ivar code_system:
    :ivar code_system_name:
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value_set:
    :ivar value_set_version:
    """
    class Meta:
        name = "EIVL.event"

    original_text: Optional[Ed] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    qualifier: Optional[Cr] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    translation: List[Cd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[TimingEvent] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    code_system: str = field(
        init=False,
        default="2.16.840.1.113883.5.139",
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: str = field(
        init=False,
        default="TimingEvent",
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        }
    )


@dataclass
class Enxp(St):
    """A character string token representing a part of a name.

    May have a type code signifying the role of the part in the whole
    entity name, and a qualifier code for more detail about the name
    part type. Typical name parts for person names are given names, and
    family names, titles, etc.

    :ivar part_type: Indicates whether the name part is a given name,
        family name, prefix, suffix, etc.
    :ivar qualifier: is a set of codes each of which specifies
        a certain subcategory of the name part in addition to
        the main name part type. For example, a given name may
        be flagged as a nickname, a family name may be a
        pseudonym or a name of public records.
    """
    class Meta:
        name = "ENXP"

    part_type: Optional[EntityNamePartType] = field(
        default=None,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
    qualifier: List[EntityNamePartQualifier] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class EnExplicit:
    """A name for a person.

    A sequence of name parts, such as given name or family name, prefix,
    suffix, etc. PN differs from EN because the qualifier type cannot
    include LS (Legal Status).

    :ivar content:
    :ivar delimiter:
    :ivar family:
    :ivar given:
    :ivar prefix:
    :ivar suffix:
    :ivar valid_time: An interval of time specifying the time during
        which the name is or was used for the entity. This accomodates
        the fact that people change names for people, places and things.
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar use: A set of codes advising a system or user which name in a
        set of like names to select for a given purpose. A name without
        specific use code might be a default name useful for any
        purpose, but a name with a specific use code would be preferred
        for that respective purpose.
    """
    class Meta:
        name = "EN_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    delimiter: List[EnExplicitDelimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    family: List[EnExplicitFamily] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    given: List[EnExplicitGiven] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    prefix: List[EnExplicitPrefix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    suffix: List[EnExplicitSuffix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    valid_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    use: List[EntityNameUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class OnExplicit:
    """A name for a person.

    A sequence of name parts, such as given name or family name, prefix,
    suffix, etc. PN differs from EN because the qualifier type cannot
    include LS (Legal Status).

    :ivar content:
    :ivar delimiter:
    :ivar prefix:
    :ivar suffix:
    :ivar valid_time: An interval of time specifying the time during
        which the name is or was used for the entity. This accomodates
        the fact that people change names for people, places and things.
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar use: A set of codes advising a system or user which name in a
        set of like names to select for a given purpose. A name without
        specific use code might be a default name useful for any
        purpose, but a name with a specific use code would be preferred
        for that respective purpose.
    """
    class Meta:
        name = "ON_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    delimiter: List[EnExplicitDelimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    prefix: List[EnExplicitPrefix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    suffix: List[EnExplicitSuffix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    valid_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    use: List[EntityNameUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class PnExplicit:
    """A name for a person.

    A sequence of name parts, such as given name or family name, prefix,
    suffix, etc. PN differs from EN because the qualifier type cannot
    include LS (Legal Status).

    :ivar content:
    :ivar delimiter:
    :ivar family:
    :ivar given:
    :ivar prefix:
    :ivar suffix:
    :ivar valid_time: An interval of time specifying the time during
        which the name is or was used for the entity. This accomodates
        the fact that people change names for people, places and things.
    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    :ivar use: A set of codes advising a system or user which name in a
        set of like names to select for a given purpose. A name without
        specific use code might be a default name useful for any
        purpose, but a name with a specific use code would be preferred
        for that respective purpose.
    """
    class Meta:
        name = "PN_explicit"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    delimiter: List[EnExplicitDelimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    family: List[EnExplicitFamily] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    given: List[EnExplicitGiven] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    prefix: List[EnExplicitPrefix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    suffix: List[EnExplicitSuffix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    valid_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    use: List[EntityNameUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Sc(St):
    """An ST that optionally may have a code attached.

    The text must always be present if a code is present. The code is
    often a local code.

    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    """
    class Meta:
        name = "SC"

    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )


@dataclass
class Co(Cv):
    """Coded data, where the domain from which the codeset comes is ordered.

    The Coded Ordinal data type adds semantics related to ordering so
    that models that make use of such domains may introduce model
    elements that involve statements about the order of the terms in a
    domain.
    """
    class Meta:
        name = "CO"


@dataclass
class Pqr(Cv):
    """A representation of a physical quantity in a unit from any code system.

    Used to show alternative representation for a physical quantity.

    :ivar value: The magnitude of the measurement value in terms of the
        unit specified in the code.
    """
    class Meta:
        name = "PQR"

    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AdxpAdditionalLocator(Adxp):
    class Meta:
        name = "adxp.additionalLocator"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.ADL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpBuildingNumberSuffix(Adxp):
    class Meta:
        name = "adxp.buildingNumberSuffix"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.BNS,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpCareOf(Adxp):
    class Meta:
        name = "adxp.careOf"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CAR,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpCensusTract(Adxp):
    class Meta:
        name = "adxp.censusTract"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CEN,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpCity(Adxp):
    class Meta:
        name = "adxp.city"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CTY,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpCountry(Adxp):
    class Meta:
        name = "adxp.country"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CNT,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpCounty(Adxp):
    class Meta:
        name = "adxp.county"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CPA,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpDelimiter(Adxp):
    class Meta:
        name = "adxp.delimiter"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DEL_VALUE,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpDeliveryAddressLine(Adxp):
    class Meta:
        name = "adxp.deliveryAddressLine"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DAL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpDeliveryInstallationArea(Adxp):
    class Meta:
        name = "adxp.deliveryInstallationArea"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DINSTA,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpDeliveryInstallationQualifier(Adxp):
    class Meta:
        name = "adxp.deliveryInstallationQualifier"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DINSTQ,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpDeliveryInstallationType(Adxp):
    class Meta:
        name = "adxp.deliveryInstallationType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DINST,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpDeliveryMode(Adxp):
    class Meta:
        name = "adxp.deliveryMode"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DMOD,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpDeliveryModeIdentifier(Adxp):
    class Meta:
        name = "adxp.deliveryModeIdentifier"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DMODID,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpDirection(Adxp):
    class Meta:
        name = "adxp.direction"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DIR,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpHouseNumber(Adxp):
    class Meta:
        name = "adxp.houseNumber"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.BNR,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpHouseNumberNumeric(Adxp):
    class Meta:
        name = "adxp.houseNumberNumeric"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.BNN,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpPostBox(Adxp):
    class Meta:
        name = "adxp.postBox"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.POB,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpPostalCode(Adxp):
    class Meta:
        name = "adxp.postalCode"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.ZIP,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpPrecinct(Adxp):
    class Meta:
        name = "adxp.precinct"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.PRE,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpState(Adxp):
    class Meta:
        name = "adxp.state"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STA,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpStreetAddressLine(Adxp):
    class Meta:
        name = "adxp.streetAddressLine"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.SAL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpStreetName(Adxp):
    class Meta:
        name = "adxp.streetName"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STR_VALUE,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpStreetNameBase(Adxp):
    class Meta:
        name = "adxp.streetNameBase"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STB,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpStreetNameType(Adxp):
    class Meta:
        name = "adxp.streetNameType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STTYP,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpUnitId(Adxp):
    class Meta:
        name = "adxp.unitID"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.UNID,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class AdxpUnitType(Adxp):
    class Meta:
        name = "adxp.unitType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.UNIT,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class EnDelimiter(Enxp):
    class Meta:
        name = "en.delimiter"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.DEL_VALUE,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class EnFamily(Enxp):
    class Meta:
        name = "en.family"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.FAM,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class EnGiven(Enxp):
    class Meta:
        name = "en.given"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.GIV,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class EnPrefix(Enxp):
    class Meta:
        name = "en.prefix"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.PFX,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class EnSuffix(Enxp):
    class Meta:
        name = "en.suffix"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.SFX,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )


@dataclass
class Ad(Any):
    """Mailing and home or office addresses.

    A sequence of address parts, such as street or post office Box,
    city, postal code, country, etc.

    :ivar content:
    :ivar delimiter:
    :ivar country:
    :ivar state:
    :ivar county:
    :ivar city:
    :ivar postal_code:
    :ivar street_address_line:
    :ivar house_number:
    :ivar house_number_numeric:
    :ivar direction:
    :ivar street_name:
    :ivar street_name_base:
    :ivar street_name_type:
    :ivar additional_locator:
    :ivar unit_id:
    :ivar unit_type:
    :ivar care_of:
    :ivar census_tract:
    :ivar delivery_address_line:
    :ivar delivery_installation_type:
    :ivar delivery_installation_area:
    :ivar delivery_installation_qualifier:
    :ivar delivery_mode:
    :ivar delivery_mode_identifier:
    :ivar building_number_suffix:
    :ivar post_box:
    :ivar precinct:
    :ivar useable_period: A GTS specifying the periods of time during
        which the address can be used. This is used to specify different
        addresses for different times of the year or to refer to
        historical addresses.
    :ivar use: A set of codes advising a system or user which address in
        a set of like addresses to select for a given purpose.
    :ivar is_not_ordered: A boolean value specifying whether the order
        of the address parts is known or not. While the address parts
        are always a Sequence, the order in which they are presented may
        or may not be known. Where this matters,  can be used to convey
        this information.
    """
    class Meta:
        name = "AD"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    delimiter: List[AdxpDelimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    country: List[AdxpCountry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    state: List[AdxpState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    county: List[AdxpCounty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    city: List[AdxpCity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    postal_code: List[AdxpPostalCode] = field(
        default_factory=list,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    street_address_line: List[AdxpStreetAddressLine] = field(
        default_factory=list,
        metadata={
            "name": "streetAddressLine",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    house_number: List[AdxpHouseNumber] = field(
        default_factory=list,
        metadata={
            "name": "houseNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    house_number_numeric: List[AdxpHouseNumberNumeric] = field(
        default_factory=list,
        metadata={
            "name": "houseNumberNumeric",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    direction: List[AdxpDirection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    street_name: List[AdxpStreetName] = field(
        default_factory=list,
        metadata={
            "name": "streetName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    street_name_base: List[AdxpStreetNameBase] = field(
        default_factory=list,
        metadata={
            "name": "streetNameBase",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    street_name_type: List[AdxpStreetNameType] = field(
        default_factory=list,
        metadata={
            "name": "streetNameType",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    additional_locator: List[AdxpAdditionalLocator] = field(
        default_factory=list,
        metadata={
            "name": "additionalLocator",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    unit_id: List[AdxpUnitId] = field(
        default_factory=list,
        metadata={
            "name": "unitID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    unit_type: List[AdxpUnitType] = field(
        default_factory=list,
        metadata={
            "name": "unitType",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    care_of: List[AdxpCareOf] = field(
        default_factory=list,
        metadata={
            "name": "careOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    census_tract: List[AdxpCensusTract] = field(
        default_factory=list,
        metadata={
            "name": "censusTract",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_address_line: List[AdxpDeliveryAddressLine] = field(
        default_factory=list,
        metadata={
            "name": "deliveryAddressLine",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_installation_type: List[AdxpDeliveryInstallationType] = field(
        default_factory=list,
        metadata={
            "name": "deliveryInstallationType",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_installation_area: List[AdxpDeliveryInstallationArea] = field(
        default_factory=list,
        metadata={
            "name": "deliveryInstallationArea",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_installation_qualifier: List[AdxpDeliveryInstallationQualifier] = field(
        default_factory=list,
        metadata={
            "name": "deliveryInstallationQualifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_mode: List[AdxpDeliveryMode] = field(
        default_factory=list,
        metadata={
            "name": "deliveryMode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    delivery_mode_identifier: List[AdxpDeliveryModeIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "deliveryModeIdentifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    building_number_suffix: List[AdxpBuildingNumberSuffix] = field(
        default_factory=list,
        metadata={
            "name": "buildingNumberSuffix",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    post_box: List[AdxpPostBox] = field(
        default_factory=list,
        metadata={
            "name": "postBox",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    precinct: List[AdxpPrecinct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    useable_period: List[SxcmTs] = field(
        default_factory=list,
        metadata={
            "name": "useablePeriod",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    use: List[PostalAddressUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    is_not_ordered: Optional[str] = field(
        default=None,
        metadata={
            "name": "isNotOrdered",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class Pq(Qty):
    """
    A dimensioned quantity expressing the result of a measurement act.

    :ivar translation: An alternative representation of the same
        physical quantity expressed in a different unit, of a different
        unit code system and possibly with a different value.
    :ivar value: The magnitude of the quantity measured in terms of the
        unit.
    :ivar unit: The unit of measure specified in the Unified Code for
        Units of Measure (UCUM) [http://aurora.rg.iupui.edu/UCUM].
    """
    class Meta:
        name = "PQ"

    translation: List[Pqr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    unit: str = field(
        default="1",
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class IvlTs(SxcmTs):
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    """
    class Meta:
        name = "IVL_TS"

    low: Optional[IvxbTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    width: List[Pq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    high: List[IvxbTs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    center: Optional[Ts] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )


@dataclass
class En(Any):
    """A name for a person, organization, place or thing.

    A sequence of name parts, such as given name or family name, prefix,
    suffix, etc. Examples for entity name values are "Jim Bob Walton,
    Jr.", "Health Level Seven, Inc.", "Lake Tahoe", etc. An entity name
    may be as simple as a character string or may consist of several
    entity name parts, such as, "Jim", "Bob", "Walton", and "Jr.",
    "Health Level Seven" and "Inc.", "Lake" and "Tahoe".

    :ivar content:
    :ivar delimiter:
    :ivar family:
    :ivar given:
    :ivar prefix:
    :ivar suffix:
    :ivar valid_time: An interval of time specifying the time during
        which the name is or was used for the entity. This accomodates
        the fact that people change names for people, places and things.
    :ivar use: A set of codes advising a system or user which name in a
        set of like names to select for a given purpose. A name without
        specific use code might be a default name useful for any
        purpose, but a name with a specific use code would be preferred
        for that respective purpose.
    """
    class Meta:
        name = "EN"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    delimiter: List[EnDelimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    family: List[EnFamily] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    given: List[EnGiven] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    prefix: List[EnPrefix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    suffix: List[EnSuffix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    valid_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    use: List[EntityNameUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class On:
    """A name for an organization.

    A sequence of name parts.

    :ivar content:
    :ivar delimiter:
    :ivar family:
    :ivar given:
    :ivar prefix:
    :ivar suffix:
    :ivar valid_time: An interval of time specifying the time during
        which the name is or was used for the entity. This accomodates
        the fact that people change names for people, places and things.
    :ivar use: A set of codes advising a system or user which name in a
        set of like names to select for a given purpose. A name without
        specific use code might be a default name useful for any
        purpose, but a name with a specific use code would be preferred
        for that respective purpose.
    """
    class Meta:
        name = "ON"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    delimiter: List[EnDelimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    family: List[EnFamily] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    given: List[EnGiven] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    prefix: List[EnPrefix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    suffix: List[EnSuffix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "sequential": True,
        }
    )
    valid_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    use: List[EntityNameUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Pn(En):
    """A name for a person.

    A sequence of name parts, such as given name or family name, prefix,
    suffix, etc. PN differs from EN because the qualifier type cannot
    include LS (Legal Status).
    """
    class Meta:
        name = "PN"


@dataclass
class Tn(En):
    """
    A restriction of entity name that is effectively a simple string used for a
    simple name for things and places.
    """
    class Meta:
        name = "TN"
