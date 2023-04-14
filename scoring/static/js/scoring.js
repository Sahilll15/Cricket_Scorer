var currentScoreA = 0;
var currentScoreB = 0;
var currentWicketsA = 0;
var currentWicketsB = 0;
var currentOvers = 0;
var currentBalls = 0;
var maxOvers = 2;
var currentInning = 1;
var Target = 0;

function score(runs) {
    if (currentInning == 1) {
        if (currentOvers >= maxOvers || EndInnings()) {
            targetScore = currentScoreA + 1;
            var targetElement = document.getElementById("Target");
            targetElement.textContent = targetScore;
            alert("Maximum overs reached. Cannot score any more runs.");

            currentInning = 2;
            currentOvers = 0;
            currentBalls = 0;

            return;
        }
        currentScoreA += runs;

        var scoreElement = document.getElementById("team-a-runs");
        scoreElement.textContent = currentScoreA;
    } else if (currentInning == 2) {


        if (currentOvers >= maxOvers || EndInnings()) {
            displayWinner();
            return;
        }
        currentScoreB += runs;
        var scoreElement = document.getElementById("team-b-runs");
        scoreElement.textContent = currentScoreB;
        if (currentScoreB > currentScoreA) {
            alert('team b won')
        }

    }
    updateOver();
    saveState();
}

function wideNoball() {
    if (currentInning == 1) {
        var scoreElement = document.getElementById("team-a-runs");
        var newscore = parseInt(scoreElement.textContent) + 1;
        scoreElement.textContent = newscore;
    } else if (currentInning == 2) {
        var scoreElement = document.getElementById("team-b-runs");
        var newscore = parseInt(scoreElement.textContent) + 1;
        scoreElement.textContent = newscore;
    }
    updateOver();
    saveState();
}

function widenNoball() {
    if (currentInning == 2) {
        var scoreElement = document.getElementById("team-b-runs");
        var newscore = parseInt(scoreElement.textContent) + 1;
        scoreElement.textContent = newscore;
    } else {
        var scoreElement = document.getElementById("team-a-runs");
        var newscore = parseInt(scoreElement.textContent) + 1;
        scoreElement.textContent = newscore;
    }
    saveState();

}

function wicket() {
    if (EndInnings()) {
        return;
    }

    if (currentInning == 1) {
        currentWicketsA += 1;
        var wicketElement = document.getElementById("team-a-wickets");
        wicketElement.textContent = currentWicketsA;
        updateOver();
    } else if (currentInning == 2) {
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
            //   var teamAName = document.getElementById("team-a-name");
            var teamAScore = document.getElementById("team-a-runs");
            var teamAWickets = document.getElementById("team-a-wickets");
            //   teamAName.textContent = "Team B";
            //   teamAScore.textContent = "0";
            //   teamAWickets.textContent = "0";
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
        return;
    } else if (teamBScore > teamAScore) {
        alert(`Team ` + teamBname + ` wins!`);
        return;
    } else {
        alert("The match ended in a tie!");
    }
    saveState();
}

function displayBWinner() {
    var teamBname = document.getElementById("team-b-name").textContent;
    if (teamBScore > teamAScore) {
        alert("Team" + teamBname + "wins!");
    }
    saveState();
}

function saveState() {
    localStorage.setItem('currentScoreA', currentScoreA);
    localStorage.setItem('currentScoreB', currentScoreB);
    localStorage.setItem('currentWicketsA', currentWicketsA);
    localStorage.setItem('currentWicketsB', currentWicketsB);
    localStorage.setItem('currentOvers', currentOvers);
    localStorage.setItem('currentBalls', currentBalls);
    localStorage.setItem('maxOvers', maxOvers);
    localStorage.setItem('currentInning', currentInning);
    localStorage.setItem('Target', Target);
}

function loadState() {
    currentScoreA = parseInt(localStorage.getItem('currentScoreA')) || 0;
    currentScoreB = parseInt(localStorage.getItem('currentScoreB')) || 0;
    currentWicketsA = parseInt(localStorage.getItem('currentWicketsA')) || 0;
    currentWicketsB = parseInt(localStorage.getItem('currentWicketsB')) || 0;
    currentOvers = parseFloat(localStorage.getItem('currentOvers')) || 0;
    currentBalls = parseInt(localStorage.getItem('currentBalls')) || 0;
    maxOvers = parseInt(localStorage.getItem('maxOvers')) || 2;
    currentInning = parseInt(localStorage.getItem('currentInning')) || 1;
    Target = parseInt(localStorage.getItem('Target')) || 0;

    // Update UI with loaded state
    document.getElementById('team-a-runs').textContent = currentScoreA;
    document.getElementById('team-b-runs').textContent = currentScoreB;
    document.getElementById('team-a-wickets').textContent = currentWicketsA;
    document.getElementById('team-b-wickets').textContent = currentWicketsB;
    document.getElementById('overs').textContent = 'From ' + currentBalls / 6 + '/' + currentOvers + ' Overs';
    document.getElementById('Target').textContent = Target;
}

// Call loadState function when page loads
window.onload = loadState;