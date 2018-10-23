#include <string.h>
#include <sys/param.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/event_groups.h"
#include "esp_system.h"
#include "esp_wifi.h"
#include "esp_event_loop.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "driver/uart.h"

#include "network_mo.h"
#include "relay_mo.h"
#include "tty_mo.h"
#include "main.h"

static const char *TAG = "example";

RELAY_MO relay_mo;

void on()
{
    relay_mo.relay[0].on();
    relay_mo.relay[1].on();
}

void off()
{
    relay_mo.relay[0].off();
    relay_mo.relay[1].off();
}

void data_handler(char* data,int len)
{
    DATAGRAM d = *(DATAGRAM*)data;
    switch(d.what)
    {
    case 1001:
        on();
        break;
    case 1002:
        off();
        break;
    }
}

void app_main()
{
    ESP_ERROR_CHECK( nvs_flash_init() );
    tty_init();
    relay_mo = relay_init();
    network_init();

    ESP_LOGI(TAG, "Inited");    
}
