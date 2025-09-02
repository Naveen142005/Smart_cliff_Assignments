const { consoleRW } = require("./consoleRW");
const crw = new consoleRW();

async function proc() {
    let date = new Date(await crw.get("Enter date:"));

    let st = new Date();
    st.setFullYear(date.getFullYear());
    st.setMonth(0);
    st.setDate(1);

    for (let i = 0; i < 7; i++) {
        if (st.getDay() === 5) {
            break;
        }
        st.setDate(st.getDate() + 1);
    }

    if (date.getMonth() === 0 && date.getDate() <= st.getDate()) {
        console.log(1);
        return;
    }

    let days = 0;
    while (!(st.getFullYear() === date.getFullYear() && st.getMonth() === date.getMonth() && st.getDate() === date.getDate())) {
        days++;
        st.setDate(st.getDate() + 1);
    }

    console.log(Math.floor(days / 7 + 1));
}

async function main() {
    await proc();
    crw.close();
}

main();

