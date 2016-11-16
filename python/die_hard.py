#!/usr/bin/env python
"""Spoj.com - Die Hard (Accepted)

Your initially have H amount of health and A amount of armour. At any one time
you can live in one of 3 places: fire, water and air. After every unit of time
you must change your place of living.

If you step into:
    - air, your health increases by 3 and your armour increases by 2
    - water, your health decreases by 5 and your armour decreases by 10
    - fire, your health decreases by 20 and your armour increases by 5

If your health reaches zero or less, you will die instantly.

Find the maximum time you can survive.
"""

from sys import stdin


class Player(object):

    def __init__(self, health, armour):
        self.health = health
        self.armour = armour
        self.time_alive = 0
        self.location = None

    @property
    def alive(self):
        if self.health > 0 and self.armour > 0:
            return True
        return False

    def start(self):
        while self.alive:
            self.choose_next_step()
        print self.time_alive

    def choose_next_step(self):
        # Always go back to air if you can, no negatives
        if not isinstance(self.location, Air):
            self.location = Air(self)
        # Now there are only 2 options left, Fire or Water
        elif self.armour <= 10 and not isinstance(self.location, Fire):
            self.location = Fire(self)
        else:
            self.location = Water(self)


class Location(object):

    def __init__(self, player):
        self.player = player
        self.take_effect()
        if self.player.alive:
            self.player.time_alive += 1

    def take_effect(self):
        pass


class Air(Location):
    """Health +3, armour +2"""

    def take_effect(self):
        self.player.health += 3
        self.player.armour += 2


class Water(Location):
    """Health -5, armour -10"""

    def take_effect(self):
        self.player.health -= 5
        self.player.armour -= 10


class Fire(Location):
    """Health -20, armour +5"""

    def take_effect(self):
        self.player.health -= 20
        self.player.armour += 5


if __name__ == '__main__':
    no_of_tcs = int(stdin.readline())
    for tc in xrange(no_of_tcs):
        H, A = stdin.readline().split()
        Player(int(H), int(A)).start()
