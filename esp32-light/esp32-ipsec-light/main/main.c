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

void app_main()
{
    ESP_ERROR_CHECK( nvs_flash_init() );
    tty_init();
    relay_mo = relay_init();
    
    ESP_LOGI(TAG, "CreateTasks");
    
}
