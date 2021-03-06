""" Gen3 RNG tools. """
from itertools import islice

from pokemon import BoxMon


def seeds(seed: int = 0, frame: int = 0, limit: int = 2**32):
    """ Yields successive seeds (32 bits) up to a limit.

    Args:
        seed (int): Initial seed. Defaults to 0.
        frame (int): Cycles to skip. Defaults to 0.
        limit (int): Number of seeds to produce. Defaults to 2**32.
    >>> list(seeds(limit=4))
    [0, 24691, 3917380458, 1383151765]
    """
    if frame and seed == 0:  # Use fast seed calculation
        seed = seed_at(frame)
    elif frame and seed != 0:  # Skip cycles manually
        for _ in range(frame):
            seed = 0xffffffff & seed * 0x41c64e6d + 0x6073
    for _ in range(limit):
        yield seed
        seed = 0xffffffff & seed * 0x41c64e6d + 0x6073


def rand(seed: int = 0, frame: int = 0, limit: int = 2**32):
    """ Yields successive RNG *values* (16 bits) up to a limit.

    Args:
        seed (int): Initial seed. Defaults to 0.
        frame (int): Cycles to skip. Defaults to 0.
        limit (int): Number of values to produce. Defaults to 2**32.
    """
    return (seed >> 16 for seed in seeds(seed, frame, limit))


