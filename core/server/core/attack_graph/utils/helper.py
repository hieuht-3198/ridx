


from core.attack_graph.model.asset import Asset


def add_reachable_asset(node1: Asset, node2: Asset):
    if node2 not in node1.reachable_assets:
        node1.reachable_assets.append(node2)