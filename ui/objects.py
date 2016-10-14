#!/usr/bin/python

import time
import datetime

class Wheel():
    ticks = 0
    ride_start_time = time.time()
    last_tick_time = time.time()
    this_tick_time = time.time()
    circumference = .001366 # 700pi converted to miles

    def increment(self):
        self.ticks += 1
        self.last_tick_time = self.this_tick_time
        self.this_tick_time = time.time()

    def speed(self):
        if self.ticks == 0:
            return 0.0
        return self.circumference / \
            (self.this_tick_time - self.last_tick_time) * 3600

    def total_distance(self):
        return self.ticks * self.circumference

    def total_ticks(self):
        return self.ticks

    def total_time(self):
        return str(datetime.timedelta(seconds = int(time.time() - self.ride_start_time)))

class Cadence():
    ticks = 0
    last_tick_time = time.time()
    this_tick_time = time.time()

    def increment(self):
        self.ticks += 1
        self.last_tick_time = self.this_tick_time
        self.this_tick_time = time.time()

    def cadence(self):
        if self.ticks == 0:
            return 0
        return 60 / (self.this_tick_time - self.last_tick_time)

    def total_ticks(self):
        return self.ticks



