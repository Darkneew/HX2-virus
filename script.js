const Display_Move = ([x,y], player) => {
    let pawn = document.createElement("div");
    if (player == "player_1") pawn.className += "white_pawn";
    else pawn.className += "black_pawn";
    let cell = document.getElementById(`data_${x}_${y}`);
    if (cell.hasChildNodes) cell.childNodes.forEach(child => {cell.removeChild(child)});
    cell.appendChild(pawn);
    setTimeout(() => {pawn.style.opacity = 1},100)
};

const End = (p, m) => {
    let e = document.getElementById("end");
    e.style.display = "block";
    setTimeout(() => {e.style.opacity = 1}, 100);
    if (p == "equality") return e.innerHTML = "personne n'a gagné";
    e.innerHTML = `${m.split("_")[parseInt(p.split("_")[1])-1]} a gagné`;
}

const Load = async (sec) => {
    let e = document.getElementById("loading");
    switch (e.innerHTML) {
        case "":
            e.innerHTML = "."; break;
        case ".":
            e.innerHTML = ".."; break;
        case "..":
            e.innerHTML = "..."; break;
        default:
            e.innerHTML = ""; break
    };
    if (sec > 0) setTimeout(Load, 500, sec - 500)
}

const Play = async (i, match, interesting_move, sauts) => {
    let move = games[match][i];
    if (move.length < 2) return End(move[0], match);
    document.getElementById("move").innerHTML = "";
    let pname = match.split("_")[parseInt(move[0].split("_")[1])-1];
    document.getElementById("player_turn").innerHTML = pname;
    let wait = Math.floor(Math.random()* 2) * 500 + 500;
    if (interesting_move) wait += 1000 + Math.floor(Math.random()* 2) * 500;
    if (sauts[0] > 2) wait = 0;
    Load(wait);
    setTimeout(() => {
        document.getElementById("loading").innerHTML = " ";
        if (move[1] == "False") {
            document.getElementById("move").innerHTML = `${pname} saute son tour`;
            sauts[0] ++;
            if (sauts[1] == 1) sauts[1] = 0
        } else {
            document.getElementById("move").innerHTML = `${pname} joue en ${move[1][0]},${move[1][1]}`;
            Display_Move(move[1], move[0]);
            setTimeout(()=>{move[1][2].forEach((pos) => {Display_Move(pos, move[0])})}, 500);
            if (sauts[1] == 0) sauts[1] = 1;
            else {sauts[1] = 0; sauts[0] = 0}
        };
        if (sauts[0] > 2) setTimeout(Play, 250, i+1, match, false, sauts);
        else if (move[1][2].length) setTimeout(Play, 1500, i+1, match, true, sauts);
        else setTimeout(Play, 1000, i+1, match, false, sauts)
    }, wait)
};

const Choice = (match) => {
    let [p1, p2] = match.split("_");
    Grid_Setup();
    document.getElementById("vs_title").innerHTML = `${p1} vs ${p2}`;
    document.getElementById("p1").innerHTML = p1;
    document.getElementById("p2").innerHTML = p2;   
    document.getElementById("choice").style.opacity = 0;
    document.getElementById("game").style.opacity = 1;
    document.getElementById("vignette_game").style.opacity = 1;
    Play(0, match, true, [0,0])
};

const Grid_Setup = () => {
    let [w, h] = [window.innerWidth, window.innerHeight];
    const GRID = document.getElementById("grid");
    const GAME = document.getElementById("game");
    if (w >= 2*h) {GAME.style.top = `${0.05 * h}px`; GAME.style.left = `${0.5 * w - 0.9 * h}px`}
    else {
        const TEXT = document.getElementById("text");
        GAME.style.width = "90vw"; GAME.style.height = "45vw"; 
        GRID.style.height = "45vw"; GRID.style.width = "45vw";
        TEXT.style.height = "45vw"; TEXT.style.width = "45vw";
        GAME.style.top = `${0.5 * h - 0.225 * w}px`; GAME.style.left = `${0.05 * w}px`
    };
    for (let i = 0; i < 10; i++) {
        let row = document.createElement("tr");
        row.id = `row_${i}`;
        for (let j = 0; j < 10; j++) {
            let data = document.createElement("td");
            data.id = `data_${i}_${j}`;
            row.appendChild(data)
        };
        GRID.appendChild(row)
    };
    document.getElementById("data_0_0").style.borderTopLeftRadius = "50%";
    document.getElementById("data_9_0").style.borderBottomLeftRadius = "50%";
    Display_Move([0,0], "player_1"); Display_Move([9,9], "player_1");
    Display_Move([9,0], "player_2"); Display_Move([0,9], "player_2")
};

window.onload = () => {
    const LIST = document.getElementById("list");
    const CHOICE = document.getElementById("choice");
    Object.keys(games).forEach(match => {
        let [p1, p2] = match.split("_");
        let e = document.createElement("div");
        e.innerHTML = `- ${p1} vs ${p2}`;
        e.addEventListener("click", () => Choice(match));
        LIST.appendChild(e)
    });
    if (CHOICE.offsetHeight > window.innerHeight) {CHOICE.style.height = "99vh"; CHOICE.style.overflow = "scroll"}
}