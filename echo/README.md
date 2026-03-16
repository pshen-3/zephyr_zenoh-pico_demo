# Prepare
- Install Zephyr following the official guide.
- Copy `zephyr/samples/net/sockets/echo` into this folder.

# Build
```sh
cd echo
west build -p always -b nucleo_h563zi
```

# Flash
```sh
west flash -r jlink
```

Note: add mac network interface to devicetree

# RTT Output, Echo Server
This sample output to SEGGER RTT console (instead of a UART serial console).

Example:
```text
*** Booting Zephyr OS build v4.3.0-6868-g17da549ce2ac ***
IPV6_V6ONLY option is on, turning it off.
Sharing same socket between IPv6 and IPv4
Single-threaded TCP echo server waits for a connection on port 4242...
Connection #0 from 3Ã
Connection from 3Ã closed
```
# Echo Client
```sh
python tcp_client.py 192.0.2.1 4242
hi there
hi there
hi echo server 
hi echo server
^C
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
