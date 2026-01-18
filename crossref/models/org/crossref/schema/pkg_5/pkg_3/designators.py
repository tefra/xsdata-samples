from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_adopted_from import (
    StdAdoptedFrom,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_alt_as_published import (
    StdAltAsPublished,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_as_published import (
    StdAsPublished,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_family_designator import (
    StdFamilyDesignator,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_revision_of import (
    StdRevisionOf,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_set_designator import (
    StdSetDesignator,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_supersedes import (
    StdSupersedes,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_undated_designator import (
    StdUndatedDesignator,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Designators:
    """
    A wrapper for designators or other primary identifiers for a standard.
    """

    class Meta:
        name = "designators"
        namespace = "http://www.crossref.org/schema/5.3.1"

    std_family_designator: None | StdFamilyDesignator = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    std_set_designator: None | StdSetDesignator = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    std_undated_designator: None | StdUndatedDesignator = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    std_as_published: None | StdAsPublished = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    std_alt_as_published: list[StdAltAsPublished] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    std_supersedes: list[StdSupersedes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    std_adopted_from: list[StdAdoptedFrom] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    std_revision_of: list[StdRevisionOf] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
