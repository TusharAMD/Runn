var em = ["💐", "🌹", "🌻", "🏵️", "🌺", "🌴", "🌈", "🍓", "🍒", "🍎", "🍉", "🍊", "🥭", "🍍", "🍋", "🍏", "🍐", "🥝", "🍇", "🥥", "🍅", "🌶️", "🍄", "🧅", "🥦", "🥑", "🍔", "🍕", "🧁", "🎂", "🍬", "🍩", "🍫", "🎈"];
//Shuffling above array
var tmp, c, p = em.length;
if (p)
    while (--p) {
        c = Math.floor(Math.random() * (p + 1));
        tmp = em[c];
        em[c] = em[p];
        em[p] = tmp;
    }

//Variables
var pre = "",
    pID, ppID = 0,
    turn = 0,
    t = "transform",
    flip = "rotateY(180deg)",
    flipBack = "rotateY(0deg)",
    time, mode;