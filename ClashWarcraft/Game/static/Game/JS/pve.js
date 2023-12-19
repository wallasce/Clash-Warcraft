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

export function increaseThreat(playerToIncrease, typePlayer, mobThreat = null) {
    // Value to increase threat depends of card Type
    const valueToIncrease = {
        0 : 4,
        2 : 2,
        4 : 3,
        6 : 1,
    };

    if (mobThreat) {
        threats[mobThreat][playerToIncrease] += valueToIncrease[typePlayer];
    } else {
        for (const [key, value] of Object.entries(threats)) {
            threats[key][playerToIncrease] += valueToIncrease[typePlayer]
        }
    }
}