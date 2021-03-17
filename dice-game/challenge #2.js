/*
GAME RULES:
- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game
*/

/*

let scores, reoundScore, activeplayer, gamePlaying; /*,dice ;
init();
gamePlaying = true;

document.querySelector(".btn-roll").addEventListener("click", () => {
  if (gamePlaying) {
    //1.random number
    let dice = Math.floor(Math.random() * 6) + 1;
    //2.display the result
    let diceDOM = document.querySelector(".dice");
    diceDOM.style.display = "block";
    diceDOM.src = `dice-${dice}.png`;
    //3.update the score ,but if only if the number NOT 1
    if (dice !== 1) {
      reoundScore += dice;
      document.querySelector(
        `#current-${activeplayer}`
      ).textContent = reoundScore;
    } else {
      NextPlayer();
    }
  }
});

//hold butn
document.querySelector(".btn-hold").addEventListener("click", () => {
  if (gamePlaying) {
    //add current score
    scores[activeplayer] += reoundScore;

    //update the UI
    document.querySelector(`#score-${activeplayer}`).textContent =
      scores[activeplayer];
    //check if the player win the game
    if (scores[activeplayer] >= 20) {
      document.querySelector(`#name-${activeplayer}`).textContent = "Winner!";
      document.querySelector(".dice").style.display = "none";

      document
        .querySelector(`.player-${activeplayer}-panel`)
        .classList.add("winner");
      document
        .querySelector(`.player-${activeplayer}-panel`)
        .classList.remove("active");
      gamePlaying = false;
    } else {
      NextPlayer();
    }
  }
});

document.querySelector(".btn-new").addEventListener("click", init);

function NextPlayer() {
  activeplayer === 0 ? (activeplayer = 1) : (activeplayer = 0);
  reoundScore = 0;
  gamePlaying = true;
  document.getElementById(`current-0`).textContent = "0";
  document.getElementById(`current-1`).textContent = "0";

  document.querySelector(".player-0-panel").classList.toggle("active");
  document.querySelector(".player-1-panel").classList.toggle("active");

  document.querySelector(".dice").style.display = "none";
}

function init() {
  scores = [0, 0];
  reoundScore = 0;
  activeplayer = 0;

  document.querySelector(`.dice`).style.display = "none";

  document.getElementById("score-0").textContent = "0";
  document.getElementById("score-1").textContent = "0";
  document.getElementById("current-0").textContent = "0";
  document.getElementById("current-1").textContent = "0";

  document.getElementById(`name-0`).textContent = "player 1";
  document.getElementById(`name-1`).textContent = "player 1";
  document.querySelector(".player-0-panel").classList.remove("active");
  document.querySelector(".player-1-panel").classList.remove("active");
  document.querySelector(".player-0-panel").classList.remove("winner");
  document.querySelector(".player-1-panel").classList.remove("winner");
  document.querySelector(".player-0-panel").classList.add("active");
}

//dice = Math.floor(Math.random() * 6) + 1;

//document.querySelector(`#current-${activeplayer}`).textContent = dice;
//document.querySelector(`#current-${activeplayer}`).innerHTML ='<em>' + dice + '</em>'

//let x = document.querySelector("#score-0").textContent;

//console.log(x);
*/

/*
1. player looses when roll 2 6 dice in row will go to the other player turn
(Hint : always save the last score in seperate var)
2.add input faild when the player can set the winning score
(Hint: you can read that var with  the .value property in javascript use google)
3.add onther dice
*/

let scores, reoundScore, activeplayer, gamePlaying, lastDice; /*,dice ;*/
init();
gamePlaying = true;

document.querySelector(".btn-roll").addEventListener("click", () => {
  if (gamePlaying) {
    //1.random number
    let dice = Math.floor(Math.random() * 6) + 1;
    //2.display the result
    let diceDOM = document.querySelector(".dice");
    diceDOM.style.display = "block";
    diceDOM.src = `dice-${dice}.png`;
    //challenge 1 : i lose
    if (dice === 6 && lastDice === 6) {
      scores[activeplayer] = 0;
      document.querySelector("#score-" + activeplayer).textContent = "0";
      NextPlayer();
    }
    //3.update the score ,but if only if the number NOT 1

    if (dice !== 1) {
      reoundScore += dice;
      document.querySelector(
        `#current-${activeplayer}`
      ).textContent = reoundScore;
    } else {
      NextPlayer();
    }
    lastDice = dice;
  }
});

//hold butn
document.querySelector(".btn-hold").addEventListener("click", () => {
  if (gamePlaying) {
    //add current score
    scores[activeplayer] += reoundScore;

    //update the UI
    document.querySelector(`#score-${activeplayer}`).textContent =
      scores[activeplayer];

    //challenge 2
    let UserSCore = document.querySelector(".Scoree").value;
    let WinningScore;
    if (UserSCore) {
      WinningScore = UserSCore;
    } else {
      WinningScore = 10;
    }
    //check if the player win the game
    if (scores[activeplayer] >= WinningScore) {
      document.querySelector(`#name-${activeplayer}`).textContent = "Winner!";
      document.querySelector(".dice").style.display = "none";

      document
        .querySelector(`.player-${activeplayer}-panel`)
        .classList.add("winner");
      document
        .querySelector(`.player-${activeplayer}-panel`)
        .classList.remove("active");
      gamePlaying = false;
    } else {
      NextPlayer();
    }
  }
});

document.querySelector(".btn-new").addEventListener("click", init);

function NextPlayer() {
  activeplayer === 0 ? (activeplayer = 1) : (activeplayer = 0);
  reoundScore = 0;
  gamePlaying = true;
  document.getElementById(`current-0`).textContent = "0";
  document.getElementById(`current-1`).textContent = "0";

  document.querySelector(".player-0-panel").classList.toggle("active");
  document.querySelector(".player-1-panel").classList.toggle("active");

  document.querySelector(".dice").style.display = "none";
}

function init() {
  scores = [0, 0];
  reoundScore = 0;
  activeplayer = 0;
  gamePlaying = true;
  document.querySelector(`.dice`).style.display = "none";

  document.getElementById("score-0").textContent = "0";
  document.getElementById("score-1").textContent = "0";
  document.getElementById("current-0").textContent = "0";
  document.getElementById("current-1").textContent = "0";

  document.getElementById(`name-0`).textContent = "player 1";
  document.getElementById(`name-1`).textContent = "player 1";
  document.querySelector(".player-0-panel").classList.remove("active");
  document.querySelector(".player-1-panel").classList.remove("active");
  document.querySelector(".player-0-panel").classList.remove("winner");
  document.querySelector(".player-1-panel").classList.remove("winner");
  document.querySelector(".player-0-panel").classList.add("active");
}
