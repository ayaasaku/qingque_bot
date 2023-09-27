#天鳳牌理分析 https://tenhou.net/2/
#0 = dora
class Tile:
    def __init__(self, type_: str, idx: int=1, subtype: str=''):
        '''construct tile
        Tile('bamboo', idx=8), Tile('dragon', subtype='white'), Tile('wind', subtype='east')
        '''
        assert type_ in {'characters', 'bamboo', 'dots', 'honor'}
        if type_ in {'characters', 'bamboo', 'dots'}:
            assert idx in {1, 2, 3, 4, 5, 6, 7, 8, 9}
        else:
            assert subtype in {'east', 'south', 'west', 'north', 'white', 'green', 'red'}
        self.type_ = type_
        self.idx = idx
        self.subtype = subtype

    @classmethod
    def from_str(self, short_str: str): 
        '''construct tile from simple string like '9s', '4m', '3p', 'east', 'green'
        '''
        assert short_str in {
            '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s',   # 索子
            '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m',   # 万子 
            '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',   # 筒子
            '1z', '2z', '3z', '4z', '5z' '6z', '7z',     # 东南西北白發中
            
        }

        if short_str[0].isdigit():
            if short_str[1] == 'm': # 9m
                return Tile('characters', idx=int(short_str[0]))
            elif short_str[1] == 's': # 9s
                return Tile('bamboo', idx=int(short_str[0]))
            elif short_str[1] == 'p': # 9p
                return Tile('dots', idx=int(short_str[0]))
            elif short_str[1] =='z': # east
                return Tile('honor', idx=int(short_str[0]))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        # if self.type_ in {'characters', 'bamboo', 'dots'}:
        #   return f'[{self.type_}-{self.idx}]'
        # else:
        #   return f'[{self.type_}-{self.subtype}]'
        if self.type_ == 'characters':
            return f'{self.idx}m'
        elif self.type_ == 'bamboo':
            return f'{self.idx}s'
        elif self.type_ == 'dots':
            return f'{self.idx}p'
        else:
            return f'{self.idx}z'

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __hash__(self):
        return hash(self.__repr__())



# 顺子
def is_sequence(tiles:list):
    tiles.sort(key=lambda x: x.idx)
    if len(tiles) != 3:
        return False
    if not (tiles[0].type_ == tiles[1].type_ == tiles[2].type_):
        return False
    if tiles[0].type_ not in {'characters', 'bamboo', 'dots'}:
        return False
    if not (tiles[0].idx + 1 == tiles[1].idx + 1 == tiles[2].idx):
        return False
    return True


# 刻子
def is_triplet(tiles):
    if len(tiles) != 3:
        return False
    if not (tiles[0] == tiles[1] == tiles[2]):
        return False
    return True

# 杠子
def is_kong(tiles):
    if len(tiles) != 4:
        return False
    if not (tiles[0] == tiles[1] == tiles[2] == tiles[3]):
        return False
    return True

# [1, [2, [3, 4]]] => (1, (2, (3, 4)))
def recursive_tuple(x):
    if isinstance(x, list):
        return tuple([recursive_tuple(elem) for elem in x])
    else:
        return x

def dedup(l):
    return [value for index, value in enumerate(l) if value not in l[:index]]


#test
if __name__ == '__main__':
    # t1 = Tile(type_='characters', idx=9)
    # print(t1)

    # t2 = Tile.from_str('9w')
    # print(t2)

    t = [Tile.from_str(str) for str in ['3w', '9w', '1s', '4s', '5p', 'east', 'south', 'north', 'green', '4s', 'north']]
    from random import shuffle
    shuffle(t)
    print(t)
    
    t.sort(key=lambda x: x.__repr__())
    print(t)

    # print(set(t))