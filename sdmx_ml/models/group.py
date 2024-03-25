from dataclasses import dataclass

from sdmx_ml.models.group_type import GroupType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class Group(GroupType):
    """Group describes a group descriptor in a data structure definition.

    It is a set metadata concepts (and possibly their values) that
    define a partial key derived from the key descriptor in a data
    structure definition.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
