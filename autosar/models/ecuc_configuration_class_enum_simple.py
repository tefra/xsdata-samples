from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EcucConfigurationClassEnumSimple(Enum):
    """
    :cvar LINK: Link Time: parts of configuration are delivered from
        another object code file
    :cvar POST_BUILD: PostBuildTime: after compilation a configuration
        parameter can be changed.
    :cvar PRE_COMPILE: PreCompile Time: after compilation a
        configuration parameter can not be changed any more.
    :cvar PUBLISHED_INFORMATION: PublishedInformation is used to specify
        the fact that certain information is fixed even before the pre-
        compile stage.
    """

    LINK = "LINK"
    POST_BUILD = "POST-BUILD"
    PRE_COMPILE = "PRE-COMPILE"
    PUBLISHED_INFORMATION = "PUBLISHED-INFORMATION"
