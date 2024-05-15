from components import COMPONENT_PRICES, COMPONENT_NAMES

def process_order(components):
    parts = [COMPONENT_NAMES[comp] for comp in components]
    total = sum(COMPONENT_PRICES[comp] for comp in components)
    return parts, total
