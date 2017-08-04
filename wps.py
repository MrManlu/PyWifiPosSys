import sys
print(sys.platform)
#print aquihaymanteca 
#/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport
import subprocess
def getWifiMacAddresses():
    #autodetect platform and then report based on this?
    #results = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport", "-s"])
     
    #win?
    #results = subprocess.check_output(["netsh", "wlan", "show", "network"])
 
    #linux?
    #! apt-get -y install wireless-tools
    results = subprocess.check_output(["iwlist","scanning"])
     
    results = results.decode("utf-8") # needed in python 3
    ls = results.split("\n")
    ls = ls[1:]
    macAddr={}
    for l in [x.strip() for x in ls if x.strip()!='']:
        ll=l.split(' ')
        macAddr[l.strip().split(' ')[0]]=(l.strip().split(' ')[1], l.strip().split(' ')[2])
    return macAddr
 
 
#For Mac:
postjson={'wifiAccessPoints':[]}
hotspots=getWifiMacAddresses()
for h in hotspots:
    addr,db=hotspots[h]
    postjson['wifiAccessPoints'].append({'macAddress':addr, 'signalStrength':int(db)})
     
url='https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBoWUxHvRMpWLrUBXiujznU0Ebs3gaU9Mg'.format(googleMapsAPIkey)
 
import requests
r = requests.post(url, json=postjson)
r.json()
