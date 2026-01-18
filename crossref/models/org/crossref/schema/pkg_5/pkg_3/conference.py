from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_paper import (
    ConferencePaper,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.event_metadata import (
    EventMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.proceedings_metadata import (
    ProceedingsMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.proceedings_series_metadata import (
    ProceedingsSeriesMetadata,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Conference:
    """
    Container for all information about a single conference and its
    proceedings.

    If a conference proceedings spans multiple volumes, each volume must be
    contained in a unique conference element.
    """

    class Meta:
        name = "conference"
        namespace = "http://www.crossref.org/schema/5.3.1"

    contributors: None | Contributors = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    event_metadata: None | EventMetadata = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    proceedings_series_metadata: None | ProceedingsSeriesMetadata = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    proceedings_metadata: None | ProceedingsMetadata = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conference_paper: list[ConferencePaper] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
