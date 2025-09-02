const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter a 2D Array: ");
    let arr = JSON.parse(s);
    let ans = []
    let m = arr.length;
    let n = arr[0].length;

    k = 0, l = 0, r = m - 1, p = n - 1
    while (k <= r && l <= p ) {
        for (let i = l; i <= p; i += 1)
            ans.push(arr[k][i])
        k += 1;

        for (let i = k; i <= r; i += 1) 
            ans.push(arr[i][p]);
        p -= 1;

        if (k <= r) {
            for (let i = p; i >= l; i -= 1)
                ans.push(arr[r][i])
            r-= 1
        }

        if (l <= p) {
            for (let i = r; i >= k; i -= 1)
                ans.push(arr[i][l])
            l += 1
        }

    }
    console.log(ans);
    

    cwr.close();
}

main();
