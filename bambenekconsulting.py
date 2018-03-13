import requests
import yaml
import os

inteltype = ['INTEL_DOMAIN','INTEL_ADDR']

path = os.environ["WORKDIR"]
with open(path + "/enrichment_plugins/bambenekconsulting/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

def import_domain_intel():
    try:
        source = cfg['enrichment_plugin']['BAMBENEK_DOMAIN_SOURCE']
        response = requests.get(source, stream=True)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            s = str(line)
            s = s.strip()
            if not s.startswith("#") and s != '' and s != '##':
                s = s.strip()
                a = s.split(',')
                tmp_dict = {}
                tmp_dict["$EvtType"] = "DOMAIN"
                tmp_dict["$EvtName"] = a[0]
                tmp_dict2 = {}
                tmp_dict2["$IntelRef"] = ["BAMBENEKCONSULTING"]
                tmp_dict2["$IntelRefURL"] = [a[3]]
                b_lst = []
                tmp_str = a[1]
                tmp_type= tmp_str.split(" ")
                b_lst.append(tmp_type[3]+"C&C")
                tmp_dict2["$ThreatType"] = b_lst
                tmp_dict["$AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines,'INTEL_DOMAIN'


def import_ip_intel():
    try:
        source = cfg['enrichment_plugin']['BAMBENEK_IP_SOURCE']
        response = requests.get(source)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            s = str(line)
            s = s.strip()
            if not s.startswith("#") and s != '' and s != '##':
                s = s.strip()
                a = s.split(',')
                tmp_dict = {}
                tmp_dict["$EvtType"] = "IPv4"
                tmp_dict["$EvtName"] = a[0]
                tmp_dict2 = {}
                tmp_dict2["$IntelRef"] = ["BAMBENEKCONSULTING"]
                tmp_dict2["$IntelRefURL"] = [a[3]]
                b_lst = []
                tmp_str = a[1]
                tmp_type= tmp_str.split(" ")
                b_lst.append(tmp_type[3]+tmp_type[4])
                tmp_dict2["$ThreatType"] = b_lst
                tmp_dict["$AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines, 'INTEL_ADDR'

