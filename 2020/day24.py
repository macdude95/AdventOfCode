import itertools

instructions = ["swnenewnenenwneneeseseenwwnesenenenenene","neeewseswneewwnwsewwwsewwnwwsw","eewswwnwnwwnwwnwnwwnwnwnwnwnwswnw","nwwnwnwwnwenwnwnwnwwewsewnwnwwnww","senweeswswnwnesenwnweneeenenweeesw","neenenenewnenenenenenenwswnenene","sewneeewswneneneeenewneneneenee","seesenwsenwwsenwswswseseeneseswseswsese","ewewswswwwsewnwnwswsewww","nwnenwwwwwwwneesenwswnwwwwwsw","wnwnwsesenwnwsenwnwnwnwnwnewnenwnwnwwnwnw","nwnwnwnwenwwwnwnwnwewnwenwnwswnwnwsenw","swewsesenwsenwsesesenesweswneneese","swwwwwwwwswwwwswnwweww","nenweneesweenweseeneeenwswseeene","wsenwneseeewswswswseswswseswswseswse","sewnewwwsewwwwwwswnewnewwwww","eneesweewsweeeeenweeeenww","eswswswseswswswnwwswnwswswwswswswswsw","wnwwwnewsenwwwwnwwwsewwwnesew","nwnenwnwnwnwwnwsenwwnwnwnenwsenwnwnenwnw","swwneswwseswswwnwswneswwwewneswsww","swsweswneswwnwseseswnweswewswswswswsw","nwwsenwwwnwnwenwnwwnwnwwenwnwnww","senwnenwneenenewnenwnwnwnwwwnwnwsenw","eneeeesweneenenweneeeeewnee","eswneenenwswnesenwnwnww","wesenweweweseswnwswsenwneswwwswnw","wseenenenenenenewne","nwnwnwswnwnwwnwnwenenwnenesenwnwwnwne","nenenenenwneneeeeswe","neswswwswseswswnwswswswswswneswswwswswesw","enewsenenenenesenwseneneenenweneene","enwneeeeswneeenenene","newnewnenenenenenenenwnwwsenenenweese","weenenwneseneeeeneeenesweeene","nenwnenwnwnenwnwnweenenenwnenwneneswsw","seseeseenwseseseeseenesesesenweeew","seswnewswsenwseswwnwseseseseesesesenenw","eeeeeeeseeeseweeseee","neneweswwswswwseswwswswswwswswswsw","swswswswneswsewswswswseswesweseswnwsesew","eseseseseseswneswswnwsewswnwneswsewse","swswswneswswsewswswswne","sesesewseseeseswnwseseseseseseenwsesw","sesesesewseseesesesesesenwese","swnweseswswsenenenenwwnenewnwnwsenwenw","neseneneswneeneneeneenwneenenesewnw","nwwnesenenenenenwneneseswnenwneswneenenwnw","nwnwnwnwenwwswnwnwnenwnwnwnwswnwnwnwne","senewswswswwwww","wwswwswwwwnwwswneenewesewwswe","wwwswwneswseswsenewswswwneswswneesw","nwswewneneeeenwneeeeneswswnweeswe","swnenenenwnenwnwewwwsweneesewne","nwswwswneswswwneeseseeswswswseswswsw","seseswseneeseseesese","neeeeweeneeeeeenewsweenene","nenwnwnwnenwnwnwnwwsenenwenwnenw","nweesesewneeeneenwwneesweswenese","eenwsewenwswnwnwsewenenweneewswswsw","sesesesewsenwsenwsene","eeesewseenwwseeseseneeeneesee","wwwswswswwswswneenwswwwseswwwnw","nenenewnenesenenwseeseswnwneswnenwnenese","ewewneneseeseewnweneswneeswnee","seesenewseesesesese","sewnwneseseenenwwwnenenwnwnwsenwsenwne","enesesesenwswseseswswsesesesesesesesese","eseeeewneeeeweseeeeee","eeeneeneeeenwseeeeeee","sesesenwnweseeneneseseswnewseseseseseswse","weeseeeneeeeeenweswneneneenw","nwewnwseseseseseswseseneeseswsesewsesee","wwnwnwnwewwnwnwnwnwwnwnwnenwwsenw","enwsesesenwseneswewnesewneseenwewew","nwenwnwnwwswnwsenwenenwnwnwnenwwnwnwsw","wnwwnwnenwwnwnwnwnwnwesewnwwenwsw","sewseswneenwnwesesenwseeswsesesesese","weswnwnwnwnwwsewnwnwwnewnwww","nwwwwnwwwwwnwewnwewswnwwwnw","wwwwnwwnwwwwsenwnewwwwswwew","seswnewneswsenwswswseseswwneneesewne","newseswnwwwwwwwnewswswwwwsew","nenwnenenwseneneneswnwenwnwnenw","enwnwswneenewswse","eseswnwsesenwsesenwseseweenwseseswse","wewsenesesenewsewene","eeswseewsenwsesenwswnenw","swswneswswswneswsewswweswwswswswswsw","wswswnwseneeesweesesenwnwnwnwsenwsewse","ewenenewseeeeneneeenwswneneneee","seeeseeseeseneseesesewseesewwsene","swsweswswwswseswswnwswweeseswswswswnw","nwnwnenenenenwsewnenesenenenenenesenwne","neneseseneeewnenewseenwnwnenenwnene","swsenwseweesesenwnweeweewee","weseeeneeeeeneneeneeeneswee","nwnwnwnwneswnenwwswnwnwnwnwnwnwnww","nenweneswnenwnwnwne","nenweneeneswnewswswnwnenesewenenenwnw","swsweeswnwnwwsesesw","nenenewnenenenenenenenenenwnewnenesenwse","neswwwwswewwswwswswsewwwneww","nwnenenenenenesenenwneeneneneneswnewne","swwwnwnwwnwwwwnwnwewnwww","wwswwewwwsewswswwswwsewenenesww","newseseneeneswnenwnenwseweenenwene","swswwwwswswwwnenwwwwewsewswswnw","nwnwnwnwenwnwnwnwseeswnenwnwwnwnwnesw","swnwnewneewswwswnwenwswwnwnwwwnew","seneswsewswseswsenwnewswwwnwwswnesww","sewwwnwnesenwwwwwnewwwwnww","nenenenwseswnwnenenwnw","wwswnwswwwwnwwwewewseswwww","neneneeneneswseneeswnewneeeneeenenene","wsewwwswnewnwnwewwwnwswwnwwnww","nwneewneeneneeneeswneeneneenenee","neswnwseeswneneswsewswsw","eswswsewswswnwswnweswnwneswsesweesw","nesewnenenenenwneneseneneneneneneewne","nwnwnwnwnwnwnwswnewwwswne","swneneenwwswesenenwwnesewswnewwswswnw","swnwwwnwnwnwnesenwnwnwwsenwnwwnwnwnw","seseneseseneseswseseswseswswsesese","swnwswenenenweee","seseseeseesewseseswseseseswsesenesww","swseesesesewneseswswnwswswswnenenwnese","seenenwswnenesewneswneswneewneweneene","seeweeweneeeneneenweswweww","neswwswswswnwswswnwnenwsesesweewnene","eenwwneeswseenweeeeeswewnew","eweenweseeeseeewseenwseneswe","ewwwwewnwsewwwwwwswwwenww","swnewneeneneenenwnenwnenenenenenenwnw","sewewswswwnwwwwwenwnewwswenw","nwnwnenwnwnwswnwsenwseneneenwswswnwnenw","seeseseeesewnwseseeeneseeewsese","nenewneneneneneenwnenenwnenenw","seseneswswswsweswswswsenesewseswswsesw","newwwswwnewnwwwnwsewwwseeswne","neenwnwnenenenenenesewnwne","swnenewwsenenenwnenwweseseswnesesww","wwwwnweewwwnwnw","swneswwswewwswswwswseswneseww","sewseseseseseseseesenee","swsewnwwwneswswseswswwnewsewswswswwsw","wneseewewnwsweswewnwnwwnwswsew","swsesewswneseenwseswsesweswswseswnwsw","nenwenwnwwnenwnwne","nwnwnwnwsenenenenenwnwneswnwswnenwnwnene","sewwnwwwneswswenwwswwswsweseswse","neeneseneeswneswneneenenenenenwnesenwnw","swswnwswswswwswswswswseswswswseneswswsw","eeeeneeeeeneswesweneeeee","swswseeswnwnwswswswswswseswswwsweswsww","nwnwnenwnwenwnenwnwnwnwnwnwnwsw","swsenwwseseesenwsewsenweseseseseseswne","eewwswswswswswsweswenwneweswswnw","neeeneneseeeneswneeneewnwneeeee","swwsweneswneswewwsenewswswwesesewnw","swweeeseesenwsesesweseesenwnwee","nwewnwnwnwseswnwnwnwnwwnwwenwnwwnwnesw","eeeeeeeeeseeeesesenwe","neeneneswsenenewnenwwnwseswneneeenwnene","eseeeeeewenwse","eeeneesweeeeweeesewneeeee","swswsweswswswswswsesenwsw","wwswwwwwsewwwwseswnewwwnewsw","eswnesenweswewenenwnesweeeeene","nwwswnwsweeweeenewneneneneneneswnese","nweenwenwnwneswnenwnwnwnwswswswnwenwnwnw","neswneneneenwnenenene","wwwwwswwwwwswwnesw","wwwsewnwnwwnwwnwwwwweewwwsw","nwwnwnwnewewwwwnwwnwwwswnww","swseswswsewswsweneswseswswwnwsesenesesesw","nwenesenenewnwnwnenwneswseneswnenenenene","neneeneseneneenweeeneswnw","swnwewseswswwnewswswswwweeswswse","swseswswwneswswswswswswswswswswseneswsw","wswnwseswnwneswwnewnenweesw","nwnwwnwnenwnesenwnwwnwnwnwenwsenenenw","swneswswnwseseseseswnew","wswsweswseswswseswswswswswsw","neenenenenwneneneeenenenwsewsenenenene","weswswswwswsewwsweneswseswwswnesw","wnwnwnwwswnewwwwwesewneww","nweneenenenesenwseneeeee","sewseesesesesesewneewsee","eseseseseesewseeseneesesese","eeweeseneenwneweeeseeeeseene","swwwwnenewswwswsenwwswew","swwswswwwswnwwswsenwseswnwweesww","seneneneneneneweswnenenenewnwne","nwsewwenwewsewwnwswnwwnw","weneneneneswsweweseeeswseseeew","neseswseseswseswseseswsesewsewseseene","nenwwnwsenwsenwnwswnwsenwnwnwnenwesw","eeswsweeenwseneeeeeeenenwewe","enweeeeenweeeeeeeseseesesw","eseswseseseseneseseseswswneswsesewswsenw","nwnwnwnwnwwnwnwswnwewnweenwnwnwnwnww","nwwwnwswwnwnwwnewnww","enwsesenenwsenwnwnwnenwswswnwnewnwnwenw","nwnwnwswnenwnwnwnwnenenenenwnwnw","swwnwnwenwnenwwwwwwneswewnwwsw","wswwwswewswswwwwwswswswwe","wswwesesewswwnwwwwnwnewwswwwsw","esewnwesenwsesesweseeeeswenwswnw","enenwnenenenenenewenenenesweeenene","swneeeeeeewneswenwsenwenwsenwsw","nenwnwnenwenwnwnwnwnwnwsenwnwnwnwnww","ewswwseneseswswswswwnewnwnwswswne","swseseseeeseseseseesenwwseseseswsenese","seeeeseweseseseneswesee","neeseeeeeweeneseenwneswweesee","swnwnenwsenenewnweswnwnenwnw","swswswwneswwnwwwwswwsesewnweee","nwwwnwwswnwwwweswsenwwwwwwewnw","wsweewwenwnwnenwneenwnww","nwswnenwnwneswswesenenene","swseseneseeeneweswe","seseseseeeeeseenweeseswe","seswswsenwseswswwswsesesesesweswsewnese","eeeneeeeeneneseewnweneesenesw","swswswswswnwsweswswnweswswswnwsenesw","esweeeneeeenwneeeswenw","nwsenwnewwwnewswwsewnwwnenw","swwenewwwwswswswweswweenwsww","eeeeeneeeeeeew","wwwswseenewewnwswneswswswwswnenese","newneneseenenenwneneneneneneneeswnenene","eenwsenwnwnenwnwnwnenwsewnwseneswwnw","swwneswsenesenwwnwenenwswwnwnwnwnenwww","swseenwseswswenwswswnwneseseswswwswsw","nwnwnwenwwswwnwwseswnewewnwnwnwnw","wewwsenwneswwwnwsewwwwnwneww","nenwnweswnwnenwnenwnwnwnenenenwne","sesesenwwsenwswsesenwenweseseseseesesese","wwwnewwwwwsewwswwewwwww","neeneneneenenenenenweneswweenesenene","swwseeswsesenwseswswswwneswswesw","nenewswwewswwnwwwewwswswwseswe","enwseswnwsesenwneseewswswswnwenwswne","senenwnenwenenwnesewnwnwnwnesenenwwnwsew","wsenwneswswwsenwnwwwwsenenwnewewsw","neneneneneneneswneneneenenwswnenwswnene","wnwnenwnwenwswnwsenwnwnwnwnwnwne","enewswnwnenenenenenenwneseenenewnenwsw","eeewswwsenesewseneseeeseseeseee","wweeswnweneeswenewneeswseeenwnwne","swwseseseseswwneseesesesesesesenesesese","nwnwseswnwnwnwenwnwswnesenwnwwnwnwnenww","eneneneneewweeeswsewweneneeee","nwnwnwnwnwnwwswewnwenwnwnwwwnenwse","eseseseweseeeesewswseenwsenwsee","swswswsweswwnwswswswswseeswseseswswsw","nwnesewnesenenenwsewnenenewnenwnenenenw","swswwneswwswwswwswswwswwnewsww","nwnwnwneenwswwenwwsenw","enenwseseseswseseesesesesesewnww","seswsenwseseswnwswseseseswswswnwseseswne","enesesenesewsesewsesewweseseesesenwsw","swwswesewneseswnenewwewseeswswswne","eeswewweesesesenwswseenesesesene","neswswsweswswnwswswneswseswswswswswswsewsw","senwnesenenewweseswsewenenwseseseew","sweseswsewseseseswneswsesewswsesesenese","neswneneeneneswneneeneneenenenenenew","sweenenewswnweneswesweeneenwnenee","nwnewwnwsesenesesenwnwnwwnwnewwswnww","swwwwnwswswswswswswwsewwsww","nweewneneswsesewswnewwwnewswew","nesweseeeneseswwnwseswnwseswwnweswsenw","esewnwnesenwwswnenwwwnwnewnweswsw","nenwnwsenwnenenenwwsweswswnenenwenenw","esweeeewseeeeseswweeneeenwne","swenwenwwneneswnenweeswnwwnwswsee","nwswswswwswswseswswseswneswseswswesesw","nwswwnesesesweseswseswnewe","nenwnwnwnwewnwnwsenwnwnwnwnwnwwenwnw","enwsewnwwwwnweewnenenwwswwswwsw","wswswswsweswseswseneswswseswsewswswsw","nwnenwnwnwnesenenwnwnenwnenenesenwnenenesw","eeeeseneenwseswswesenwsesenwseee","enenewsewewenewsenenewseenwneswne","neenwnwneswneneswneneswnesenewenwswnee","neneseseeneswnwsenenesenwwwnwneneswnee","nwswnenenenwnenenewnwnwnwenwnwnenwnwe","nwnwnwnwnwnwnenwnwnwnesesenenwnwswnwnwnwe","senwnwnesenwnwsenwswwnwwnesene","swsewenweseeeseseseeseneeseeenw","wnenenwnenwnenenenenese","senwsenwnwwswenwnwenwneswnwnenenwnwsw","neeswswswswnwswswenw","wnewswwwwnewwsewwwwwwwww","wnwnwwnwwwnwwnwswnwnwewnwwnwne","nenenweswnenwenweneeswneseeeeese","sesenenwnenwnwnwnwsewwswswwnewwwe","ewswseswswseswsesenwseseseseseseesese","seseeeseswswswwewseswseswsesesenwsenw","seseseeseesesesesenwseneswsesesenesesw","swswenewswswswswswswnwswswwswswswswswesw","newwwwwwwwwswwnewswswnwwnweenw","swsesewseswswswseeswswneseswswnwswwseswsw","neeenweseneswneenwneswnwsenewswwnwswe","wewneswswswwnwseewsenewnwnenewsese","neneswwesenweneneneswewnwnewnwnenenee","neneesenenesewnenwwnesenwneneneneneswne","wwwwnwenwewwnwswwnwswwnwwnwww","neswnenenenewnenwnenwnenwenwsewnwnenee","nenenwswnwneneenwneswwnenenenenenenenese","neswwwswwwwwwwswwwsweenwswswsw","eneneneeenenwweneswseneneneseeneee","enenesenweenewwneneneeeweeee","sesewsesewswsesenwnweseneeswnwnewese","swswswswwwswnewenwnenenwwswseswwew","sewnewnweswwswswenwewnweenwnwnw","wwewwwwwwswwswwnwewnenwsesw","swsenenenenenwsenenenenwnenenenwneneswne","nwwwnwnwenwwnwnwnwwnwwsesenenewsewne","wnwwnesewnwnwnwsewwnwnwnwnwwnwnwnw","swsweneswswswswwnwswswenwswswswse","eseneswneeenwneeweenweeeenene","nenwewnwswwnwnwsewwwnwwswwwnew","newnwseswwneenenweneesewsw","seseseswseneewswneseseswwseweneseswnwsw","seseseswwnwnwwswwwwsewsesenenewnwne","swnwsewnwnwwnenwwwnwnwnwnesewwwnwwnw","nweeswseneeeeeeeesw","wnwnwnwsenwnwnwnwnwnwnwnwnw","swwnwsewswswweeswnwnwswnwswneewe","swseseseseswseseswneneswseewswsenweswse","swwneeeweeseeneeenenesenenwseenene","neneswnwnenenenenwnenenenenwswnwnene","nwwnwwnwsewwnwwwwenenwwnw","neenwnwwnwwswnwwnwnesewnwwwswnenesw","eeneeeeeweeeseeeeeenwese","seswneseseswseswswwswswswswnenwsesesesesw","eeneseseswsesenwneseswnwseswseseseesese","nwneewswseswwseneseseswneeswnenesese","swenwenesewnwneswneneneneneenenenee","seewswwnwwwneneseswnwwenwswewnw","eeeneeeeeeswesweeseseneswnwse","wwwswwwewesesweeswwwnewsww","enenenenewnenesenewnenwsenenewenene","eeeeenweneseeewseeswwseesesese","seseseseswneseseswsesw","neswneeesweseeeeeenwsweneeeenw","esweeweeeeenweeneeeneee","enwnwnenwnwnwneswnwnwnwnwsewnenwnenwe","swswwswswswnwwswwswswewwnewwswse","senenwnwsweswswseswseswwsw","wnweeseseeeeeseseseeeseeesesw","neseeswseswseseseeseswnewswwnesewsww","seswseswseswseswnwswseweswneeseesewnw","wwsenwsenwnwnenwswnewnwnwnwnenwsenwnwsw","swswswswseswsewswswnwswnwswswsw","ewwwwwswwwnewwwwnwwwewswsesw","eeseseenesewseseeseeseeesese","sesenwwesweeneneewenwesesesweseew","swswnwseswswswseseseswswswsw","neweneenenenwswesene","neneneneneswneneswswneenenenenwnenenenene","wwesesenewswnenwwnweswswswwnwsee","wswnewewnwwnenwswwwnwwswnwnwww","eseewneneewneeeeneswwsenenwwswnee","neneeneneenwneswewnwneswnewswneswenw","nwesewneneeneneeneneswneeeneswnenenwne","seswnwswseswseswswseswwnweesweswwsesw","wnwnwnwswnwnwnwwsenwnewwewwnwsenww","neneneneneneeseesenenwneneswnenenenwnew","eeneeeeneeseeeeeenewewnwe","nwnwswewnwwswswswseneswwswswwswswsese","swswswswseenwnwswswswwswswswswswsww","enwseneseewewenwseeseseneswewsese","wsewneneswswwwnwewswseseseneswnwsw","seswswseneneseseneswswswswswsewswswsese","eseewseneswnwneeseenwe","neswwneseswwseswswsenwswswnwswnwsewnese","swswnwswswswwswneswsesenenesenewswswse","newswswswneswnenwsewseseswswwwseswswne","eswnwnwenwneeseweswweesweenwswe","seeeseseenwesweseeesesesesese","seseseeeeeenwesenwweeeeseeese","eeeeeeenwswweeseeenewesesese","nwnenwnwnenenenenenwswnenwnwnw","nwswneswseswsenewswweeswnwswwseenw","enenwnenenwnwswswnwswswnwnwnwenwnwswnwe","nwwswnwswnwnwnweneswnwnwwne","neswnenenwnwnenwnwneneenwnwnw","nwwsenwnenwnwwnwnwnwwnwneesewnwnwsenenw","nwnwnwwnwnwnwnenwnwnwsesenwnwnwnwnwnwnw","wwnewwwsewwwwewsewwnwwww","wswswwwwwswwnenewswnwwswwwewsw","swswsewswswnenwswseswswwsweswswswsw","senwseesesesweseswseswswswseswseswsww","swenwswseeswswswswwswswseseseseswseswew","nwnenenwwswnwsenenwwnwnwnwswnwnwneswswnw","nwseswnewwnwenwwnwewsenwwswnwww","nwswwwneswnwewwsenwnwnwnwnenwwwse","wwneeeeneeeneeeseeenenenenee","wsewwwnwswwwwwneewwnewswnew","wewseweswwwnwswsewwwwwswswnw","sesewnwseeeseeseneseseeewwenwe","neswswnwswswseeswswswswwswwseswswswse","enwnenenenwnwswnenwwnwnwnwsenenenwnw","eenenenwneneneswneneseneeneesenwene","nwswewwnwnweeswnwnwwnwsenwswewnwsene","eeenwseseswsesenweseeseneneswsewsesw","sewswneeeswseneseeseseswseswnwswnwwne","swseseswseseseseseseseswsesenwsesenwese","nwnwsewsesesesenesesesesesesesese","seswseseswseeseeneswswwswwseeswnwnese","ewnwsenwsewwswwnwwneseswswseneww","nenenwneneneswnenenwneswnwneswneenw","newnwswswswwswswwswswswswwwesw","wnwswneneeeneswnwwnwnenenwnwseenwe","seneeneenenewneneeeene","nwnwswnwwneewenwnwnwwwswnwnwswsenww","sewneswnwswneseseswww","senenwnenewnenenwswneneneseenenenwnenwnw","wswneneswwneseswewnenenwnwswswnenwsw"]
# instructions = ["sesenwnenenewseeswwswswwnenewsewsw","neeenesenwnwwswnenewnwwsewnenwseswesw","seswneswswsenwwnwse","nwnwneseeswswnenewneswwnewseswneseene","swweswneswnenwsewnwneneseenw","eesenwseswswnenwswnwnwsewwnwsene","sewnenenenesenwsewnenwwwse","wenwwweseeeweswwwnwwe","wsweesenenewnwwnwsenewsenwwsesesenwne","neeswseenwwswnwswswnw","nenwswwsewswnenenewsenwsenwnesesenew","enewnwewneswsewnwswenweswnenwsenwsw","sweneswneswneneenwnewenewwneswswnese","swwesenesewenwneswnwwneseswwne","enesenwswwswneneswsenwnewswseenwsese","wnwnesenesenenwwnenwsewesewsesesew","nenewswnwewswnenesenwnesewesw","eneswnwswnwsenenwnwnwwseeswneewsenese","neswnwewnwnwseenwseesewsenwsweewe","wseweeenwnesenwwwswnew"]

