import json

from model.network import DynamicBayesianNetwork

with open('sample_data.json') as file:
    data = json.loads(file.read())

attack_graph = data['attack_graph']
exploitability = data['exploitability']
remediation_level = data['remediation_level']
report_confidence = data['report_confidence']

network1 = DynamicBayesianNetwork(deployment_scenario=data, attack_graph=attack_graph,
                                  exploitability=exploitability, remediation_level=remediation_level,
                                  report_confidence=report_confidence, time_step=1, time_layer=1)

result = {
    'status': True,
    'data': {
        'cia': network1.get_cia_assets(),
        'likelihood': network1.get_likelihood(),
    }
}

print(result)
