#!/usr/bin/python
# -*- coding:utf-8 -*-

from waveshare_epd import epd7in5_V2 as epd_driver

epd = epd_driver.EPD()
epd.init()
epd.Clear()
epd.sleep()  
epd_driver.epdconfig.module_exit()

exit()
