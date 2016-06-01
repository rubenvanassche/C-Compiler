mst 0
cup 0 init
init:
ssp 5
mst 0
cup 0 main0
hlt
main0:
ssp 6
ldc i 3
str i 0 5
lod i 0 5
conv i i
lod i 0 5
conv i i
add i
retp


mst 0
cup 0 init
init:
ssp 5
mst 0
cup 0 main0
hlt
main0:
ssp 7
ldc i 3
str i 0 5
ldc i 4
str i 0 6
lod i 0 5
conv i i
lod i 0 5
conv i i
add i
retp
