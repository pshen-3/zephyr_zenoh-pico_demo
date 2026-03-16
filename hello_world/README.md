# Prepare
- Install Zephyr following the official guide.
- Copy `zephyr/samples/hello_world` into this folder.

# Build
```sh
cd hello_world
west build -p always -b nucleo_h563zi
```

# Flash
```sh
west flash -r jlink
```

Note: I am using a custom STM32H563ZI board (not the official `nucleo_h563zi`), so I have to adjust the devicetree to match my hardware. I also use J-Link for flashing.

# RTT Output
This sample output to SEGGER RTT console (instead of a UART serial console).

Example:
```text
*** Booting Zephyr OS build v4.3.0-6868-g17da549ce2ac ***
Hello World! nucleo_h563zi/stm32h563xx
```

# Integrate zenoh-pico
- As a Zephyr module
  - Add `zephyr/submanifests/zenoh-pico.yaml`:
    ```yaml
    manifest:
      projects:
        - name: zenoh-pico
          url: https://github.com/eclipse-zenoh/zenoh-pico
          revision: main
          path: modules/lib/zenoh-pico
    ```
  - Add to `prj.conf`:
    ```conf
    CONFIG_ZENOH_PICO=y
    ```
- As a standalone library
  - TODO
