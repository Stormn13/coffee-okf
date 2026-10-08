---
type: equipment
title: Smart Fridge Temperature Sensor
description: Maintenance logs and specs for the ESP32 milk fridge monitor.
tags: [hardware, maintenance]
---

# Fridge Sensor (ESP32)

We use a custom ESP32 microcontroller with a DS18B20 temperature sensor to monitor the milk fridge. 

If the temperature reads above 40°F (4°C), the sensor triggers an alert. 

**Troubleshooting:**
If the OLED display is blank, check the power flow diagram or reboot the microcontroller. If milk spoils due to a sensor failure, baristas must process refunds using the [Refund Policy](../policies/refund-policy.md).