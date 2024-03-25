from dataclasses import dataclass

from sdmx_ml.models.item_scheme_map_type import ItemSchemeMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class OrganisationSchemeMapType(ItemSchemeMapType):
    """
    OrganisationSchemeMapType defines the structure of a map which identifies
    relationships between organisations in different organisation schemes.
    """
