let count = 0;


function cc(card) {
    if (card >= 2 && card <= 6) { 
        count += 1;
    }
    else if (card >= 7 && card <= 9 ) { 
        count += 0;
    } 
    else { 
        count -= 1; 
    }
    if (count > 0 ) { 
        return count + " Bet";
    } else { 
        return count + " Hold";
    }

}

console.log(cc(2));
console.log(cc("J"));
console.log(cc(9));
console.log(cc(2));
console.log(cc(7));
