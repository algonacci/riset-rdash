#!/bin/bash
set -euo pipefail

NS1_TS="${PDNS_NS1_TAILSCALE:?set PDNS_NS1_TAILSCALE to ns1 tailscale IPv4}"

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y pdns-server pdns-backend-sqlite3 sqlite3 dnsutils

mkdir -p /etc/systemd/resolved.conf.d
cat >/etc/systemd/resolved.conf.d/no-stub.conf <<'EOF'
[Resolve]
DNSStubListener=no
EOF
systemctl restart systemd-resolved

install -d -o pdns -g pdns /var/lib/powerdns
if [ ! -f /var/lib/powerdns/pdns.sqlite3 ]; then
  sqlite3 /var/lib/powerdns/pdns.sqlite3 </usr/share/pdns-backend-sqlite3/schema/schema.sqlite3.sql
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

systemctl enable --now pdns
systemctl restart pdns

ss -ulnp | grep ':53' || true
echo "NS2 ready. No zones yet. Slave notify from ${NS1_TS}"
