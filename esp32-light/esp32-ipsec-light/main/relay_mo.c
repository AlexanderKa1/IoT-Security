#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"
#include "driver/gpio.h"
#include "relay_mo.h"

#define GPIO_OUTPUT_IO_0    18
#define GPIO_OUTPUT_IO_1    19
#define GPIO_OUTPUT_PIN_SEL  ((1ULL<<GPIO_OUTPUT_IO_0) | (1ULL<<GPIO_OUTPUT_IO_1))


void relay0_on()
{
    gpio_set_level(GPIO_OUTPUT_IO_0, 0);
}
void relay0_off()
{
    gpio_set_level(GPIO_OUTPUT_IO_0, 1);
}

void relay1_on()
{
    gpio_set_level(GPIO_OUTPUT_IO_1, 0);
}
void relay1_off()
{
    gpio_set_level(GPIO_OUTPUT_IO_1, 1);
}

RELAY_MO relay_init()
{
    gpio_config_t io_conf;
    RELAY_MO relay_mo;
    //disable interrupt
    io_conf.intr_type = GPIO_PIN_INTR_DISABLE;
    //set as output mode
    io_conf.mode = GPIO_MODE_OUTPUT;
    //bit mask of the pins that you want to set,e.g.GPIO18/19
    io_conf.pin_bit_mask = GPIO_OUTPUT_PIN_SEL;
    //disable pull-down mode
    io_conf.pull_down_en = 0;
    //disable pull-up mode
    io_conf.pull_up_en = 0;
    //configure GPIO with the given settings
    gpio_set_level(GPIO_OUTPUT_IO_0, 1);
    gpio_set_level(GPIO_OUTPUT_IO_1, 1);
    gpio_config(&io_conf);
    
    relay_mo.relay[0].off = relay0_off;
    relay_mo.relay[0].on = relay0_on;
    
    relay_mo.relay[1].off = relay1_off;
    relay_mo.relay[1].on = relay1_on;

    return relay_mo;
}
