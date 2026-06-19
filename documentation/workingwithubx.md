# Working with UBX U-Blox files

This document talks about the differences between reading NMEA messages
vs. UBX binary while receiving GNSS data.

## Issues with NMEA data

- Data needs to be parsed

- Can take up a lot of memory on smaller microcontrollers,
requiring a separate processor to interpret the data (this is because NMEA data is text)

We need a low memory solution to store the most data possible for our
STEC and VTEC calculations.

## UBX binary protocol

Information is found in the refernces

Thankfully `ubxlib` is able to take care of the recording logic for us.

## Why use `ubxlib`

// add later

### Linking `ubxlib` to project using CMake


```
include(DIRECTORY_WHERE_YOU_HAVE_PUT_UBXLIB/port/platform/linux/linux.cmake)
target_link_libraries(YOUR_APPLICATION_NAME ubxlib ${UBXLIB_REQUIRED_LINK_LIBS})
target_include_directories(YOUR_APPLICATION_NAME PUBLIC ${UBXLIB_INC} ${UBXLIB_PUBLIC_INC_PORT})
```

# References

- [10Hz U-blox binary GPS data in 66 lines of code (arduino)](https://www.youtube.com/watch?v=TwhCX0c8Xe0&t=1s)

- [ZED-F9P Interface Description (ubx binary protocol)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/6/ZED-F9P_UBX_NMEA_and_RTCM_protocols.pdf)

- [ubxlib GitHub](https://github.com/u-blox/ubxlib)

- [ubxlib Linux Integration](https://github.com/u-blox/ubxlib/tree/master/port/platform/linux)

**Key Takeaways** - We should be interesting in programming our
data acquisition in C++ to limit overhead and use popular libraries
like `ubxlib`.
