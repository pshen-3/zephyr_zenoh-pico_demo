#!/usr/bin/env python3
import argparse
import socket
import sys
import threading


def _recv_loop(sock: socket.socket) -> None:
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                break
            sys.stdout.write(data.decode(errors="replace"))
            sys.stdout.flush()
    except OSError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Interactive TCP client")
    parser.add_argument("host", help="Server host/IP")
    parser.add_argument("port", type=int, help="Server TCP port")
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Encoding for stdin->socket (default: utf-8)",
    )
    parser.add_argument(
        "--no-newline",
        action="store_true",
        help="Do not append newline when sending each input line",
    )
    args = parser.parse_args()

    with socket.create_connection((args.host, args.port)) as sock:
        recv_thread = threading.Thread(target=_recv_loop, args=(sock,), daemon=True)
        recv_thread.start()

        try:
            for line in sys.stdin:
                payload = line if args.no_newline else (line if line.endswith("\n") else line + "\n")
                sock.sendall(payload.encode(args.encoding, errors="replace"))
        except KeyboardInterrupt:
            pass
        except BrokenPipeError:
            return 1
        finally:
            try:
                sock.shutdown(socket.SHUT_WR)
            except OSError:
                pass

        recv_thread.join(timeout=1.0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
