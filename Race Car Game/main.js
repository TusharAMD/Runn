let firstCar = document.getElementById("first-car");

// First CAR move

firstCar.addEventListener("animationiteration", function(){
    let random = ((Math.floor(Math.random() *3)) * 140)
    firstCar.style.left = random + "px"
})