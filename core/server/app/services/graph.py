import pydot

from core.attack_graph.main import generator_attack_graph


class GraphService:
    
    def generate_coordinates(gph: dict, rankdir='LR', nodesep = 0.75, ranksep=2):
        def generator_menu(vuls):
            def find_node_by_id(id, nodes):
                for node in nodes:
                    if node['id'] == id:
                        return node['label']
                return None
            result = {}
            edges = vuls['edges']
            nodes = vuls['nodes']
            for edge in edges:
                source = find_node_by_id(edge['source'], nodes)
                target = find_node_by_id(edge['target'], nodes)
                if source in result:
                    result[source] = result[source] + [target]
                else:
                    result[source] = [target]
            return result

        def find_node_by_label(label, nodes):
            for node in nodes:
                if node['label'] == label:
                    return node
            return None

        def draw(parent_name, child_name):
            edge = pydot.Edge(parent_name, child_name)
            graph.add_edge(edge)

        def visit(node):
            for source in node:
                for target in node[source]:
                    draw(source, target)

        menu = generator_menu(gph)
        graph = pydot.Dot(graph_type='digraph', rankdir=rankdir, nodesep=nodesep, ranksep=ranksep)
        graph.set_node_defaults(shape='box')
        visit(menu)
        graph.write_dot('tmp.dot')
        g = pydot.graph_from_dot_file('tmp.dot')

        nodes = []
        for node in g[0].get_nodes()[2:-1]:
            pos = [
                float(tmp) + 1 for tmp in node.get_pos().replace('"', '').split(',')]
            label = node.get_name().replace('"', '')
            nodes.append({
                'x': int(pos[0]),
                'y': int(pos[1]),
                **find_node_by_label(label, gph['nodes']),
            })
        gph['nodes'] = nodes
        return gph
    

    def generation_attack_graph(deployment_scenario: dict):
        return generator_attack_graph(deployment_scenario)
