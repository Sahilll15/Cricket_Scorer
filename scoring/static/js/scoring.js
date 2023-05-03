var currentScoreA = 0;
var currentScoreB = 0;
var currentWicketsA = 0;
var currentWicketsB = 0;
var currentOvers = 0;
var currentBalls = 0;
var maxOvers = document.getElementById("Overs").textContent;
var currentInning = 1;
var Target = 0;


function score(runs) {

    if (currentInning == 1) {
        var batsmanSelect = document.getElementById("batsman-select-a");
        var selectedBatsman = batsmanSelect.value;
        if (selectedBatsman === "") {
            alert("select a Batsmen");
            return;
        }
        var selectedBatsmanRow = document.querySelector(`.batter-row[data-batter-name="${selectedBatsman}"]`);
        if (selectedBatsmanRow === "") {
            alert("select a batsmen");
            return;
        }
        var bolwerSelect = document.getElementById("bowler-select-a");
        var selectedBowler = bolwerSelect.value;
        var selectedBowlerRow = document.querySelector(`.bowler-row[data-bowler-name="${selectedBowler}"]`);
        if (currentOvers >= maxOvers || EndInnings()) {
            targetScore = currentScoreA + 1;
            var targetElement = document.getElementById("Target");
            targetElement.textContent = targetScore;
            var teamAname = document.getElementById("team-a-name").textContent;
            alert(`The ` + teamAname + `Innings has Ended!`);

            currentInning = 2;
            currentOvers = 0;
            currentBalls = 0;

            return;
        }

        currentScoreA += runs;

        var scoreElement = document.getElementById("team-a-runs");
        scoreElement.textContent = currentScoreA;
        //update bowler stats
        selectedBowlerRow.querySelector(".bowler-runs").textContent = parseInt(selectedBowlerRow.querySelector(".bowler-runs").textContent) + runs;
        selectedBowlerRow.querySelector(".bowler-overs").textContent = getOversBowled(currentBalls);

        // Update selected batsman stats
        selectedBatsmanRow.querySelector(".batter-runs").textContent = parseInt(selectedBatsmanRow.querySelector(".batter-runs").textContent) + runs;
        selectedBatsmanRow.querySelector(".balls-faced").textContent = parseInt(selectedBatsmanRow.querySelector(".balls-faced").textContent) + 1;

        if (runs == 4) {
            selectedBatsmanRow.querySelector(".fours").textContent = parseInt(selectedBatsmanRow.querySelector(".fours").textContent) + 1;
        } else if (runs == 6) {
            selectedBatsmanRow.querySelector(".sixes").textContent = parseInt(selectedBatsmanRow.querySelector(".sixes").textContent) + 1;
        }

        var ballsFaced = parseInt(selectedBatsmanRow.querySelector(".balls-faced").textContent);
        var batterRuns = parseInt(selectedBatsmanRow.querySelector(".batter-runs").textContent);
        var strikeRate = (batterRuns / ballsFaced) * 100;
        selectedBatsmanRow.querySelector(".strike-rate").textContent = strikeRate.toFixed(2);
    } if (currentInning == 2) {

        var bowlerselect = document.getElementById("bowler-select-b");
        var selectedBowlerB = bowlerselect.value;

        var selectedBowlerRowB = document.querySelector(`.bowler-row-b[data-bowler-name="${selectedBowlerB}"]`);
        selectedBowlerRowB.querySelector(".bowler-runs").textContent = parseInt(selectedBowlerRowB.querySelector(".bowler-runs").textContent) + runs;
        selectedBowlerRowB.querySelector(".bowler-overs").textContent = getOversBowled(currentBalls);

        if (currentOvers >= maxOvers || EndInnings()) {
            displayWinner();

        }

        currentScoreB += runs;
        var scoreElement = document.getElementById("team-b-runs")
        scoreElement.textContent = currentScoreB;
        var teamBname = document.getElementById("team-b-name").textContent;

        if (currentScoreB > currentScoreA) {
            alert("Team " + teamBname + " wins!");
        }
        var batsmanSelect = document.getElementById("batsman-select-b");

        var selectedBatsman = batsmanSelect.value;
        if (selectedBatsman === "") {
            alert("select a Batsmen");
            return;
        }
        //update bowler statss
        if (selectedBatsmanRow === "") {
            alert("select a batsmen");
            return;
        }

        // Update selected batsman stats for team B
        var selectedBatsmanRowB = document.querySelector(`.batter-row-b[data-batter-name="${selectedBatsman}"][data-team="B"]`);
        selectedBatsmanRowB.querySelector(".batter-runs").textContent = parseInt(selectedBatsmanRowB.querySelector(".batter-runs").textContent) + runs;
        selectedBatsmanRowB.querySelector(".balls-faced").textContent = parseInt(selectedBatsmanRowB.querySelector(".balls-faced").textContent) + 1;

        if (runs == 4) {
            selectedBatsmanRowB.querySelector(".fours").textContent = parseInt(selectedBatsmanRowB.querySelector(".fours").textContent) + 1;
        } else if (runs == 6) {
            selectedBatsmanRowB.querySelector(".sixes").textContent = parseInt(selectedBatsmanRowB.querySelector(".sixes").textContent) + 1;
        }
        var ballsFaced = parseInt(selectedBatsmanRowB.querySelector(".balls-faced").textContent);
        var batterRuns = parseInt(selectedBatsmanRowB.querySelector(".batter-runs").textContent);
        var strikeRate = (batterRuns / ballsFaced) * 100;
        selectedBatsmanRowB.querySelector(".strike-rate").textContent = strikeRate.toFixed(2);
    }

    updateOver();
    saveState();
}
var isOverComplete = false;

