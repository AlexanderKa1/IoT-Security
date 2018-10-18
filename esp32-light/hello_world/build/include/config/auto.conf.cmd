deps_config := \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/app_trace/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/aws_iot/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/bt/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/driver/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/esp32/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/esp_adc_cal/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/esp_http_client/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/ethernet/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/fatfs/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/freertos/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/heap/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/http_server/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/libsodium/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/log/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/lwip/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/mbedtls/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/mdns/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/mqtt/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/nvs_flash/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/openssl/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/pthread/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/spi_flash/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/spiffs/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/tcpip_adapter/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/vfs/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/wear_levelling/Kconfig \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/bootloader/Kconfig.projbuild \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/esptool_py/Kconfig.projbuild \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/components/partition_table/Kconfig.projbuild \
	/home/ark/Desktop/IoT-Security/esp32-light/esp-idf/Kconfig

include/config/auto.conf: \
	$(deps_config)

ifneq "$(IDF_CMAKE)" "n"
include/config/auto.conf: FORCE
endif

$(deps_config): ;
