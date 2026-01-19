from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.description import Description
from sdmx_ml.models.identifiable_type import IdentifiableType
from sdmx_ml.models.name import Name

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


@dataclass(frozen=True, kw_only=True)
class NameableType(IdentifiableType):
    """
    NameableType is an abstract base type for all nameable objects.

    :ivar name: Name provides for a human-readable name for the object.
        This may be provided in multiple, parallel language-equivalent
        forms.
    :ivar description: Description provides for a longer human-readable
        description of the object. This may be provided in multiple,
        parallel language-equivalent forms.
    """

    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common",
            "min_occurs": 1,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common",
        },
    )
