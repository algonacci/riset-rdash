#!/bin/bash
set -euo pipefail

ZONE=sitasiin.my.id
NS1_PUBLIC=103.59.160.126

pdnsutil create-zone "${ZONE}" ns1.orvix.id || true
pdnsutil replace-rrset "${ZONE}" @ NS 3600 "ns1.orvix.id." "ns2.orvix.id."
pdnsutil replace-rrset "${ZONE}" @ A 3600 "${NS1_PUBLIC}"
pdnsutil replace-rrset "${ZONE}" www A 3600 "${NS1_PUBLIC}"
pdnsutil set-kind "${ZONE}" master || pdnsutil set-kind "${ZONE}" primary || true
pdnsutil increase-serial "${ZONE}" || true
pdnsutil rectify-zone "${ZONE}"
pdnsutil list-zone "${ZONE}"
dig @127.0.0.1 "${ZONE}" SOA +norecurse
dig @127.0.0.1 "${ZONE}" NS +norecurse
