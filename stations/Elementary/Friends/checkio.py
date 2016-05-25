"""Friends - https://checkio.org/mission/friends/"""


class Friends:
    def __init__(self, connections):
        # print(type(connections))
        self.connections = set(frozenset(c) for c in connections)

    def add(self, connection):
        cond = connection not in self.connections
        if cond:
            self.connections.add(frozenset(connection))
        return cond

    def remove(self, connection):
        cond = connection in self.connections
        if cond:
            self.connections.remove(frozenset(connection))
        return cond

    def names(self):

        name = set()

        for friendship in self.connections:
            fr = set(friendship)
            name = name.union(fr)
        return name

    def connected(self, name):
        friends = set()
        for con in self.connections:
            if name in con:
                fr = set(con)
                friends = friends.union(fr)

        if name in friends:
            friends.remove(name)
            return friends
        else:
            return set()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])

    Friends.connected("a")

    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
