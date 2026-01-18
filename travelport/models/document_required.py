from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class DocumentRequired:
    """
    Additional Details, Documents , Project IDs.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    doc_type: None | str = field(
        default=None,
        metadata={
            "name": "DocType",
            "type": "Attribute",
        },
    )
    include_exclude_use_ind: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeExcludeUseInd",
            "type": "Attribute",
        },
    )
    doc_id: None | str = field(
        default=None,
        metadata={
            "name": "DocId",
            "type": "Attribute",
        },
    )
    allowed_ids: None | str = field(
        default=None,
        metadata={
            "name": "AllowedIds",
            "type": "Attribute",
        },
    )
