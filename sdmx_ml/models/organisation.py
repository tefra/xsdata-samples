from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.item_type import OrganisationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class Organisation(OrganisationType):
    """
    Organisation is an abstract substitution head for a generic
    organisation.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
