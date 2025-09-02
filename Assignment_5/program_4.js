const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter a Array: example ->[1,2,3,4]\n");
    let arr = JSON.parse(s)
    let sz = arr.length;
    let left = Array(sz);
    let right = Array(sz);

    left[0] = arr[0];
    right[sz - 1] = arr[sz - 1];
    let i = 1, j = sz - 2;
    while (i < sz) {
        left[i] = left[i - 1] * arr[i];
        right[j] = right[j + 1] * arr[j];
        i += 1;
        j -= 1;
    }
    let ans = Array(sz);
    ans.fill(1)
    i = 0;
    while (i < sz) {
        if (i - 1 >= 0) ans[i] = left[i - 1];
        if (i + 1 < sz) ans[i] *= right[i + 1];
        i += 1
    }
    console.log(ans);
    cwr.close();
}

main();
