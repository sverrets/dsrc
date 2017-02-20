INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DSRCMOD dsrcmod)

FIND_PATH(
    DSRCMOD_INCLUDE_DIRS
    NAMES dsrcmod/api.h
    HINTS $ENV{DSRCMOD_DIR}/include
        ${PC_DSRCMOD_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DSRCMOD_LIBRARIES
    NAMES gnuradio-dsrcmod
    HINTS $ENV{DSRCMOD_DIR}/lib
        ${PC_DSRCMOD_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DSRCMOD DEFAULT_MSG DSRCMOD_LIBRARIES DSRCMOD_INCLUDE_DIRS)
MARK_AS_ADVANCED(DSRCMOD_LIBRARIES DSRCMOD_INCLUDE_DIRS)

