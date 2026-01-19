from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


class ActionType(Enum):
    """
    ActionType provides a list of actions, describing the intention of the
    data transmission from the sender's side.

    Each action provided at the data or metadata set level applies to the
    entire data set for which it is given. Note that the actions indicated
    in the Message Header are optional, and used to summarize specific
    actions indicated with this data type for all registry interactions.
    When absent (not recommended), Merge is assumed.

    :cvar MERGE: Merge - Data or data-related reference metadata is to
        be merged, through either update or insertion depending on
        already existing information. This operation does not allow
        deleting any component values. Updating individual values in
        multi-valued measure, attribute or data-related reference
        metadata values is not supported either. The complete multi-
        valued value is to be provided. Only non-dimensional components
        (measure, attribute or data-related reference metadata values)
        can be omitted (null or absent) as long as at least one of those
        components is present. Bulk merges are thus not supported. Only
        the provided values are merged. Dimension values for higher-
        level (data-related reference metadata) attributes can be
        switched-off (using ~) when those are not attached to these
        dimensions. All observations as well as the sets of data-related
        reference metadata attributes at specific dimension combinations
        impacted by the Merge action change their time stamp when used
        to update an SDMX storage system.
    :cvar APPEND: Append - Deprecated. When used to update an SDMX
        storage system, the Merge action is assumed.
    :cvar REPLACE: Replace - Data or data-related reference metadata is
        to be replaced, through either update, insert or delete
        depending on already existing information. A full replacement is
        hereby assumed to take place at specific “replacement levels”:
        for entire observations and for any specific dimension
        combination for data-related reference metadata attributes.
        Within these “replacement levels” the provided values are
        inserted or updated, and omitted values are deleted. Values
        provided for the other attributes (those above the observation
        level) are merged (see Merge action). Only non-dimensional
        components (measure, attribute or data-related reference
        metadata values) can be omitted (null or absent). Bulk replacing
        is thus not supported. Dimension values for higher-level (data-
        related reference metadata) attributes can be switched-off
        (using ~) when those are not attached to these dimensions.
        Replacing non-existing elements is not resulting in an error.
        All observations as well as the sets of data-related reference
        metadata attributes at specific dimension combinations impacted
        by the replace action change their time stamp when used to
        update an SDMX storage system. Because the Replace action always
        takes place at specific levels, it cannot be used to replace a
        whole dataset or a whole series. However, a “replace all” effect
        can be achieved by combining an `Delete` dataset containing a
        completely wildcarded key (where all dimension values are
        omitted) with a `Merge` or `Replace` dataset within the same
        data message. Similarly, to replace a whole series, a message
        can combine a `Delete` dataset containing only the partial key
        of the series (where the not used dimension values are omitted)
        with a `Merge` or `Replace` dataset for that series.
    :cvar DELETE: Delete - Data or data-related reference metadata is to
        be deleted. Deletion is hereby assumed to take place at the
        lowest level of detail provided in the message. Any component
        (including dimensions) can be omitted (dimensions: empty,
        others: null or absent). Omitting dimension values allows for
        bulk deletions. Partially omitting non-dimension component
        values allows restricting the deletion of measure, attribute or
        data-related reference metadata values to the ones being
        present. Instead of real values for non-dimensional components,
        it is sufficient to use any valid value. With this, whole
        datasets, any slices of observations for dimension groups such
        as time series, observations or individual measure, attribute
        and data-related reference metadata attributes values can be
        deleted. Dimension values for higher-level (data-related
        reference metadata) attributes can be switched-off (using ~)
        when those are not attached to these dimensions. Deleting non-
        existing elements or values is not resulting in an error. All
        observations as well as the sets of attributes and data-related
        reference metadata at higher partial keys impacted by the Delete
        action change their time stamp when used to update an SDMX
        storage system.
    :cvar INFORMATION: Information - Deprecated. When used to update an
        SDMX storage system, the Merge action is assumed.
    """

    MERGE = "Merge"
    APPEND = "Append"
    REPLACE = "Replace"
    DELETE = "Delete"
    INFORMATION = "Information"