# Data structure idea from https://stackoverflow.com/questions/1838656/how-do-i-represent-a-hextile-hex-grid-in-memory


def parse_instruction(ins):
    moves = []
    while len(ins) > 0:
        if ins[0] == "w" or ins[0] == "e":
            moves.append(ins[0])
            ins = ins[1:]
        else:
            moves.append(ins[:2])
            ins = ins[2:]
    return moves


def translate_move_to_delta(move):
    if move == "w":
        return -1, 1, 0
    elif move == "nw":
        return 0, 1, -1
    elif move == "ne":
        return 1, 0, -1
    elif move == "e":
        return 1, -1, 0
    elif move == "se":
        return 0, -1, 1
    elif move == "sw":
        return -1, 0, 1
    else:
        print("Invalid Move: " + str(move))
        exit()


def number_of_black_in_grid(hex_grid):
    num_black = 0
    for hexagon in hex_grid:
        if not hex_grid[hexagon]:
            num_black += 1
    return num_black


def process_instructions(instructions):
    hex_grid = {}  # True means white, False means black
    for instruction in instructions:
        moves = parse_instruction(instruction)
        deltas = [translate_move_to_delta(move) for move in moves]
        delta = 0, 0, 0
        for d in deltas:
            delta = delta[0] + d[0], delta[1] + d[1], delta[2] + d[2]
        if delta in hex_grid:
            hex_grid[delta] = not hex_grid[delta]
        else:
            hex_grid[delta] = False
    return hex_grid


