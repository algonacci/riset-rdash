#!/bin/bash
set -euo pipefail

ZONE="${1:?usage: create-zone.sh example.my.id}"
ZONE="${ZONE%.}."
PARK_IP="${PARK_IP:-103.59.160.126}"
API_KEY="${PDNS_API_KEY:?set PDNS_API_KEY}"
API="http://127.0.0.1:8081/api/v1/servers/localhost/zones"

payload=$(cat <<EOF
{
  "name": "${ZONE}",
  "kind": "Master",
  "nameservers": ["ns1.orvix.id.", "ns2.orvix.id."],
  "rrsets": [
    {
      "name": "${ZONE}",
      "type": "A",
      "ttl": 3600,
      "changetype": "REPLACE",
      "records": [{"content": "${PARK_IP}", "disabled": false}]
    },
    {
      "name": "www.${ZONE}",
      "type": "A",
      "ttl": 3600,
      "changetype": "REPLACE",
      "records": [{"content": "${PARK_IP}", "disabled": false}]
    }
  ]
}
EOF
)

curl -sS -X POST "$API" \
  -H "X-API-Key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$payload"

echo
pdns_control notify "${ZONE%.}" || true
echo "zone ${ZONE} created. A @/www -> ${PARK_IP}"
