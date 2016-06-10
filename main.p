mst 0
cup 0 init
init:
ssp 5
mst 0
cup 0 main0
hlt
main0:
ssp 6
ldc i 0
str i 0 5
bl1:
lod i 0 5
ldc i 10
les i
fjp el2
lod i 0 5
ldc i 1
add i
str i 0 5
ujp bl1
el2:
lod i 0 5
str i 0 0
retf
retp
retp
