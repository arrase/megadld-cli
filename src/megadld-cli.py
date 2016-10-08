#!/usr/bin/python

import argparse
import json
import socket

__application__ = "megadld-cli"
__version__ = "0.1.0"
__release__ = __application__ + '/' + __version__
__author__ = "Juan Ezquerro LLanes"


class MegadldCli:
    _host = None
    _port = None
    _url = None
    _sock = None

    def __init__(self, url, host, port=8000):
        self._host = host
        self._port = port
        self._url = url

    def run(self):
        try:
            # Create a socket (SOCK_STREAM means a TCP socket)
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.connect((self._host, self._port))
            # Connect to server and send data
            self._sock.sendall('{"url":"' + self._url + '"}' + "\n")
            # Receive data from the server and shut down
            received = json.loads(self._sock.recv(1024))
            if received.has_key('status') and received["status"] == "true":
                print "The URL has been received by the server and the download should start now\n"
            else:
                print "Something went wrong.....\n"
        except socket.error:
            print "There was an error when trying to connect to the server\n"
        finally:
            self._sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', '-i', required=True, help='Server IP')
    parser.add_argument('--url', required=True, help='Mega url')
    parser.add_argument('--port', '-p', default=8000, help='Server port (Default=8000)')
    args = parser.parse_args()

    cli = MegadldCli(args.url, args.ip, args.port)
    cli.run()
