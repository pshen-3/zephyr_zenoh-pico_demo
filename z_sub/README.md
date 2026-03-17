# Prepare
- Install Zephyr following the official guide.
- Copy `zenoh-pico/examples/zephyr/z_sub.c` into this folder.

# Build
```sh
cd z_sub
west build -p always -b nucleo_h563zi
```

# Flash
```sh
west flash -r jlink
```

Note: add zenoh-pico config to `prj.conf`:
```conf
CONFIG_ZENOH_PICO=y
```

# RTT Output
This sample output to SEGGER RTT console (instead of a UART serial console).

Example:
```text
*** Booting Zephyr OS build v4.3.0-6868-g17da549ce2ac ***
Opening Zenoh Session...OK
Declaring Subscriber on 'demo/example/**'...OK!
 >> [Subscriber handler] Received ('demo/example/zenoh-pico-pub': '[   0] Pub from Pico!')
 >> [Subscriber handler] Received ('demo/example/zenoh-pico-pub': '[   1] Pub from Pico!')
 >> [Subscriber handler] Received ('demo/example/zenoh-pico-pub': '[   2] Pub from Pico!')
 >> [Subscriber handler] Received ('demo/example/zenoh-pico-pub': '[   3] Pub from Pico!')
 >> [Subscriber handler] Received ('demo/example/zenoh-pico-pub': '[   4] Pub from Pico!')
 >> [Subscriber handler] Received ('demo/example/zenoh-pico-pub': '[   5] Pub from Pico!')
 >> [Subscriber handler] Received ('demo/example/zenoh-pico-pub': '[   6] Pub from Pico!')
 ...
```
# run zenoh-pico/build/examples/z_pub on host
```sh
% ./z_pub
Opening session...
Declaring publisher for 'demo/example/zenoh-pico-pub'...
Press CTRL-C to quit...
Putting Data ('demo/example/zenoh-pico-pub': '[   0] Pub from Pico!')...
Putting Data ('demo/example/zenoh-pico-pub': '[   1] Pub from Pico!')...
Putting Data ('demo/example/zenoh-pico-pub': '[   2] Pub from Pico!')...
Putting Data ('demo/example/zenoh-pico-pub': '[   3] Pub from Pico!')...
Putting Data ('demo/example/zenoh-pico-pub': '[   4] Pub from Pico!')...
Putting Data ('demo/example/zenoh-pico-pub': '[   5] Pub from Pico!')...
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
