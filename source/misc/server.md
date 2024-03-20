# Server Instructions

## data.virtualbrainlab.org

The original data server runs on `128.95.53.64` (Lenovo mini-PC) served by Apache 2.

## data2.virtualbrainlab.org

The data server runs on `128.95.53.93` (raspberry pi #2) served by Apache 2.

## pinpoint.virtualbrainlab.org

Pinpoint is a virtual host that redirects to `data.virtualbrainlab.org/Pinpoint/`

## urchin.virtualbrainlab.org

Urchin is a virtual host that redirects to `data.virtualbrainlab.org/Urchin/`

## proxy1.virtualbrainlab.org

Heroku server, see separate instructions in Urchin

## proxy2.virtualbrainlab.org

vbl-proxy-server runs on `128.95.53.223:5000` (raspberry pi #1)

Should auto launch itself

```
cd /mnt/data/vbl-proxy-server
npm start
```

## dock.virtualbrainlab.org

Dock runs on `128.95.53.223:?` (raspberry pi #1)

Apache serves the flask app (running on gunicorn)