from dataclasses import dataclass, field
from typing import List, Optional, Type
from .caption import Caption
from .category_string import CategoryString
from .chapter_enum_break_simple import ChapterEnumBreakSimple
from .condition_by_formula import ConditionByFormula
from .date import Date
from .doc_revision import DocRevision
from .ecuc_definition_element_subtypes_enum import (
    EcucDefinitionElementSubtypesEnum,
)
from .ecuc_query_subtypes_enum import EcucQuerySubtypesEnum
from .float_enum_simple import FloatEnumSimple
from .frame_enum_simple import FrameEnumSimple
from .identifier import Identifier
from .indent_sample import IndentSample
from .keep_with_previous_enum_simple import KeepWithPreviousEnumSimple
from .l_enum import LEnum
from .l_graphic import LGraphic
from .l_paragraph import LParagraph
from .l_verbatim import LVerbatim
from .list_enum_simple import ListEnumSimple
from .msr_query_props import MsrQueryProps
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multi_language_plain_text import MultiLanguagePlainText
from .multilanguage_long_name import MultilanguageLongName
from .note_type_enum_simple import NoteTypeEnumSimple
from .pgwide_enum_simple import PgwideEnumSimple
from .post_build_variant_condition import PostBuildVariantCondition
from .ref import Ref
from .referrable_subtypes_enum import ReferrableSubtypesEnum
from .sd import Sd
from .sdf import Sdf
from .sdg_caption import SdgCaption
from .sdg_caption_subtypes_enum import SdgCaptionSubtypesEnum
from .short_name_fragment import ShortNameFragment
from .standard_name_enum import StandardNameEnum
from .string import String
from .sw_systemconst_subtypes_enum import SwSystemconstSubtypesEnum
from .traceable_subtypes_enum import TraceableSubtypesEnum
from .verbatim_string import VerbatimString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Annotation:
    """
    This is a plain annotation which does not have further formal data.

    :ivar label: This is the headline for the annotation.
    :ivar annotation_origin: This attribute identifies the origin of the
        annotation. It is an arbitrary string since it can be an
        individual's name as well as the name of a tool or even the name
        of a process step.
    :ivar annotation_text: This is the text of the annotation.
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
    """

    class Meta:
        name = "ANNOTATION"

    label: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotation_origin: Optional[String] = field(
        default=None,
        metadata={
            "name": "ANNOTATION-ORIGIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotation_text: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "ANNOTATION-TEXT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )


@dataclass
class DefItem:
    """This represents an entry in a definition list.

    The defined item is specified using shortName and longName.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar def_value: This represents the definition part of the DefItem.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    :ivar help_entry: This specifies an entry point in an online help
        system to be linked with the parent class. The syntax shall be
        defined by the applied help system respectively help system
        generator.
    """

    class Meta:
        name = "DEF-ITEM"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["DefItem.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    def_value: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )
    help_entry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HELP-ENTRY",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )


@dataclass
class MsrQueryP2:
    """
    This meta-class represents the ability to express a query which yields the
    content of a DocumentationBlock as a result.

    :ivar msr_query_props: This is argument and properties of the
        DocumentationBlock query.
    :ivar msr_query_result_p_2: This represents the result of the query.
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
    """

    class Meta:
        name = "MSR-QUERY-P-2"

    msr_query_props: Optional[MsrQueryProps] = field(
        default=None,
        metadata={
            "name": "MSR-QUERY-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msr_query_result_p_2: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "MSR-QUERY-RESULT-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )


@dataclass
class MultiLanguageParagraph:
    """
    This is the content model of a multilingual paragraph in a documentation.

    :ivar l_1: This is the paragraph content in one partiucular
        language.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    :ivar help_entry: This specifies an entry point in an online help
        system to be linked with the parent class. The syntax shall be
        defined by the applied help system respectively help system
        generator.
    """

    class Meta:
        name = "MULTI-LANGUAGE-PARAGRAPH"

    l_1: List[LParagraph] = field(
        default_factory=list,
        metadata={
            "name": "L-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )
    help_entry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HELP-ENTRY",
            "type": "Attribute",
        },
    )


@dataclass
class MultiLanguageVerbatim:
    """This class represents multilingual Verbatim.

    Verbatim means, that white-space is maintained. When Verbatim is
    rendered in PDF or Online media, white-space is obeyed. Blanks are
    rendered as well as newline characters.

    :ivar l_5: This the text in one particular language.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    :ivar allow_break: This indicates if the verbatim text might be
        split on multiple pages. Default is "1".
    :ivar float_value: Indicate whether it is allowed to break the
        element. The following values are allowed:
    :ivar help_entry: This specifies an entry point in an online help
        system to be linked with the parent class. The syntax shall be
        defined by the applied help system respectively help system
        generator.
    :ivar pgwide: Used to indicate wether the figure should take the
        complete page width (value = "pgwide") or not (value =
        "noPgwide").
    """

    class Meta:
        name = "MULTI-LANGUAGE-VERBATIM"

    l_5: List[LVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "L-5",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )
    allow_break: Optional[str] = field(
        default=None,
        metadata={
            "name": "ALLOW-BREAK",
            "type": "Attribute",
        },
    )
    float_value: Optional[FloatEnumSimple] = field(
        default=None,
        metadata={
            "name": "FLOAT",
            "type": "Attribute",
        },
    )
    help_entry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HELP-ENTRY",
            "type": "Attribute",
        },
    )
    pgwide: Optional[PgwideEnumSimple] = field(
        default=None,
        metadata={
            "name": "PGWIDE",
            "type": "Attribute",
        },
    )


@dataclass
class BlueprintFormula:
    """This class express the extension of the Formula Language to provide
    formalized blueprint-Value resp.

    blueprintCondition.

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
    :ivar content:
    """

    class Meta:
        name = "BLUEPRINT-FORMULA"

    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "SYSC-STRING-REF",
                    "type": Type["BlueprintFormula.SyscStringRef"],
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "SYSC-REF",
                    "type": Type["BlueprintFormula.SyscRef"],
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "ECUC-QUERY-REF",
                    "type": Type["BlueprintFormula.EcucQueryRef"],
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "ECUC-REF",
                    "type": Type["BlueprintFormula.EcucRef"],
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "VERBATIM",
                    "type": MultiLanguageVerbatim,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
        },
    )

    @dataclass
    class SyscStringRef(Ref):
        dest: Optional[SwSystemconstSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SyscRef(Ref):
        dest: Optional[SwSystemconstSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class EcucQueryRef(Ref):
        dest: Optional[EcucQuerySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class EcucRef(Ref):
        dest: Optional[EcucDefinitionElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class DefList:
    """This meta-class represents the ability to express a list of definitions.

    Note that a definition list might be rendered similar to a labeled
    list but has a particular semantics to denote definitions.

    :ivar def_item: This is one entry in the definition list. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    """

    class Meta:
        name = "DEF-LIST"

    def_item: List[DefItem] = field(
        default_factory=list,
        metadata={
            "name": "DEF-ITEM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )


@dataclass
class MlFigure:
    """
    This metaclass represents the ability to embed a figure.

    :ivar figure_caption: This element specifies the title of an
        illustration.
    :ivar l_graphic:
    :ivar verbatim: &lt;verbatim&gt; is a paragraph in which white-space
        (in particular blanks and line feeds) is obeyed. This enables
        basic preformatting to be carried out, which can even be
        displayed on simple devices. Behavior is the same as PRE in HTML
        .
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    :ivar frame: Used to defined the frame line around a figure. It can
        assume the following values: * TOP - Border at the top of the
        figure * BOTTOM - Border at the bottom of the figure * TOPBOT -
        Borders at the top and bottom of  the figure * ALL - Borders all
        around the figure * SIDES - Borders at the sides of the figure *
        NONE - No borders around the figure
    :ivar help_entry: This specifies an entry point in an online help
        system to be linked with the parent class. The syntax shall be
        defined by the applied help system respectively help system
        generator.
    :ivar pgwide: Used to indicate wether the figure should take the
        complete page width (value = "pgwide") or not (value =
        "noPgwide").
    """

    class Meta:
        name = "ML-FIGURE"

    figure_caption: Optional[Caption] = field(
        default=None,
        metadata={
            "name": "FIGURE-CAPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    l_graphic: List[LGraphic] = field(
        default_factory=list,
        metadata={
            "name": "L-GRAPHIC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    verbatim: Optional[MultiLanguageVerbatim] = field(
        default=None,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )
    frame: Optional[FrameEnumSimple] = field(
        default=None,
        metadata={
            "name": "FRAME",
            "type": "Attribute",
        },
    )
    help_entry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HELP-ENTRY",
            "type": "Attribute",
        },
    )
    pgwide: Optional[PgwideEnumSimple] = field(
        default=None,
        metadata={
            "name": "PGWIDE",
            "type": "Attribute",
        },
    )


@dataclass
class MlFormula:
    """This meta-class represents the ability to express a formula in a
    documentation.

    The formula can be expressed by various means. If more than one
    representation is available, they need to be consistent. The
    rendering system can use the representation which is most
    appropriate.

    :ivar formula_caption: This element specifies the identification or
        heading of a formula.
    :ivar l_graphic:
    :ivar verbatim: this represents a formula using only text and white-
        space. It can be used to denote the formula in a kind of pseudo
        code or whatever appears approprate.
    :ivar tex_math: this is the TeX representation of TeX formula. A TeX
        formula can be processed by a TeX or a LaTeX processor.
    :ivar generic_math: this rpresents the semantic and mathematical
        descriptions which are processed by a math-processor.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    """

    class Meta:
        name = "ML-FORMULA"

    formula_caption: Optional[Caption] = field(
        default=None,
        metadata={
            "name": "FORMULA-CAPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    l_graphic: List[LGraphic] = field(
        default_factory=list,
        metadata={
            "name": "L-GRAPHIC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    verbatim: Optional[MultiLanguageVerbatim] = field(
        default=None,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tex_math: Optional[MultiLanguagePlainText] = field(
        default=None,
        metadata={
            "name": "TEX-MATH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    generic_math: Optional[MultiLanguagePlainText] = field(
        default=None,
        metadata={
            "name": "GENERIC-MATH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )


@dataclass
class StructuredReq:
    """This represents a structured requirement.

    This is intended for a case where specific requirements for features
    are collected. Note that this can be rendered as a labeled list.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar trace_refs: This assocation represents the ability to trace to
        upstream requirements / constraints. This supports for example
        the bottom up tracing ProjectObjectives &lt;- MainRequirements
        &lt;- Features &lt;- RequirementSpecs &lt;- BSW/AI
    :ivar date: This represents the date when the requirement was
        initiated.
    :ivar issued_by: This represents the person, organization or
        authority which issued the requirement.
    :ivar type_value: This attribute allows to denote the type of
        requirement to denote for example is it an "enhancement", "new
        feature" etc.
    :ivar importance: This allows to represent the importance of the
        requirement.
    :ivar description: Ths represents the general description of the
        requirement.
    :ivar rationale: This represents the rationale of the requirement.
    :ivar applies_to_dependencies:
    :ivar dependencies: This represents an informal specifiaction of
        dependencies. Note that upstream tracing should be formalized in
        the property trace provided by the superclass Traceable.
    :ivar use_case: This describes the relevant use cases. Note that
        formal references to use cases should be done in the trace
        relation.
    :ivar conflicts: This represents an informal specification of
        conflicts.
    :ivar supporting_material: This represents an informal specifiaction
        of the supporting material.
    :ivar remark: This represents an informal remark. Note that this is
        not modeled as annotation, since these remark is still essential
        part of the requirement.
    :ivar tested_item_refs: This assocation represents the ability to
        trace on the same specification level. This supports for example
        the of acceptance tests.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    """

    class Meta:
        name = "STRUCTURED-REQ"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["StructuredReq.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional["AdminData"] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["StructuredReq.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace_refs: Optional["StructuredReq.TraceRefs"] = field(
        default=None,
        metadata={
            "name": "TRACE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    date: Optional[Date] = field(
        default=None,
        metadata={
            "name": "DATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    issued_by: Optional[String] = field(
        default=None,
        metadata={
            "name": "ISSUED-BY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    type_value: Optional[String] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    importance: Optional[String] = field(
        default=None,
        metadata={
            "name": "IMPORTANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    description: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "DESCRIPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rationale: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "RATIONALE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    applies_to_dependencies: Optional[
        "StructuredReq.AppliesToDependencies"
    ] = field(
        default=None,
        metadata={
            "name": "APPLIES-TO-DEPENDENCIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dependencies: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "DEPENDENCIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    use_case: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "USE-CASE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    conflicts: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "CONFLICTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    supporting_material: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "SUPPORTING-MATERIAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    remark: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "REMARK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tested_item_refs: Optional["StructuredReq.TestedItemRefs"] = field(
        default=None,
        metadata={
            "name": "TESTED-ITEM-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TraceRefs:
        trace_ref: List["StructuredReq.TraceRefs.TraceRef"] = field(
            default_factory=list,
            metadata={
                "name": "TRACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TraceRef(Ref):
            dest: Optional[TraceableSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class AppliesToDependencies:
        """
        :ivar applies_to: This attribute represents the platform the
            requirement is assigned to.
        """

        applies_to: List[StandardNameEnum] = field(
            default_factory=list,
            metadata={
                "name": "APPLIES-TO",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TestedItemRefs:
        tested_item_ref: List[
            "StructuredReq.TestedItemRefs.TestedItemRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "TESTED-ITEM-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TestedItemRef(Ref):
            dest: Optional[TraceableSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )


@dataclass
class TraceableText:
    """This meta-class represents the ability to denote a traceable text item such
    as requirements etc.

    The following approach applies:
    * '''shortName''' represents the tag for tracing
    * '''longName''' represents the head line
    * '''category''' represents the kind of the tagged text

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar trace_refs: This assocation represents the ability to trace to
        upstream requirements / constraints. This supports for example
        the bottom up tracing ProjectObjectives &lt;- MainRequirements
        &lt;- Features &lt;- RequirementSpecs &lt;- BSW/AI
    :ivar msr_query_p_2: This represents automatically contributed
        contents provided by an msrquery in the context of
        DocumentationBlock.
    :ivar p: This is one particular paragraph. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was 1.
    :ivar verbatim: This represents one particular verbatim text. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar list_value: This represents numbered or unnumbered list. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar def_list: This represents a definition list in the
        documentation block. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was 1.
    :ivar labeled_list: This represents a labeled list. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar formula: This is a formula in the definition block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar figure: This represents a figure in the documentation block.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        1.
    :ivar note: This represents a note in the text flow. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar trace: This represents traceable text in the documentation
        block. This allows to specify requirements/constraints in any
        documentation block. The kind of the trace is specified in the
        category. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar structured_req: This aggregation supports structured
        requirements embedded in a documentation block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    """

    class Meta:
        name = "TRACEABLE-TEXT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["TraceableText.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional["AdminData"] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional["DocumentationBlock"] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["TraceableText.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace_refs: Optional["TraceableText.TraceRefs"] = field(
        default=None,
        metadata={
            "name": "TRACE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msr_query_p_2: List[MsrQueryP2] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    p: List[MultiLanguageParagraph] = field(
        default_factory=list,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    verbatim: List[MultiLanguageVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    list_value: List["ListType"] = field(
        default_factory=list,
        metadata={
            "name": "LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "DEF-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    labeled_list: List["LabeledList"] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    formula: List[MlFormula] = field(
        default_factory=list,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    figure: List[MlFigure] = field(
        default_factory=list,
        metadata={
            "name": "FIGURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    note: List["Note"] = field(
        default_factory=list,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace: List["TraceableText"] = field(
        default_factory=list,
        metadata={
            "name": "TRACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    structured_req: List[StructuredReq] = field(
        default_factory=list,
        metadata={
            "name": "STRUCTURED-REQ",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TraceRefs:
        trace_ref: List["TraceableText.TraceRefs.TraceRef"] = field(
            default_factory=list,
            metadata={
                "name": "TRACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TraceRef(Ref):
            dest: Optional[TraceableSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )


@dataclass
class Note:
    """This represents a note in a documentation, which may be used to highlight
    specific issues such as hints or caution notes.

    N.B., Documentation notes can be nested recursively, even if this is
    not really intended. In case of nested notes e.g. the note icon of
    inner notes might be omitted while rendering the note.

    :ivar label: This label can be used to superseed the default label
        specified by the noteType attribute. It is in particular useful
        for noteType="other".
    :ivar msr_query_p_2: This represents automatically contributed
        contents provided by an msrquery in the context of
        DocumentationBlock.
    :ivar p: This is one particular paragraph. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was 1.
    :ivar verbatim: This represents one particular verbatim text. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar list_value: This represents numbered or unnumbered list. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar def_list: This represents a definition list in the
        documentation block. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was 1.
    :ivar labeled_list: This represents a labeled list. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar formula: This is a formula in the definition block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar figure: This represents a figure in the documentation block.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        1.
    :ivar note: This represents a note in the text flow. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar trace: This represents traceable text in the documentation
        block. This allows to specify requirements/constraints in any
        documentation block. The kind of the trace is specified in the
        category. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar structured_req: This aggregation supports structured
        requirements embedded in a documentation block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    :ivar note_type: Type of the Note. Default is "HINT"
    """

    class Meta:
        name = "NOTE"

    label: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msr_query_p_2: List[MsrQueryP2] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    p: List[MultiLanguageParagraph] = field(
        default_factory=list,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    verbatim: List[MultiLanguageVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    list_value: List["ListType"] = field(
        default_factory=list,
        metadata={
            "name": "LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "DEF-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    labeled_list: List["LabeledList"] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    formula: List[MlFormula] = field(
        default_factory=list,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    figure: List[MlFigure] = field(
        default_factory=list,
        metadata={
            "name": "FIGURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    note: List["Note"] = field(
        default_factory=list,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace: List[TraceableText] = field(
        default_factory=list,
        metadata={
            "name": "TRACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    structured_req: List[StructuredReq] = field(
        default_factory=list,
        metadata={
            "name": "STRUCTURED-REQ",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )
    note_type: Optional[NoteTypeEnumSimple] = field(
        default=None,
        metadata={
            "name": "NOTE-TYPE",
            "type": "Attribute",
        },
    )


@dataclass
class LabeledItem:
    """
    This represents an item of a labeled list.

    :ivar item_label: This is the label of the item.
    :ivar msr_query_p_2: This represents automatically contributed
        contents provided by an msrquery in the context of
        DocumentationBlock.
    :ivar p: This is one particular paragraph. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was 1.
    :ivar verbatim: This represents one particular verbatim text. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar list_value: This represents numbered or unnumbered list. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar def_list: This represents a definition list in the
        documentation block. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was 1.
    :ivar labeled_list: This represents a labeled list. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar formula: This is a formula in the definition block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar figure: This represents a figure in the documentation block.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        1.
    :ivar note: This represents a note in the text flow. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar trace: This represents traceable text in the documentation
        block. This allows to specify requirements/constraints in any
        documentation block. The kind of the trace is specified in the
        category. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar structured_req: This aggregation supports structured
        requirements embedded in a documentation block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    :ivar help_entry: This specifies an entry point in an online help
        system to be linked with the parent class. The syntax shall be
        defined by the applied help system respectively help system
        generator.
    """

    class Meta:
        name = "LABELED-ITEM"

    item_label: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "ITEM-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msr_query_p_2: List[MsrQueryP2] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    p: List[MultiLanguageParagraph] = field(
        default_factory=list,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    verbatim: List[MultiLanguageVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    list_value: List["ListType"] = field(
        default_factory=list,
        metadata={
            "name": "LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "DEF-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    labeled_list: List["LabeledList"] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    formula: List[MlFormula] = field(
        default_factory=list,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    figure: List[MlFigure] = field(
        default_factory=list,
        metadata={
            "name": "FIGURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace: List[TraceableText] = field(
        default_factory=list,
        metadata={
            "name": "TRACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    structured_req: List[StructuredReq] = field(
        default_factory=list,
        metadata={
            "name": "STRUCTURED-REQ",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )
    help_entry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HELP-ENTRY",
            "type": "Attribute",
        },
    )


@dataclass
class LabeledList:
    """This meta-class represents a labeled list, in which items have a label and a
    content.

    The policy how to render such items is specified in the labeled
    list.

    :ivar indent_sample: This is a sample item. This sample is used by a
        rendering system to measure out the width of indentation. Since
        this depends on the particular fontsize etc. the indentation
        cannot be specified e.g. in mm.
    :ivar labeled_item: This represents one particular item in the
        labeled list. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    """

    class Meta:
        name = "LABELED-LIST"

    indent_sample: Optional[IndentSample] = field(
        default=None,
        metadata={
            "name": "INDENT-SAMPLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    labeled_item: List[LabeledItem] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-ITEM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )


@dataclass
class Item:
    """
    This meta-class represents one particular item in a list.

    :ivar msr_query_p_2: This represents automatically contributed
        contents provided by an msrquery in the context of
        DocumentationBlock.
    :ivar p: This is one particular paragraph. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was 1.
    :ivar verbatim: This represents one particular verbatim text. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar list_value: This represents numbered or unnumbered list. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar def_list: This represents a definition list in the
        documentation block. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was 1.
    :ivar labeled_list: This represents a labeled list. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar formula: This is a formula in the definition block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar figure: This represents a figure in the documentation block.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        1.
    :ivar note: This represents a note in the text flow. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar trace: This represents traceable text in the documentation
        block. This allows to specify requirements/constraints in any
        documentation block. The kind of the trace is specified in the
        category. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar structured_req: This aggregation supports structured
        requirements embedded in a documentation block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    """

    class Meta:
        name = "ITEM"

    msr_query_p_2: List[MsrQueryP2] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    p: List[MultiLanguageParagraph] = field(
        default_factory=list,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    verbatim: List[MultiLanguageVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    list_value: List["ListType"] = field(
        default_factory=list,
        metadata={
            "name": "LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "DEF-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    labeled_list: List[LabeledList] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    formula: List[MlFormula] = field(
        default_factory=list,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    figure: List[MlFigure] = field(
        default_factory=list,
        metadata={
            "name": "FIGURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace: List[TraceableText] = field(
        default_factory=list,
        metadata={
            "name": "TRACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    structured_req: List[StructuredReq] = field(
        default_factory=list,
        metadata={
            "name": "STRUCTURED-REQ",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )


@dataclass
class ListType:
    """This meta-class represents the ability to express a list.

    The kind of list is specified in the attribute.

    :ivar item: this represents a particular list item. Note that this
        is again a documentation block.Therefore lists can be
        arbitrarily nested. It is discouraged to have a very deep
        nesting. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was -1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    :ivar type_value: The type of the list. Default is "UNNUMBER"
    """

    class Meta:
        name = "LIST"

    item: List[Item] = field(
        default_factory=list,
        metadata={
            "name": "ITEM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional["VariationPoint"] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )
    type_value: Optional[ListEnumSimple] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        },
    )


@dataclass
class DocumentationBlock:
    """This class represents a documentation block.

    It is made of basic text structure elements which can be displayed
    in a table cell.

    :ivar msr_query_p_2: This represents automatically contributed
        contents provided by an msrquery in the context of
        DocumentationBlock.
    :ivar p: This is one particular paragraph. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was 1.
    :ivar verbatim: This represents one particular verbatim text. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar list_value: This represents numbered or unnumbered list. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar def_list: This represents a definition list in the
        documentation block. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was 1.
    :ivar labeled_list: This represents a labeled list. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar formula: This is a formula in the definition block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar figure: This represents a figure in the documentation block.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        1.
    :ivar note: This represents a note in the text flow. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar trace: This represents traceable text in the documentation
        block. This allows to specify requirements/constraints in any
        documentation block. The kind of the trace is specified in the
        category. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar structured_req: This aggregation supports structured
        requirements embedded in a documentation block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
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
    """

    class Meta:
        name = "DOCUMENTATION-BLOCK"

    msr_query_p_2: List[MsrQueryP2] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    p: List[MultiLanguageParagraph] = field(
        default_factory=list,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    verbatim: List[MultiLanguageVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "DEF-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    labeled_list: List[LabeledList] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    formula: List[MlFormula] = field(
        default_factory=list,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    figure: List[MlFigure] = field(
        default_factory=list,
        metadata={
            "name": "FIGURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace: List[TraceableText] = field(
        default_factory=list,
        metadata={
            "name": "TRACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    structured_req: List[StructuredReq] = field(
        default_factory=list,
        metadata={
            "name": "STRUCTURED-REQ",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )


@dataclass
class BlueprintGenerator:
    """
    This class express the Extended Language to generate blueprint derivates in
    complex descriptions.

    :ivar introduction: This represents a description that documents how
        the blueprint generator shall be resolved when deriving objects
        from blueprints.
    :ivar expression: This represents a formal term in the expression
        based on the extented language.
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
    """

    class Meta:
        name = "BLUEPRINT-GENERATOR"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    expression: Optional[VerbatimString] = field(
        default=None,
        metadata={
            "name": "EXPRESSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )


@dataclass
class VariationPoint:
    """This meta-class represents the ability to express a "structural variation
    point".

    The container of the variation point is part of the selected variant
    if swSyscond evaluates to true and each postBuildVariantCriterion is
    fulfilled.

    :ivar short_label: This provides a name to the particular variation
        point to support the RTE generator. It is necessary for
        supporting splitable aggregations and if binding time is later
        than codeGenerationTime, as well as some RTE conditions. It
        needs to be unique with in the enclosing Identifiables with the
        same ShortName.
    :ivar desc: This allows to describe shortly the purpose of the
        variation point.
    :ivar blueprint_condition: This represents a description that
        documents how the variation point shall be resolved when
        deriving objects from the blueprint. Note that variationPoints
        are not allowed within a blueprintCondition.
    :ivar formal_blueprint_condition: This denotes a formal
        blueprintCondition. This shall be not in contradiction with
        blueprintCondition or formalBlueprintGenerator. It is
        recommended only to use one of the two.
    :ivar formal_blueprint_generator: This represents a description that
        documents how the variation point shall be resolved when
        deriving objects from the blueprint by using ARMQL. Note that
        variationPoints are not allowed within a
        formalBlueprintGenerator.
    :ivar sw_syscond: This condition acts as Binding Function for the
        VariationPoint. Note that the mulitplicity is 0..1 in order to
        support pure postBuild variants.
    :ivar post_build_variant_conditions: This is the set of post build
        variant conditions which all  shall be fulfilled in order to
        (postbuild) bind the variation point.
    :ivar sdg: An optional special data group is attached to every
        variation point. These data can be used by external software
        systems to attach application specific data. For example, a
        variant management system might add an identifier, an URL or a
        specific classifier.
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
    """

    class Meta:
        name = "VARIATION-POINT"

    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blueprint_condition: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-CONDITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    formal_blueprint_condition: Optional[BlueprintFormula] = field(
        default=None,
        metadata={
            "name": "FORMAL-BLUEPRINT-CONDITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    formal_blueprint_generator: Optional[BlueprintGenerator] = field(
        default=None,
        metadata={
            "name": "FORMAL-BLUEPRINT-GENERATOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_syscond: Optional[ConditionByFormula] = field(
        default=None,
        metadata={
            "name": "SW-SYSCOND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    post_build_variant_conditions: Optional[
        "VariationPoint.PostBuildVariantConditions"
    ] = field(
        default=None,
        metadata={
            "name": "POST-BUILD-VARIANT-CONDITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdg: Optional["Sdg"] = field(
        default=None,
        metadata={
            "name": "SDG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class PostBuildVariantConditions:
        post_build_variant_condition: List[PostBuildVariantCondition] = field(
            default_factory=list,
            metadata={
                "name": "POST-BUILD-VARIANT-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )


@dataclass
class ReferrableRefConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar referrable_ref:
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    """

    class Meta:
        name = "REFERRABLE-REF-CONDITIONAL"

    referrable_ref: Optional["ReferrableRefConditional.ReferrableRef"] = field(
        default=None,
        metadata={
            "name": "REFERRABLE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class ReferrableRef(Ref):
        dest: Optional[ReferrableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class Sdg:
    """Sdg (SpecialDataGroup) is a generic model which can be used to keep
    arbitrary information which is not explicitly modeled in the meta-model.

    Sdg can have various contents as defined by sdgContentsType. Special
    Data should only be used moderately since all elements should be
    defined in the meta-model. Thereby SDG should be considered as a
    temporary solution when no explicit model is available. If an
    sdgCaption is available, it is possible to establish a reference to
    the sdg structure.

    :ivar sdg_caption: This aggregation allows to assign the properties
        of Identifiable to the sdg. By this, a shortName etc. can be
        assigned to the Sdg.
    :ivar sdg_caption_ref: This association allows to reuse an already
        existing caption.
    :ivar sdx_ref: Reference to any identifiable element. This allows to
        use Sdg even to establish arbitrary relationships.
    :ivar sdxf: Additional reference with variant support. This property
        was modified due to atpVariation (DirectedAssociationPattern).
    :ivar sd: This is one particular special data element.
    :ivar sdg: This aggregation allows to express nested special data
        groups. By this, any structure can be represented in
        SpeicalData. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar sdf: This is one particular special data element.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar gid: This attributes specifies an identifier. Gid comes from
        the SGML/XML-Term "Generic Identifier" which is the element name
        in XML. The role of this attribute is the same as the name of an
        XML - element.
    """

    class Meta:
        name = "SDG"

    sdg_caption: Optional[SdgCaption] = field(
        default=None,
        metadata={
            "name": "SDG-CAPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdg_caption_ref: Optional["Sdg.SdgCaptionRef"] = field(
        default=None,
        metadata={
            "name": "SDG-CAPTION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdx_ref: List["Sdg.SdxRef"] = field(
        default_factory=list,
        metadata={
            "name": "SDX-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdxf: List[ReferrableRefConditional] = field(
        default_factory=list,
        metadata={
            "name": "SDXF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd: List[Sd] = field(
        default_factory=list,
        metadata={
            "name": "SD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdg: List["Sdg"] = field(
        default_factory=list,
        metadata={
            "name": "SDG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdf: List[Sdf] = field(
        default_factory=list,
        metadata={
            "name": "SDF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    gid: Optional[str] = field(
        default=None,
        metadata={
            "name": "GID",
            "type": "Attribute",
        },
    )

    @dataclass
    class SdgCaptionRef(Ref):
        dest: Optional[SdgCaptionSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SdxRef(Ref):
        dest: Optional[ReferrableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class AdminData:
    """AdminData represents the ability to express administrative information for
    an element.

    This administration information is to be treated as meta-data such as revision id or state of the file. There are basically four kinds of meta-data
    * The language and/or used languages.
    * Revision information covering e.g. revision number, state, release date, changes. Note that this information can be given in general as well as related to a particular company.
    * Document meta-data specific for a company

    :ivar language: This attribute  specifies the master language of the
        document or the document fragment. The master language is the
        one in which the document is maintained and from which the other
        languages are derived from. In particular in case of
        inconsistencies, the information in the master language is
        priority.
    :ivar used_languages: This property specifies the languages which
        are provided in the document. Therefore it should only be
        specified in the top level admin data. For each language
        provided in the document there is one entry in
        MultilanguagePlainText. The content of each entry can be used
        for illustration of the language. The used language itself
        depends on the language attribute in the entry.
    :ivar doc_revisions: This allows to denote information about the
        current revision of the object. Note that information about
        previous revisions can also be logged here. The entries shall be
        sorted descendant by date in order to reflect the history.
        Therefore the most recent entry representing the current version
        is denoted first.
    :ivar sdgs: This property allows to keep special data which is not
        represented by the standard model. It can be utilized to keep
        e.g. tool specific data.
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
    """

    class Meta:
        name = "ADMIN-DATA"

    language: Optional[LEnum] = field(
        default=None,
        metadata={
            "name": "LANGUAGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    used_languages: Optional[MultiLanguagePlainText] = field(
        default=None,
        metadata={
            "name": "USED-LANGUAGES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    doc_revisions: Optional["AdminData.DocRevisions"] = field(
        default=None,
        metadata={
            "name": "DOC-REVISIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdgs: Optional["AdminData.Sdgs"] = field(
        default=None,
        metadata={
            "name": "SDGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class DocRevisions:
        doc_revision: List[DocRevision] = field(
            default_factory=list,
            metadata={
                "name": "DOC-REVISION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Sdgs:
        sdg: List[Sdg] = field(
            default_factory=list,
            metadata={
                "name": "SDG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
