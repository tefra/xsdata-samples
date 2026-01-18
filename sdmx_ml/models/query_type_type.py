from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


class QueryTypeType(Enum):
    """
    QueryType provides an enumeration of values which specify the objects
    in the result-set for a registry query.

    :cvar DATA_SETS: Only references data sets should be returned.
    :cvar METADATA_SETS: Only references to metadata sets should be
        returned.
    :cvar ALL_SETS: References to both data sets and metadata sets
        should be returned.
    """

    DATA_SETS = "DataSets"
    METADATA_SETS = "MetadataSets"
    ALL_SETS = "AllSets"
