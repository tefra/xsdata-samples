from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.company_name_type import CompanyNameType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class UniqueIdType:
    """
    An identifier used to uniquely reference an object in a system (e.g. an
    airline reservation reference, customer profile reference, booking
    confirmation number, or a reference to a previous availability quote).

    Attributes:
        company_name: Identifies the company that is associated with the
            UniqueID.
        url: URL that identifies the location associated with the record
            identified by the UniqueID.
        type_value: A reference to the type of object defined by the
            UniqueID element. Refer to OTA Code List Unique ID Type
            (UIT).
        instance: The identification of a record as it exists at a point
            in time. An instance is used in update messages where the
            sender must assure the server that the update sent refers to
            the most recent modification level of the object being
            updated.
        id: A unique identifying value assigned by the creating system.
            The ID attribute may be used to reference a primary-key
            value within a database or in a particular implementation.
        id_context: Used to identify the source of the identifier (e.g.
            IATA, ABTA, etc.).
    """

    class Meta:
        name = "UniqueID_Type"

    company_name: None | CompanyNameType = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    instance: None | str = field(
        default=None,
        metadata={
            "name": "Instance",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        },
    )
    id_context: None | str = field(
        default=None,
        metadata={
            "name": "ID_Context",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
