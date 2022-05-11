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

//Resizing Screen
window.onresize = init;

function init() {
    W = innerWidth;
    H = innerHeight;
    $('body').height(H + "px");
    $('#ol').height(H + "px");
}
/Showing instructions
window.onload = function() {
    $("#ol").html(`<center><div id="inst"><h1>Instructions</h1><li>Make pairs of similiar blocks by flipping them.</li><li>To flip a block you can click on it.</li><li>If two blocks you clicked are not similar, they will be flipped back.</li><p style="font-size:18px;">Click one of the following mode to start the game.</p></div><button onclick="start(3, 4)">3 x 4</button> <button onclick="start(4, 4)" style="w">4 x 4</button><button onclick="start(4, 5)">4 x 5</button><button onclick="start(5, 6)">5 x 6</button><button onclick="start(6, 6)">6 x 6</button></center>`);
}