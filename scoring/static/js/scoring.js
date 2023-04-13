
var currentOver=0;
var currentBall=0;
var maxOvers=2;
function score(runs){
    if (currentOver >= maxOvers) {
        alert("Maximum overs reached. Cannot score any more runs.");
        return;
    }
    var scoreElement=document.getElementById("team-a-runs");
    var newscore=parseInt(scoreElement.textContent)+runs;
    if(EndInnigs()){
        alert("The innings is over you cannot score")
        return;
    }
    
    updateOver();

    scoreElement.textContent=newscore;
    
}




function widenNoball(){
    var scoreElement=document.getElementById("team-a-runs");
    var newscore=parseInt(scoreElement.textContent)+1;

    scoreElement.textContent=newscore;

}

function wicket(){
    if(EndInnigs()){
        return ;
    }
    
    var wicketElement=document.getElementById("team-a-wickets");
    var newwickets=parseInt(wicketElement.textContent)+1;

    wicketElement.textContent=newwickets;
}

function EndInnigs(){
    var wicketElement=document.getElementById("team-a-wickets");
    var wickets=parseInt(wicketElement.textContent);
    if (wickets ===10) {
        alert("Innings is over");
        currentOver=0;
        currentOver=0;
        return true;
    }

    return false;
}
function updateOver() {
    if (currentOver < maxOvers) {
        currentBall++;
        if (currentBall > 6) {
            currentBall = 1;
            currentOver++;
        }
    } 
    else {
        alert("The innings has ended")
        return;
    }

    var overElement = document.getElementById("overs");
    overElement.textContent = "From " + "0." + (currentBall-1) + "/" + currentOver+".0" + " Overs";
    if (currentOver >= maxOvers) {
        alert("Maximum overs reached. Cannot score any more runs.");
    }
}