function getOversBowled(balls) {
    var overs = Math.floor(balls / 7);
    var ballsInOver = balls % 6 + 1;
    if (ballsInOver >= 6) {
        overs += 1;
        ballsInOver = 0; // set isOverComplete to true if the current over is complete
        alert("Change the bowler");
    }
    return overs + "." + ballsInOver;
}

const selectElement = document.getElementById('bowler-select-a');
let selectedBowlerName = null; // variable to store the selected bowler name

selectElement.addEventListener('change', handleSelectChange);

function handleSelectChange(event) {
    if (isOverComplete) {
        selectElement.style.display = 'block'; // show the select element if the over is complete
        selectedBowlerName = event.target.value; // store the selected bowler name
        isOverComplete = false; // reset isOverComplete to false when a new bowler is selected
    } else {
        alert("YOU CANNOT SELECT ANOTHER BOWLER IN BETWWEEN THE Over")// set the selected bowler back to the previous selection
    }
}

function completeOver() {
    // ...code to complete the over
    selectElement.style.display = 'none'; // hide the select element until the over is completed
    isOverComplete = true; // set isOverComplete to true when the over is completed
}





function widenNoball() {
    if (currentInning == 2) {
        var scoreElement = document.getElementById("team-b-runs");
        var newscore = parseInt(scoreElement.textContent) + 2;
        var bowlerselect = document.getElementById("bowler-select-b");
        var selectedBowlerB = bowlerselect.value;
        var selectedBowlerRowB = document.querySelector(`.bowler-row-b[data-bowler-name="${selectedBowlerB}"]`);
        scoreElement.textContent = newscore;
        selectedBowlerRowB.querySelector(".bowler-runs").textContent = parseInt(selectedBowlerRowB.querySelector(".bowler-runs").textContent) + 1;
        var runs = prompt("Enter the number of runs scored on the wide ball");
        if (runs === null) {
            return
        }
        runs = parseInt(runs);
        if (isNaN(runs) || runs < 0) {
            alert("Invalid input!");
            return;
        }


        currentScoreB += runs;
        var scoreElement = document.getElementById("team-b-runs");
        scoreElement.textContent = currentScoreB;




    } else {

        var runs = prompt("Enter the number of runs scored on the wide ball");
        if (runs === null) {
            return
        }
        runs = parseInt(runs);
        if (isNaN(runs) || runs < 0) {
            alert("Invalid input!");
            return;
        }

        var scoreElement = document.getElementById("team-a-runs");
        var newscore = parseInt(scoreElement.textContent) + 1;
        scoreElement.textContent = newscore;
        var bolwerSelect = document.getElementById("bowler-select-a");
        var selectedBowler = bolwerSelect.value;
        var selectedBowlerRow = document.querySelector(`.bowler-row[data-bowler-name="${selectedBowler}"]`);
        selectedBowlerRow.querySelector(".bowler-runs").textContent = parseInt(selectedBowlerRow.querySelector(".bowler-runs").textContent) + 1;


        currentScoreA += runs;
        var scoreElement = document.getElementById("team-a-runs");
        scoreElement.textContent = currentScoreA + 1;
    }

    saveState();

}