def seed_at(cycle: int) -> int:
    """ Get the seed that would occur after a number of cycles.

    This is only valid when the initial seed is zero.

    Args:
        cycle (int): The number of elapsed RNG cycles

    Returns:
        int: Seed that occurs on that frame.
    >>> seed_at(800) == list(seeds(frame=800, limit=1))[0]
    True
    >>> seed_at(0) == 0 == seed_at(2**32)
    True
    >>> (seed_at(2**32-1)*0x41c64e6d + 0x6073) % 2**32
    0
    """
    m = 2**32
    a = 0x41c64e6d
    b = 0x6073
    # I'm unable to find the webpage I found this method on, but it works.
    # It seems to be related to modular exponentiation
    res = (a-1)*m
    return (((pow(a, cycle, res)-1) % res)//(a-1)*b) % m
    return ((a**cycle-1)//(a-1)*b) % m


def cycles_to(seed: int):
    """ Find the number of RNG cycles needed to get a seed, starting from 0.

    Args:
        seed (int): Seed to match.

    Returns:
        int: The frame that seed occurs on.
    >>> cycles_to(0)
    0
    >>> cycles_to(0x6073)
    1
    """
    for i, seed2 in enumerate(seeds()):
        if seed2 == seed:
            return i


def choose_land_index(rng):  # pick a wild mon index TODO: Move this
    rand = next(rng) % 100
    if rand < 20:
        return 0
    elif 20 <= rand < 40:
        return 1
    elif 40 <= rand < 50:
        return 2
    elif 50 <= rand < 60:
        return 3
    elif 60 <= rand < 70:
        return 4
    elif 70 <= rand < 80:
        return 5
    elif 80 <= rand < 85:
        return 6
    elif 85 <= rand < 90:
        return 7
    elif 90 <= rand < 94:
        return 8
    elif 94 <= rand < 98:
        return 9
    elif rand == 98:
        return 10
    else:
        return 11


def wild_mons(seed=0, cycle=0, limit=1000, diff=False, bike=False, rate=20, slots=None):
    """ Yield (cycle, seed, pid) tuples for wild pokemon encounters.

    Seed is the value of the RNG on the frame *before* the tile transition.

    Args:
        seed (int): Starting value for RNG. Defaults to 0.
        cycle (int): Cycles to skip. Defaults to 0.
        limit (int): Limit of cycles to search through. Defaults to 1000.
        diff (bool): If the previous and current metatile behaviors differ. Defaults to False.
        bike (bool): If the bike is being ridden. Defaults to False.
        rate (int): Encounter rate of area. Defaults to 20.
        slots (set): Set of allowed wild encounter slots. Defaults to all slots.
    """
    offset = 2  # Skip 1 frame; use the next
    rate *= 16
    rate = (80 * rate // 100) if bike else rate
    rate = min(rate, 2880)
    for i, base in enumerate(seeds(seed, cycle, limit), cycle):
        rng = rand(base, offset)
        if diff and not next(rng) % 100 < 60:  # Global encounter check
            continue
        elif not next(rng) % 2880 < rate:  # Local encounter check
            continue
        slot = choose_land_index(rng)
        if slots is not None and slot not in slots:
            continue
        level = next(rng) % 10  # TODO: Replace with range
        nature = next(rng) % 25  # PickWildMonNature
        first = True
        pid = 0
        while first or pid % 25 != nature:  # CreateMonWithNature
            low = next(rng)
            high = next(rng)
            pid = (high << 16) | low
            first = False
        yield i, base, pid


def method1_mons(seed=0, cycle=0, limit=1000):
    """ Yields (cycle, pid, ivs) tuples for method 1 pokemon.

    Args:
        seed (int): Starting value for RNG. Defaults to 0.
        cycle (int): Cycles to skip. Defaults to 0.
        limit (int): Limit of cycles to search through. Defaults to 1000.
    """
    for i, base in enumerate(seeds(seed, cycle, limit), cycle):
        rng = rand(base)
        pid = next(rng) | (next(rng) << 16)
        value = next(rng)
        hp, at, de = value & 0x1f, (value & 0x3e0) >> 5, (value & 0x7c00) >> 10
        value = next(rng)
        sp, sa, sd = value & 0x1f, (value & 0x3e0) >> 5, (value & 0x7c00) >> 10
        yield i, pid, (hp, at, de, sa, sd, sp)


def battle_seeds(seed=0, frame=0, limit=1000):
    """ Yield success battle seeds. The RNG advances twice per frame in battle.

    Args:
        seed (int): Starting seed. Defaults to zero.
        frame (int): Cycles to skip. Defaults to 0.
        limit (int): Number of seeds to yield. Defaults to 1000.
    """
    yield from islice(seeds(seed, frame*2, limit*2), 0, None, 2)


def crit_dmg_calc(rng, chance=0):
    """ Calculates the criticality and damage using a seed.

    Args:
        rng: RNG generator as returned by rand().
        chance (int): Number of critical stages. Defaults to zero.

    Returns:
        (crit, dmg) tuple where crit is whether the attack crit, and dmg is the (unadjusted) damage.
    """
    chances = (16, 8, 4, 3, 2)
    crit = (next(rng) % chances[chance]) == 0
    for _ in range(6):  # Skip 6 values
        next(rng)
    dmg = 100 - (next(rng) % 16)
    return crit, dmg


def acc_calc(rng, acc_stage=6, evade=6, move_acc=95):
    """ Calculate whether a move will hit using a seed.

    Args:
        rng: RNG generator as returned by rand().
        acc_stage (int): Attacker's accuracy stages. Defaults to 6.
        evade (int): Defender's evasion stages. Defaults to 6.
        move_acc (int): Move accuracy. Defaults to 95.

    Returns:
        (hit, acc) where hit is whether the attack hits, and acc is the actual calculation.
    """
    dividends = (33, 36, 43, 50, 60, 75, 1, 133, 166, 2, 233, 133, 3)
    divisors = (100, 100, 100, 100, 100, 100, 1, 100, 100, 1, 100, 50, 1)
    assert len(divisors) == len(dividends) == 13
    buff = acc_stage + 6 - evade
    calc = dividends[buff] * move_acc
    calc //= divisors[buff]
    acc = (next(rng) % 100) + 1
    return acc <= calc, acc


def acc_seek(seed, frame=0, limit=10, acc_stage=6, evade=6, move_acc=95):
    offset = 3  # 2 frames are skipped, the next is used
    for base in battle_seeds(seed, frame, limit):
        rng = rand(base, offset)
        hit, acc = acc_calc(rng, acc_stage, evade, move_acc)
        print(f'{base:08x}:{acc:03d}{"Y" if hit else "N"}', end=' ')
    print()


def dmg_seek(seed, frame=0, limit=10, chance=0):  # Explore critical and damage values
    offset = 3  # 2 frames are skipped, the next is used
    for base in battle_seeds(seed, frame, limit):
        rng = rand(base, offset)
        crit, dmg = crit_dmg_calc(rng, chance)
        print(f'{base:08x}:{dmg:03d}{"!" if crit else ""}', end=' ')
    print()


def nocrit_seek(seed, frame=0, limit=10):  # For tutorial battles
    offset = 3
    i = 0
    for base in battle_seeds(seed, frame, limit):
        rng = rand(base, offset)
        dmg = 100 - (next(rng) % 16)
        print(f'{base:08x}:{dmg:03d} {i}', end=' ')
        if dmg == 100:
            print()
        i += 1
    print()


nature_map = {'hardy': 0, 'lonely': 1, 'brave': 2, 'adamant': 3, 'naughty': 4, 'bold': 5, 'docile': 6,
              'relaxed': 7, 'impish': 8, 'lax': 9, 'timid': 10, 'hasty': 11, 'serious': 12,
              'jolly': 13, 'naive': 14, 'modest': 15, 'mild': 16, 'quiet': 17, 'bashful': 18,
              'rash': 19, 'calm': 20, 'gentle': 21, 'sassy': 22, 'careful': 23, 'quirky': 24}
r_nature = {v: k for k, v in nature_map.items()}

gender_thresholds = {'1:7': 225, '1:3': 191, '1:1': 127, '3:1': 63, '7:1': 31}


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    nocrit_seek(0x9649A84C, limit=100)
