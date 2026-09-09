"""Check local links and the worked numerical claims without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote
from fractions import Fraction as F
root=Path(__file__).parent
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.ids=[]; self.icons=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link' and 'icon' in a.get('rel','').split():self.icons.append(a)
        if 'id' in a:self.ids.append(a['id'])
        for key in ('href','src'):
            if key in a:self.links.append(a[key])
for path in [root.parent/'index.html', *root.glob('*.html')]:
    parser=Links();parser.feed(path.read_text())
    assert len(parser.icons)==1,f'Missing or duplicate favicon in {path}'
    icon=parser.icons[0]
    assert icon.get('type')=='image/svg+xml',path
    assert (path.parent/icon['href']).resolve()==(root.parent/'favicon.svg').resolve(),path
    assert (path.parent/icon['href']).is_file(),path
for path in root.glob('*.html'):
    parser=Links();parser.feed(path.read_text())
    assert len(parser.ids)==len(set(parser.ids)),f'Duplicate ID in {path}'
    for link in parser.links:
        file=unquote(link.split('#')[0])
        if not file or ':' in file:continue
        assert (path.parent/file).exists(),(path,link)

def mv(a,v):return [sum(F(x)*F(y) for x,y in zip(row,v)) for row in a]
def mm(a,b):return [mv(list(zip(*b)),r) for r in a]
def rank(a):
    a=[[F(x) for x in r] for r in a];r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];s=a[r][c];a[r]=[x/s for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                s=a[i][c];a[i]=[x-s*y for x,y in zip(a[i],a[r])]
        r+=1
    return r
assert mv([[2,1],[1,2]],[2,3])==[7,8]
assert mm([[1,2],[0,1]],[[2,0],[1,3]])==[[4,6],[1,3]]
assert mm([[2,0],[1,3]],[[1,2],[0,1]])==[[2,4],[1,5]]
assert mm([[2,1],[1,1]],[[1,-1],[-1,2]])==[[1,0],[0,1]]
a=[[1,2,-1],[2,5,1]]
assert mv(a,[-5,3,0])==[1,5] and mv(a,[7,-3,1])==[0,0]
a=[[1,2,0,3],[0,0,1,-1]]
assert mv(a,[2,-1,0,0])==[0,0] and mv(a,[3,0,-1,-1])==[0,0]
s=[[1,1],[1,-1]];si=[[F(1,2),F(1,2)],[F(1,2),F(-1,2)]]
assert mm(mm(si,[[2,1],[1,2]]),s)==[[3,0],[0,1]]
# Exercise results
v=[F(3,8),F(3,8),F(1,4)]
assert mv([[6,4,3],[6,0,9],[0,8,0]],v)==[12*x for x in v]
assert mv([[2,1],[-1,1],[3,-2]],[2,-1])==[3,-3,8]
assert mv([[1,1,2],[1,2,-1],[1,3,1]],[-6,3,2])==[1,-2,5]
a=[[3,2,1],[1,1,1],[1,-3,0],[2,3,1]]
assert rank(a)==3
minor=a[:3];det=minor[0][0]*(minor[1][1]*minor[2][2]-minor[1][2]*minor[2][1])-minor[0][1]*(minor[1][0]*minor[2][2]-minor[1][2]*minor[2][0])+minor[0][2]*(minor[1][0]*minor[2][1]-minor[1][1]*minor[2][0])
assert det==7
assert mv([[1,-1],[0,1],[2,-1]],[8,9])==[-1,9,7]
assert mv([[1,0,1],[2,-1,0],[-1,2,-1]],[-1,9,7])==[6,-11,12]
print('PASS: local links, unique IDs, matrix products, inverse, elimination solutions, null spaces, basis change, selected exercise results.')
