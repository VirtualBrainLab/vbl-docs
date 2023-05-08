# Development

## How to renew certificates

Run `certbot renew --cert-name data.virtualbrainlab.org` on the data server.

Copy the certificate and privkey files from `C:\Certbot\live\data.virtualbrainlab.org` to `C:\Apache24\conf\ssl`. The certificate should be named `server` and the private key `server.key`.

Restart `Services > Apache2 > Restart`

Confirm that the key propagated correctly.