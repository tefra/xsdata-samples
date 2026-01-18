from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.document import Document

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Apisrequirements:
    """
    Specific details for APIS Requirements.

    Parameters
    ----------
    document
    key
        Unique identifier for this APIS Requirements - use this key when a
        single APIS Requirements is shared by multiple elements.
    level
        Applicability level of the Document. Required, Supported,
        API_Supported or Unknown
    gender_required
    date_of_birth_required
    required_documents
        What are required documents for the APIS Requirement. One,
        FirstAndOneOther or All
    nationality_required
        Nationality of the traveler is required for booking for some
        suppliers.
    """

    class Meta:
        name = "APISRequirements"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    document: list[Document] = field(
        default_factory=list,
        metadata={
            "name": "Document",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | object = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    level: None | str = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
        },
    )
    gender_required: None | bool = field(
        default=None,
        metadata={
            "name": "GenderRequired",
            "type": "Attribute",
        },
    )
    date_of_birth_required: None | bool = field(
        default=None,
        metadata={
            "name": "DateOfBirthRequired",
            "type": "Attribute",
        },
    )
    required_documents: None | str = field(
        default=None,
        metadata={
            "name": "RequiredDocuments",
            "type": "Attribute",
        },
    )
    nationality_required: None | bool = field(
        default=None,
        metadata={
            "name": "NationalityRequired",
            "type": "Attribute",
        },
    )
