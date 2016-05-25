"""How to find friends - https://checkio.org/mission/find-friends/"""


def check_connection(network, first, second):
    network = set(map(lambda x: frozenset(x.split('-')), network))
    future = set()
    visited = set()

    visited.add(first)
    ng = find_neighbours(network, first)
    future = future.union(ng)

    while future:
        if {first, second}.issubset(visited):
            return True
        node = future.pop()
        if node not in visited:
            visited.add(node)
        else:
            continue
        future = future.union(find_neighbours(network, node))

    return False


def find_neighbours(network, name):
    pairs = set(filter({name}.issubset, network))
    neighs = set().union(*pairs)
    return neighs - {name}


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
