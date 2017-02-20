# Install script for directory: /home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/python

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/dsrcmod" TYPE FILE FILES
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/python/__init__.py"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/python/nrzi_to_nrz_bb.py"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/python/nrz_to_nrzi_bb.py"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/python/pulse_shaper_bs.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/dsrcmod" TYPE FILE FILES
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python/__init__.pyc"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python/nrzi_to_nrz_bb.pyc"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python/nrz_to_nrzi_bb.pyc"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python/pulse_shaper_bs.pyc"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python/__init__.pyo"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python/nrzi_to_nrz_bb.pyo"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python/nrz_to_nrzi_bb.pyo"
    "/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python/pulse_shaper_bs.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

