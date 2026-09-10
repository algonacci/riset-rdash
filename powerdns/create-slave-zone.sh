#!/bin/bash
set -euo pipefail

ZONE="${1:?usage: create-slave-zone.sh example.my.id}"
NS1_TS="${PDNS_NS1_TAILSCALE:-100.92.240.102}"

pdnsutil create-slave-zone "${ZONE}" "${NS1_TS}" || true
pdns_control retrieve "${ZONE}"
sleep 1
pdns_control rediscover
pdns_control reload
dig @127.0.0.1 "${ZONE}" SOA +norecurse +short
