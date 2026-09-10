#!/bin/bash
set -euo pipefail

NS2_TS="${PDNS_NS2_TAILSCALE:?set PDNS_NS2_TAILSCALE to ns2 tailscale IPv4}"
API_KEY="${PDNS_API_KEY:?set PDNS_API_KEY}"
SCHEMA=/usr/share/pdns-backend-sqlite3/schema/schema.sqlite3.sql

mkdir -p /etc/systemd/resolved.conf.d
cat >/etc/systemd/resolved.conf.d/no-stub.conf <<'EOF'
[Resolve]
DNSStubListener=no
EOF
systemctl restart systemd-resolved || true

install -d -o pdns -g pdns /var/lib/powerdns
if [ ! -s /var/lib/powerdns/pdns.sqlite3 ]; then
  sqlite3 /var/lib/powerdns/pdns.sqlite3 <"$SCHEMA"
  chown pdns:pdns /var/lib/powerdns/pdns.sqlite3
fi

if [ -f /etc/powerdns/pdns.d/bind.conf ]; then
  mv /etc/powerdns/pdns.d/bind.conf /etc/powerdns/pdns.d/bind.conf.disabled
fi

cat >/etc/powerdns/pdns.d/orvix.conf <<EOF
launch=gsqlite3
gsqlite3-database=/var/lib/powerdns/pdns.sqlite3
primary=yes
allow-axfr-ips=${NS2_TS}/32
also-notify=${NS2_TS}
api=yes
api-key=${API_KEY}
webserver=yes
webserver-address=127.0.0.1
webserver-port=8081
webserver-allow-from=127.0.0.1
default-soa-content=ns1.orvix.id hostmaster.orvix.id 0 10800 3600 604800 3600
EOF
chown root:pdns /etc/powerdns/pdns.d/orvix.conf
chmod 640 /etc/powerdns/pdns.d/orvix.conf

systemctl restart pdns
systemctl is-active pdns
ss -ulnp | grep ':53' || true
pdnsutil list-all-zones || true
echo "NS1 sqlite primary ready. AXFR only from ${NS2_TS}"
