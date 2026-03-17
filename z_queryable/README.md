# z_queryable (Zephyr + zenoh-pico)

Zenoh-pico queryable example running on Zephyr. It declares a queryable on `demo/example/zenoh-pico-queryable`.

## Prerequisites
- Install and initialize Zephyr using the official documentation
- This sample is based on `zenoh-pico/examples/zephyr/z_queryable.c`

## Build
```sh
cd z_queryable
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
cat demo_example.json5
{
  plugins: {
    rest: {
      http_port: 8000
    },
    storage_manager: {
      storages: {
        demo: {
          key_expr: "demo/example/**",
          volume: {
            id: "memory"
          }
        }
      }
    }
  }
}

./zenohd -c demo_example.json5
```

In another terminal, start `z_get` to send queries:

```sh
./z_get
```

## RTT output
This sample uses SEGGER RTT output (instead of a UART serial console).

Example:
```text
*** Booting Zephyr OS build v4.3.0-6868-g17da549ce2ac ***
Opening Zenoh Session...OK
Declaring Queryable on demo/example/zenoh-pico-queryable...OK
Zenoh setup finished!
 >> [Queryable handler] Received Query 'demo/example/**'
```

Example output from `z_get`:

```text
Opening session...
Sending Query 'demo/example/**'...
>> Received PUT ('demo/example/**': 'nucleo_h563zi/stm32h563xx Queryable from Zenoh-Pico!')
>> Received query final notification
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
