# -*- coding: utf-8 -*-
# Copyright (c) 2022 sillo01
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Zero2W
(see http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_Zero_2W#40_Pin_Interface_pin_description)
Usage:
.. code:: python
   import orangepi.zero2w
   from OPi import GPIO
   GPIO.setmode(orangepi.zero2w.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi Zero 2W physical board pin to GPIO pin
BOARD = {
    3:    264,   # PI8/TWI1-SDA
    5:    263, # PI7/TWI1-SCL
    7:    269, # PI13/PWM3/UART4_TX
    8:    224, # PH0/UART0_TX
    10:   225, # PH1/UART0_RX
    11:   226, # PH2/UART5_TX
    12:   257, # PI1
    13:   227, # PH3/UART5_RX
    15:   261, # PI5/TWI0_SCL/UART2_TX
    16:   270, # PI14/PWM4/UART4_RX
    18:   228, # PH4
    19:   231, # PH7/SPI1_MOSI
    21:   232, # PH8/SPI1_MISO
    22:   262, # PI6/TWI0_SDA/UART2_RX
    23:   230, # PH6/SPI1_CLK
    24:   229, # PH5/SPI1_CS0
    26:   233, # PH9/SPI1_CS1
    27:   266, # PI10/TWI2-SDA/UART3_RX
    28:   265, # PI9/TWI2-SCL/UART3_TX
    29:   256, # PI0
    31:   271, # PI15
    32:   267, # PI11/PWM1
    33:   268, # PI12/PWM2
    35:   258, # PI2
    36:    76, # PC12
    37:   272, # PI16
    38:   260, # PI4
    40:   259, # PI3
}

# BCM mapping not identified yet, keeping it for compatibility
BCM = BOARD
