function status_(flightNumber) {
    return new Promise((res, rej) => {
        setTimeout(() => {
            if (flightNumber == "AI202") res(`${flightNumber} is On Time`);
            else if (flightNumber == "AI404") res(`${flightNumber} is delayed`);
            else rej("Flight not found.");
        }, 2000);
    });
}

async function getFlightStatus(flightNO) {
    console.log("Searching results....");
    try {
        const res = await status_(flightNO);
        console.log(res);
    }
    catch (e) {
        console.log(e);
    }
}

async function run() {
    await getFlightStatus("AI202");
    await getFlightStatus("AI404");
    await getFlightStatus("AI239");
}

run();

