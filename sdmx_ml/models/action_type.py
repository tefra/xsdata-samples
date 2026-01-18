from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


class ActionType(Enum):
    """
    ActionType provides a list of actions, describing the intention of the
    data transmission from the sender's side.

    Each action provided at the data or metadata set level applies to the
    entire data set for which it is given. Note that the actions indicated
    in the Message Header are optional, and used to summarize specific
    actions indicated with this data type for all registry interactions.
    The "Informational" value is used when the message contains information
    in response to a query, rather than being used to invoke a maintenance
    activity.

    :cvar APPEND: Append - this is an incremental update for an existing
        data/metadata set or the provision of new data or documentation
        (attribute values) formerly absent. If any of the supplied data
        or metadata is already present, it will not replace that data or
        metadata. This corresponds to the "Update" value found in
        version 1.0 of the SDMX Technical Standards.
    :cvar REPLACE: Replace - data/metadata is to be replaced, and may
        also include additional data/metadata to be appended. The
        replacement occurs at the level of the observation - that is, it
        is not possible to replace an entire series.
    :cvar DELETE: Delete - data/metadata is to be deleted. Deletion
        occurs at the lowest level object. For instance, if a delete
        data message contains a series with no observations, then the
        entire series will be deleted. If the series contains
        observations, then only those observations specified will be
        deleted. The same basic concept applies for attributes. If a
        series or observation in a delete message contains attributes,
        then only those attributes will be deleted.
    :cvar INFORMATION: Informational - data/metadata is being exchanged
        for informational purposes only, and not meant to update a
        system.
    """

    APPEND = "Append"
    REPLACE = "Replace"
    DELETE = "Delete"
    INFORMATION = "Information"
