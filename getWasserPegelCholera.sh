#!/bin/bash


curl "https://www.noe.gv.at/wasserstand/kidata/stationdata/$1_Wasserstand_3Tage.csv" \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Referer: https://www.noe.gv.at/wasserstand/' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Linux"' -s | tail -1
