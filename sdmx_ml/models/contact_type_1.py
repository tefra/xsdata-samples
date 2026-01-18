from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from sdmx_ml.models.name import Name
from sdmx_ml.models.text_type import TextType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ContactType1:
    """
    ContactType describes the structure of a contact's details.

    :ivar name:
    :ivar department: Department is designation of the organisational
        structure by a linguistic expression, within which the contact
        person works.
    :ivar role: Role is the responsibility of the contact person with
        respect to the object for which this person is the contact.
    :ivar choice:
    :ivar id: The id attribute is used to carry user id information for
        the contact.
    """

    class Meta:
        name = "ContactType"

    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    department: tuple[TextType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    role: tuple[TextType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    choice: tuple[
        ContactType1.Telephone
        | ContactType1.Fax
        | ContactType1.X400
        | ContactType1.Uri
        | ContactType1.Email,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Telephone",
                    "type": ForwardRef("ContactType1.Telephone"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Fax",
                    "type": ForwardRef("ContactType1.Fax"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "X400",
                    "type": ForwardRef("ContactType1.X400"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "URI",
                    "type": ForwardRef("ContactType1.Uri"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Email",
                    "type": ForwardRef("ContactType1.Email"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )

    @dataclass(frozen=True)
    class Telephone:
        value: None | str = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class Fax:
        value: None | str = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class X400:
        value: None | str = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class Uri:
        value: None | str = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class Email:
        value: None | str = field(
            default=None,
            metadata={
                "required": True,
            },
        )
