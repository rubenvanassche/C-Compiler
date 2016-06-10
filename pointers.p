mst 0
cup 0 init
init:
ssp 5
mst 0
cup 0 main0
hlt
add0:
ssp 7
ind a
ind a
add i
str i 0 0
retf
retp
retp
main0:
ssp 9
ldc i 5
str i 0 5
ldc astr a 0 6
ind a
str i 0 7
TODO: String datastr a 0 8
retp
