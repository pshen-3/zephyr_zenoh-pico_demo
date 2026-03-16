# Prepare
- Install Zephyr following the official guide.
- Copy `zephyr/samples/blinky` into this folder.

# Build
```sh
cd blinky
west build -p always -b nucleo_h563zi
```

# Flash
```sh
west flash -r jlink
```

Note: besides rtt console for hello_world, here also add leds to devicetree and set clock for leds toggle every 1 second.

# RTT Output
This sample output to SEGGER RTT console (instead of a UART serial console).

Example:
```text
*** Booting Zephyr OS build v4.3.0-6868-g17da549ce2ac ***
LED state: OFF
LED state: ON
LED state: OFF
LED state: ON
...
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
