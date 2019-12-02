0:
$mod+f -> fullscreen toggle
1:
$mod+Return => xterm
2:
$mod+h/Left -> focus left
3:
$mod+{f,s} -> {fullscreen,split} toggle
4:
$mod+{1-4} -> workspace {100-103}
5:
$mod+Control+Shift {8-9,0} -> move container to workspace {8-10}; workspace @1
6:
$mod+x -> {[instance="calculator"]} scratchpad show; @0 move position center
7:
$mod+{_,Shift+}h/Left -> {focus,move} left
8:
the {{quick,brown},{fox,dog/beast}} => {xterm,kitty} -e echo {jumps,over}
9:
$mod+p/Print => scrot
10:
($mod+p/Print) => scrot
11:
# This is a comment
12:
$mod+{_,Shift+}{h/Left,j/Down,k/Up,l/Right}         -> {focus,move} {left,down,up,right}
$mod+Control+Shift+{{h/Left,k/Up},{l/Right,j/Down}} -> resize {shrink,grow} {width,height} 5px or 5ppt
$mod+{_,Shift+}{1-9,0}                              -> {_,move container to }workspace {1-10}
$mod+Control+Shift {1-9,0}                          -> move container to workspace {1-10}; workspace @1
