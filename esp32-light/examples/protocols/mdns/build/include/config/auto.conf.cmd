deps_config := \
	/home/ark/Desktop/esp/esp-idf/components/app_trace/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/aws_iot/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/bt/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/driver/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/esp32/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/esp_adc_cal/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/esp_http_client/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/ethernet/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/fatfs/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/freemodbus/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/freertos/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/heap/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/http_server/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/libsodium/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/log/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/lwip/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/mbedtls/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/mdns/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/mqtt/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/nvs_flash/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/openssl/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/pthread/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/spi_flash/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/spiffs/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/tcpip_adapter/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/vfs/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/wear_levelling/Kconfig \
	/home/ark/Desktop/esp/esp-idf/components/bootloader/Kconfig.projbuild \
	/home/ark/Desktop/esp/esp-idf/components/esptool_py/Kconfig.projbuild \
	/home/ark/Desktop/IoT-Security/esp32-light/examples/protocols/mdns/main/Kconfig.projbuild \
	/home/ark/Desktop/esp/esp-idf/components/partition_table/Kconfig.projbuild \
	/home/ark/Desktop/esp/esp-idf/Kconfig

include/config/auto.conf: \
	$(deps_config)

ifneq "$(IDF_CMAKE)" "n"
include/config/auto.conf: FORCE
endif

$(deps_config): ;
