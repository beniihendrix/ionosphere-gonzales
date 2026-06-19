# Recording Logistics

This document address problem we may face when recording and
offers solutions.

## Data Capacity

The UART transmissions recovered by the Pi definitely can't stay
very long on the Pi itself. With a baud rate of `115200`, we're
recording at a maximum rate of 11.5kB/s. Within one hour, we've
recorded 40.5MB. That's about a good stopping point to move on to
the next file. However, the 11.5kB/s is a worst case scenario.

We've decided on recording to record to files in 1.5 hour intervals.
This is just a start, and we'll find a realistic number once we record
data.

### Data cap updates

Knowing that we will be recording using ubx binary data,
we can do the math for how much data is being stored over time.

The messages we'll need for our data collection are `UBX-RXM-RAWX` and
`UBX-RXM-SFRBX`. These messages each take up $2,064$ and $~22$ bytes 
respectively. Both combined generate about $7.4$ MB an hour, or $1$ GB
a week. This gives a lot of room for storing files, but we should
still be conscious about how often we save in the case of an
unexpected reboot.

## Power

Because we're creating a transportable gnss receiver, it would
be nice to have a battery-powered design, but it introduces
problems like overheating and unreliable power delivery
when in a case for a long period of time.

A long cable running from a house is a reliable source for both the
Pi and SimpleRTK2B and opens the door for a separate fan for cooling.

## What Needs to be Designed

- Weatherproof box with reflective wrap

- Fan for cooling

- Cable routing for power and gnss antenna
