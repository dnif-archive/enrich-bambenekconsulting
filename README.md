## Bambenek Consulting   
  http://osint.bambenekconsulting.com/feeds/
### License
Use of Bambenek Consulting feeds API is governed by the license here: http://osint.bambenekconsulting.com/license.txt

### Overview
Bambenek Consulting is an cybersecurity investigations and intelligence consulting firm focusing on tackling major criminal threats. Every day, there is another story about another company having their banking accounts drained, someone having their identity stolen, or critical infrastructure being taken offline by hostile entities.  Led by IT security expert, John Bambenek, we have the resources to bring to your business so you can be sure your organization and your customers’ data is safe.

There are two main category of the feeds provided
#### Bambenek Consulting Domain feeds  
 Master feed of known, active and non-sinkholed C&Cs domain names.  
 This feed is merely an aggregate of the other feeds which list domain names of active and non-sinkholed C&C servers. The
 current list of malware families that are represented in these feeds are:
  - Cryptolocker
  - GameOver Zeus (p2p and post-Tovar)
  - PushDo
  - matsnu
  - tinba
  - qakbot
 For more information on this feed go to: http://osint.bambenekconsulting.com/manual/c2-dommasterlist.txt

#### Bambenek Consulting IP feeds
 Master feed of known, active and non-sinkholed C&Cs IP addresses
 This feed is merely an aggregate of the other feeds which list IP addresses of active and non-sinkholed C&C servers. The
 current list of malware families that are represented in these feeds are:
  - Cryptolocker
  - GameOver Zeus (p2p and post-Tovar)
  - tinba
  - matsnu
  - pushdo
  - qakbot
 For more information on this feed go to: http://osint.bambenekconsulting.com/manual/c2-ipmasterlist.txt

### Using the Bambenek Consulting feeds API
 The Bambenek Consulting feeds API is found on github at

https://github.com/dnif/enrich-bambenekconsulting

#### Getting started with Bambenek Consulting feeds API

1. #####    Login to your Data Store, A10 containers  
   ACCESS DNIF CONTAINER VIA SSH : [Click To Know How](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. #####    Move to the ‘/dnif/<Deployment-key/enrichment_plugin’ folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/enrichment_plugin/
```
3. #####   Clone using the following command  
```  
git clone https://github.com/dnif/enrich-bambenekconsulting.git bambenekconsulting
```
### API feed output structure
  | Fields        | Description  |
| ------------- |:-------------:|
| $EvtType      | An IP/Domain |
| $EvtName      | The IOC      |
| $IntelRef | Feed Name      |
| $IntelRefURL | Feed URL      |
| $ThreatType | DNIF Feed Identification Name |      

An example of API feed output
```
{'$EvtType': 'DOMAIN',
'$EvtName': 'simkov.com',
'$AddFields': {
'$IntelRefURL': ['http://osint.bambenekconsulting.com/manual/virut.txt'], 
'$ThreatType': ['virutC&C'], 
'$IntelRef': ['BAMBENEKCONSULTING']
}}
```
