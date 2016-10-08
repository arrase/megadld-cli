# MEGADLD-CLI
megadld-cli is a client written in Python for [megadld daemon](https://github.com/arrase/megadld)

### Install:
```
sudo cp src/megadld-cli.py /usr/local/bin/megadld-cli
```

### Usage:
```
$ megadld-cli -h
usage: megadld-cli.py [-h] --ip IP --url URL [--port PORT]

optional arguments:
  -h, --help            show this help message and exit
  --ip IP, -i IP        Server IP
  --url URL             Mega url
  --port PORT, -p PORT  Server port (Default=8000)

```