function wicket(currentInning) {
    if (EndInnings()) {
        return;
    }


    if (currentInning == 1) {


        var bolwerSelect = document.getElementById("bowler-select-a");
        var selectedBowler = bolwerSelect.value;
        var selectedBowlerRow = document.querySelector(`.bowler-row[data-bowler-name="${selectedBowler}"]`);

        currentWicketsA += 1;
        var wicketElement = document.getElementById("team-a-wickets");
        wicketElement.textContent = currentWicketsA;
        selectedBowlerRow.querySelector(".bowler-wickets").textContent = parseInt(selectedBowlerRow.querySelector(".bowler-wickets").textContent) + 1;
        selectedBowlerRow.querySelector(".bowler-overs").textContent = getOversBowled(currentBalls);
        updateOver();
    } else if (currentInning == 2) {



        var bolwerSelect = document.getElementById("bowler-select-b");
        var selectedBowlerB = bolwerSelect.value;
        var selectedBowlerRowB = document.querySelector(`.bowler-row-b[data-bowler-name="${selectedBowlerB}"]`);
        selectedBowlerRowB.querySelector(".bowler-wickets").textContent = parseInt(selectedBowlerRowB.querySelector(".bowler-wickets").textContent) + 1;
        selectedBowlerRowB.querySelector(".bowler-overs").textContent = getOversBowled(currentBalls);

        currentWicketsB += 1;
        var wicketElement = document.getElementById("team-b-wickets");
        wicketElement.textContent = currentWicketsB;

        updateOver();
    }

    EndInnings();
    saveState();
}

function EndInnings() {
    var wicketElement = document.getElementById("team-a-wickets");
    var wickets = parseInt(wicketElement.textContent);
    if (wickets >= 10 || currentOvers > maxOvers) {
        alert(`This innings has ended`)
        if (currentInning == 1) {
            currentInning = 2;

            var teamAScore = document.getElementById("team-a-runs");
            var teamAWickets = document.getElementById("team-a-wickets");

            var teamBName = document.getElementById("team-b-name");
            teamBName.style.fontWeight = "bold";
            var oversElement = document.getElementById("overs");
            oversElement.textContent = "From 0/0 Overs";
        } else {
            displayWinner();
        }

    }
    saveState();
}

function updateOver() {
    if (currentOvers < maxOvers) {

        if (currentBalls < 5) {
            currentBalls += 1;
            var overElement = document.getElementById("overs");
            var overString = "From " + "0." + (currentBalls) + "/" + currentOvers + ".0" + " Overs";
            overElement.textContent = overString;
        } else {
            currentBalls = 0;
            currentOvers += 1;
            var overElement = document.getElementById("overs");
            var overString = "From " + "0." + (currentBalls) + "/" + currentOvers + ".0" + " Overs";
            overElement.textContent = overString;
        }
    } else {
        EndInnings();
        if (currentInning == 2) {
            displayWinner();
        }
    }
    saveState();
}

