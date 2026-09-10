#!/bin/bash
set -euo pipefail

NS1_TS=100.92.240.102
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
secondary=yes
allow-notify-from=${NS1_TS}/32
EOF
chown root:pdns /etc/powerdns/pdns.d/orvix.conf
chmod 640 /etc/powerdns/pdns.d/orvix.conf

systemctl restart pdns
systemctl is-active pdns
ss -ulnp | grep ':53' || true
pdnsutil list-all-zones || true
echo "NS2 sqlite secondary ready. Notify from ${NS1_TS}"
