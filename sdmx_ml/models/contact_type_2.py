from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from sdmx_ml.models.name import Name
from sdmx_ml.models.text_type import TextType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class ContactType2:
    """
    ContactType provides defines the contact information about a party.

    :ivar name: Name contains a human-readable name for the contact.
    :ivar department: Department is designation of the organisational
        structure by a linguistic expression, within which the contact
        person works.
    :ivar role: Role is the responsibility of the contact person with
        respect to the object for which this person is the contact.
    :ivar choice:
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
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    role: tuple[TextType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    choice: tuple[
        ContactType2.Telephone
        | ContactType2.Fax
        | ContactType2.X400
        | ContactType2.Uri
        | ContactType2.Email,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Telephone",
                    "type": ForwardRef("ContactType2.Telephone"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "Fax",
                    "type": ForwardRef("ContactType2.Fax"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "X400",
                    "type": ForwardRef("ContactType2.X400"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "URI",
                    "type": ForwardRef("ContactType2.Uri"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "Email",
                    "type": ForwardRef("ContactType2.Email"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
            ),
        },
    )

    @dataclass(frozen=True)
    class Telephone:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class Fax:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class X400:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class Uri:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class Email:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
