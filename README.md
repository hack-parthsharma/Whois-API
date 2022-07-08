## Simple Whois API

`python whois-api.py`


`curl http://localhost:5000/whois/sensepost.com`

```
{
  "address": "BROOKLYN BRIDGE OFFICE PARK 570 FEHRSEN STREET",
  "city": "BROOKLYN",
  "country": "ZA",
  "creation_date": [
    "Mon, 14 Feb 2000 00:00:00 GMT",
    "Mon, 14 Feb 2000 09:43:00 GMT"
  ],
  "dnssec": "unSigned",
  "domain_name": "SENSEPOST.COM",
  "emails": [
    "DNSADMIN@SENSEPOST.COM",
    "abuse@enom.com"
  ],
  "expiration_date": [
    "Tue, 14 Feb 2017 00:00:00 GMT",
    "Tue, 14 Feb 2017 09:43:48 GMT"
  ],
  "name": "DNS ADMIN",
  "name_servers": [
    "NS-1447.AWSDNS-52.ORG",
    "NS-1707.AWSDNS-21.CO.UK",
    "NS-41.AWSDNS-05.COM",
    "NS-881.AWSDNS-46.NET"
  ],
  "org": "SENSEPOST",
  "referral_url": "http://www.enom.com",
  "registrar": "ENOM, INC.",
  "state": "PRETORIA",
  "status": "clientTransferProhibited https://www.icann.org/epp#clientTransferProhibited",
  "updated_date": [
    "Fri, 15 Jan 2016 00:00:00 GMT",
    "Wed, 13 Jan 2016 20:53:01 GMT"
  ],
  "whois_server": "whois.enom.com",
  "zipcode": "Thu, 15 Mar 181 00:00:00 GMT"
}
```