print("Part 1:")
hexGrid = process_instructions(instructions)
print(number_of_black_in_grid(hexGrid))

print("Part 2:")


def get_neighbor_coordinates(h):
    return [(d[0] + h[0], d[1] + h[1], h[2] + d[2]) for d in itertools.permutations([-1, 0, 1])]


def apply_rules(hex_grid):
    # First, let's make sure all the neighbors of the hexes with values in dict are set to True to make sure we
    # consider them when applying rules
    neighbor_grid = {}
    for hexagon in hex_grid:
        neighbor_grid[hexagon] = hex_grid[hexagon]
        neighbors = get_neighbor_coordinates(hexagon)
        for neighbor in neighbors:
            if neighbor not in hex_grid:
                neighbor_grid[neighbor] = True
    hex_grid = neighbor_grid

    next_grid = {}
    for hexagon in hex_grid:
        next_grid[hexagon] = hex_grid[hexagon]
        num_of_black_neighbors = 0
        current_is_white = hex_grid[hexagon]
        for neighbor in get_neighbor_coordinates(hexagon):
            if neighbor in hex_grid and not hex_grid[neighbor]:
                num_of_black_neighbors += 1
        if current_is_white:
            if num_of_black_neighbors == 2:
                next_grid[hexagon] = False
        else:
            if num_of_black_neighbors == 0 or num_of_black_neighbors > 2:
                next_grid[hexagon] = True
    return next_grid


for _ in range(100):
    hexGrid = apply_rules(hexGrid)
print(number_of_black_in_grid(hexGrid))


