const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter a 2D Array: ");
    let arr = JSON.parse(s)

    arr.sort((a , b) => a[0] - b[0])

    let st = arr[0][0]
    let end = arr[0][1]
    let ans = []

    for (let i = 1; i < arr.length; i += 1) {
        if (arr[i][0] <= end)
            end = Math.max(arr[i][1], end);
        else{
            ans.push([st, end])
            st = arr[i][0]
            end = arr[i][1]
        }
    }
    ans.push([st, end])
    console.log(ans)
    cwr.close();
}

main();