function displayWinner() {
    var teamAScore = currentScoreA;
    var teamBScore = currentScoreB;
    var teamAname = document.getElementById("team-a-name").textContent;
    var teamBname = document.getElementById("team-b-name").textContent;

    if (teamAScore > teamBScore) {
        alert(`Team ` + teamAname + ` wins!`);
        document.getElementById("winner_id").textContent = teamAname;
    } else if (teamBScore > teamAScore) {
        alert(`Team ` + teamBname + ` wins!`);
        document.getElementById("winner_id").textContent = teamBname;
    } else {
        alert("The match ended in a tie!");
        document.getElementById("winner_id").textContent = "Tie";
    }
    saveState();
}

function legbyes() {
    var runs = prompt("Enter the number of runs");
    if (runs === null) {
        return
    }
    runs = parseInt(runs);
    if (isNaN(runs) || runs < 0) {
        alert("Invalid input!");
        return;
    }

    if (currentInning == 1) {
        currentScoreA += runs;

        var scoreElement = document.getElementById("team-a-runs");
        scoreElement.textContent = currentScoreA;
    }
    if (currentInning == 2) {
        currentScoreB += runs;

        var scoreElement = document.getElementById("team-b-runs");
        scoreElement.textContent = currentScoreB;
    }



}






function displayBWinner() {
    var teamBname = document.getElementById("team-b-name").textContent;
    if (teamBScore > teamAScore) {
        alert("Team" + teamBname + "wins!");
    }
    saveState();
}

// function saveState() {
//     localStorage.setItem('currentScoreA', currentScoreA);
//     localStorage.setItem('currentScoreB', currentScoreB);
//     localStorage.setItem('currentWicketsA', currentWicketsA);
//     localStorage.setItem('currentWicketsB', currentWicketsB);
//     localStorage.setItem('currentOvers', currentOvers);
//     localStorage.setItem('currentBalls', currentBalls);
//     localStorage.setItem('maxOvers', maxOvers);
//     localStorage.setItem('currentInning', currentInning);
//     localStorage.setItem('Target', Target);
// }

// function loadState(matchId) {
//     var storedMatchId = localStorage.getItem('matchId');
//     if (storedMatchId && storedMatchId !== matchId.toString()) {
//         localStorage.clear();
//     }
//     localStorage.setItem('matchId', matchId);

//     currentScoreA = parseInt(localStorage.getItem('currentScoreA')) || 0;
//     currentScoreB = parseInt(localStorage.getItem('currentScoreB')) || 0;
//     currentWicketsA = parseInt(localStorage.getItem('currentWicketsA')) || 0;
//     currentWicketsB = parseInt(localStorage.getItem('currentWicketsB')) || 0;
//     currentOvers = parseFloat(localStorage.getItem('currentOvers')) || 0;
//     currentBalls = parseInt(localStorage.getItem('currentBalls')) || 0;
//     maxOvers = parseInt(localStorage.getItem('maxOvers')) || 2;
//     currentInning = parseInt(localStorage.getItem('currentInning')) || 1;
//     Target = parseInt(localStorage.getItem('Target')) || 0;

//     // Update UI with loaded state
//     document.getElementById('team-a-runs').textContent = currentScoreA;
//     document.getElementById('team-b-runs').textContent = currentScoreB;
//     document.getElementById('team-a-wickets').textContent = currentWicketsA;
//     document.getElementById('team-b-wickets').textContent = currentWicketsB;
//     document.getElementById('overs').textContent = 'From ' + currentBalls / 6 + '/' + currentOvers + ' Overs';
//     document.getElementById('Target').textContent = Target;
// }


// var matchId = document.getElementById('Matchid').getAttribute('data-match-id');
// loadState(matchId);

// Call loadState function when page loads
// window.onload = loadState;


// Call loadState function when page loads
// window.onload = loadState;


function saveState() {

};