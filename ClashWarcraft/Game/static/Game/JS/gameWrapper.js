import * as ajax from "./ajax.js";

export async function reduceCooldown(cardName) {
    let parameters = {
        cardName : cardName,
    }
    await ajax.makeRequest('POST', '/api/reduce-cooldown', JSON.stringify(parameters)); 
}