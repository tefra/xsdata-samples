from __future__ import annotations

from dataclasses import dataclass, field

from .ref import Ref
from .referrable_subtypes_enum import ReferrableSubtypesEnum
from .resolution_policy_enum_simple import ResolutionPolicyEnumSimple
from .show_content_enum_simple import ShowContentEnumSimple
from .show_resource_alias_name_enum_simple import (
    ShowResourceAliasNameEnumSimple,
)
from .show_resource_category_enum_simple import ShowResourceCategoryEnumSimple
from .show_resource_long_name_enum_simple import ShowResourceLongNameEnumSimple
from .show_resource_number_enum_simple import ShowResourceNumberEnumSimple
from .show_resource_page_enum_simple import ShowResourcePageEnumSimple
from .show_resource_short_name_enum_simple import (
    ShowResourceShortNameEnumSimple,
)
from .show_resource_type_enum_simple import ShowResourceTypeEnumSimple
from .show_see_enum_simple import ShowSeeEnumSimple
from .single_language_long_name import SingleLanguageLongName

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Xref:
    """
    This represents a cross-reference within documentation.

    :ivar label_1: This allows to specify a replacement text which shall
        be rendered if showContent is selected.
    :ivar referrable_ref: This establishes the reference in Autosar
        style
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    :ivar resolution_policy: Indicates if the content of the xref
        element follow a dedicated resolution policy. The default is
        "NO-SLOPPY".
    :ivar show_content: Indicates if the content of the xref element
        shall be rendered. The default is "NO-SHOW-CONTENT".
    :ivar show_resource_alias_name: This indicates if the alias names of
        the referenced objects shall be rendered. This means this is
        some kind of backward searching: look whether there is an  alias
        for the referenced object, if yes, print it. If there is more
        than one AliasNameSet, Xref might render all of those. If no
        alilas is found and showResourceShortName is set to
        NoShowShortName, then the shortName of the reference target
        shall be displayed. By this showResourceAliasName is similar to
        showResourceShortName but shows the aliasName instead of the
        shortName. Default is NO-SHOW-ALIAS-NAME.
    :ivar show_resource_category: Indicates if the category of the
        referenced resource shall be rendered. Default is "NO-SHOW-
        CATEGORY".
    :ivar show_resource_long_name: Indicates if the longName of the
        referenced resource shall be rendered. Default is "SHOW-LONG-
        NAME".
    :ivar show_resource_number: Indicates if the Number of the
        referenced resource shall be shown. Default is "SHOW--NUMBER"
    :ivar show_resource_page: Indicates if the page number of the
        referenced resource shall be shown. Default is "SHOW-PAGE"
    :ivar show_resource_short_name: Indicates if the shortJName of the
        referenced resource shall be shown. Default is "SHOW-SHORT-NAME"
    :ivar show_resource_type: Indicates if the type of the referenced
        Resource shall be shown. Default is "SHOW-TYPE"
    :ivar show_see: Indicates if the word "see " shall be shown before
        the reference. Default is "NO-SHOW-SEE". Note that this is there
        for compatibility reasons only.
    """

    class Meta:
        name = "XREF"

    label_1: SingleLanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LABEL-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    referrable_ref: Xref.ReferrableRef | None = field(
        default=None,
        metadata={
            "name": "REFERRABLE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    resolution_policy: ResolutionPolicyEnumSimple | None = field(
        default=None,
        metadata={
            "name": "RESOLUTION-POLICY",
            "type": "Attribute",
        },
    )
    show_content: ShowContentEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-CONTENT",
            "type": "Attribute",
        },
    )
    show_resource_alias_name: ShowResourceAliasNameEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-RESOURCE-ALIAS-NAME",
            "type": "Attribute",
        },
    )
    show_resource_category: ShowResourceCategoryEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-RESOURCE-CATEGORY",
            "type": "Attribute",
        },
    )
    show_resource_long_name: ShowResourceLongNameEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-RESOURCE-LONG-NAME",
            "type": "Attribute",
        },
    )
    show_resource_number: ShowResourceNumberEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-RESOURCE-NUMBER",
            "type": "Attribute",
        },
    )
    show_resource_page: ShowResourcePageEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-RESOURCE-PAGE",
            "type": "Attribute",
        },
    )
    show_resource_short_name: ShowResourceShortNameEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-RESOURCE-SHORT-NAME",
            "type": "Attribute",
        },
    )
    show_resource_type: ShowResourceTypeEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-RESOURCE-TYPE",
            "type": "Attribute",
        },
    )
    show_see: ShowSeeEnumSimple | None = field(
        default=None,
        metadata={
            "name": "SHOW-SEE",
            "type": "Attribute",
        },
    )

    @dataclass
    class ReferrableRef(Ref):
        dest: ReferrableSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
