from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_alt_script import (
    StdAltScript,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_designator import (
    StdDesignator,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_variant_form import (
    StdVariantForm,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class StdDesignatorT:
    class Meta:
        name = "std_designator_t"

    std_designator: StdDesignator = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "required": True,
        }
    )
    std_alt_script: list[StdAltScript] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    std_variant_form: list[StdVariantForm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
