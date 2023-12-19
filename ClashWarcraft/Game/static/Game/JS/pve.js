var threats = {};

export function computerPlay() {
    console.log(threats);
}

export function initializeThreats(cardsName) {
    let mobsNumber = [1,3,5,7];
    let playNumber = [0,2,4,6];

    // Generate a table of threats each play has for each mob.
    for (let i = 0; i < mobsNumber.length; i++) {
        let mob = cardsName[mobsNumber[i]];
        threats[mob] = {};
        for (let j = 0; j < playNumber.length; j++) {
            let character = cardsName[playNumber[j]];
            threats[mob][character] = 0;
        }
    }
}