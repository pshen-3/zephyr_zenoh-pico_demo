# z_get (Zephyr + zenoh-pico)

Zenoh-pico get/query example running on Zephyr. It sends periodic queries for `demo/example/**`.

## Prerequisites
- Install and initialize Zephyr using the official documentation
- This sample is based on `zenoh-pico/examples/zephyr/z_get.c`

## Build
```sh
cd z_get
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

In another terminal, start a publisher:

```sh
./z_pub
Opening session...
Declaring publisher for 'demo/example/zenoh-pico-pub'...
Press CTRL-C to quit...
Putting Data ('demo/example/zenoh-pico-pub': '[   0] Pub from Pico!')...
Putting Data ('demo/example/zenoh-pico-pub': '[   1] Pub from Pico!')...
Putting Data ('demo/example/zenoh-pico-pub': '[   2] Pub from Pico!')...
...
```

## RTT output
This sample uses SEGGER RTT output (instead of a UART serial console).

Example:
```text
*** Booting Zephyr OS build v4.3.0-6868-g17da549ce2ac ***
Opening Zenoh Session...OK
Sending Query 'demo/example/**'...
 >> Received ('demo/example/zenoh-pico-pub': '[ 329] Pub from Pico!')
 >> Received query final notification
Sending Query 'demo/example/**'...
 >> Received ('demo/example/zenoh-pico-pub': '[ 334] Pub from Pico!')
 >> Received query final notification
Sending Query 'demo/example/**'...
 >> Received ('demo/example/zenoh-pico-pub': '[ 339] Pub from Pico!')
 >> Received query final notification
Sending Query 'demo/example/**'...
 >> Received ('demo/example/zenoh-pico-pub': '[ 344] Pub from Pico!')
 >> Received query final notification
Sending Query 'demo/example/**'...
 >> Received ('demo/example/zenoh-pico-pub': '[ 349] Pub from Pico!')
 >> Received query final notification
Sending Query 'demo/example/**'...
 >> Received ('demo/example/zenoh-pico-pub': '[ 354] Pub from Pico!')
 >> Received query final notification
Sending Query 'demo/example/**'...
 >> Received query final notification
Unable to send query.
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
