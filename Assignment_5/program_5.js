const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {

    let s = await cwr.get("Enter a Array: example ->[1,2,3,4]\n");
    let k = await cwr.get("Enter k:")
    let arr = JSON.parse(s)
    let sz = arr.length;

    let mp = { 0: 1 };
    let sum = 0;
    let cnt = 0;
    for (let i = 0; i < sz; i += 1) {
        sum += arr[i];

        if (mp[sum - k]) {
            cnt += mp[sum - k];
        }
        if (mp[sum])
            mp[sum] += 1;
        else {
            mp[sum] = 1
        }

    }
    console.log(cnt);


    cwr.close();
}

main();
