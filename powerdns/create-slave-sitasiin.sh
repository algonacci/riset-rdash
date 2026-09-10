#!/bin/bash
set -euo pipefail

ZONE=sitasiin.my.id
NS1_TS=100.92.240.102

pdnsutil create-slave-zone "${ZONE}" "${NS1_TS}" || true
pdnsutil retrieve "${ZONE}" || true
pdnsutil list-zone "${ZONE}" || true
dig @127.0.0.1 "${ZONE}" SOA +norecurse
