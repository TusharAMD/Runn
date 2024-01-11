let firstCar = document.getElementById("first-car");
let secondCar = document.getElementById("second-car");
let result = document.getElementById("result")
const score =  document.getElementById("score")
let game =  document.getElementById("game");
let counter = 0;



// TRAFFIC MOVE

firstCar.addEventListener("animationiteration", function(){
    var random = ((Math.floor(Math.random() * 3)) * 165)
    firstCar.style.left = random + "px";
    counter++
})

//RACE CAR MOVE

window.addEventListener("keydown", function(e){
   if(e.keyCode == "39"){ var secondCarLeft = parseInt(window.getComputedStyle(secondCar).getPropertyValue("left"))
    if(secondCarLeft < 260){secondCar.style.left = (secondCarLeft + 165) + "px"}
};

    if(e.keyCode == "37"){
        var secondCarLeft = parseInt(window.getComputedStyle(secondCar).getPropertyValue("left"))
        if(secondCarLeft > 0){secondCar.style.left = (secondCarLeft - 165) + "px"
    }

    }
})


//GAME OVER

setInterval(function Gameover (){
    let firstCarTop = parseInt(window.getComputedStyle(firstCar).getPropertyValue("top"))
    let firstCarLeft = parseInt(window.getComputedStyle(firstCar).getPropertyValue("left"));
    let secondCarLeft = parseInt(window.getComputedStyle(secondCar).getPropertyValue("left"));
        if((firstCarLeft === secondCarLeft) && (firstCarTop > 250) && (firstCarTop < 450)){
            result.style.display = "block";
            game.style.display = "none";
            score.innerHTML = `score: ${counter} `;

            counter = 0;
        }
}, 10)