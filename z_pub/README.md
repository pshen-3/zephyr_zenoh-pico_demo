# z_pub (Zephyr + zenoh-pico)

Zenoh-pico publisher example running on Zephyr. It publishes to the keyexpr `demo/example/zenoh-pico-pub`.

## Prerequisites
- Install and initialize Zephyr using the official documentation
- This sample is based on `zenoh-pico/examples/zephyr/z_pub.c`

## Build
```sh
cd z_pub
west build -p always -b nucleo_h563zi
```

## Flash
```sh
west flash -r jlink
```

## Configuration
Enable zenoh-pico in `prj.conf`:

```conf
CONFIG_ZENOH_PICO=y
```

In client mode, if `LOCATOR` is empty, the app will try multicast scouting on `udp/224.0.0.224:7446`.
In some network environments multicast scouting may not work; use a direct locator instead, for example:

```c
#define LOCATOR "tcp/192.0.2.2:7447"
```

## Host-side verification
Start the router:

```sh
./zenohd
```

In another terminal, start the subscriber (subscribing to `demo/example/**`):

```sh
./z_sub
```

Example output:

```text
Opening session...
Declaring Subscriber on 'demo/example/**'...
Press CTRL-C to quit...
>> [Subscriber] Received ('demo/example/zenoh-pico-pub': '[   0] nucleo_h563zi/stm32h563xx Pub from Zenoh-Pico!')
>> [Subscriber] Received ('demo/example/zenoh-pico-pub': '[   1] nucleo_h563zi/stm32h563xx Pub from Zenoh-Pico!')
...
```

## RTT output
This sample uses SEGGER RTT output (instead of a UART serial console).

Example:

```text
*** Booting Zephyr OS build v4.3.0-6868-g17da549ce2ac ***
Opening Zenoh Session...OK
Declaring publisher for 'demo/example/zenoh-pico-pub'...OK
Putting Data ('demo/example/zenoh-pico-pub': '[   0] nucleo_h563zi/stm32h563xx Pub from Zenoh-Pico!')...
Putting Data ('demo/example/zenoh-pico-pub': '[   1] nucleo_h563zi/stm32h563xx Pub from Zenoh-Pico!')...
...
```

## Integrating zenoh-pico (as a Zephyr module)
Add `zephyr/submanifests/zenoh-pico.yaml`:

```yaml
manifest:
  projects:
    - name: zenoh-pico
      url: https://github.com/eclipse-zenoh/zenoh-pico
      revision: main
      path: modules/lib/zenoh-pico
```

Enable it in your app `prj.conf`:

```conf
CONFIG_ZENOH_PICO=y
```
