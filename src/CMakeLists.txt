#[[

This file sets all of the libraries and compiler settings for the project.

// to add for ubxlib
// application name: ionosphere-gonzales??

include(DIRECTORY_WHERE_YOU_HAVE_PUT_UBXLIB/port/platform/linux/linux.cmake)

target_link_libraries(YOUR_APPLICATION_NAME ubxlib ${UBXLIB_REQUIRED_LINK_LIBS})

target_include_directories(YOUR_APPLICATION_NAME PUBLIC ${UBXLIB_INC} ${UBXLIB_PUBLIC_INC_PORT})

]]


