const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

let dp = Array(101).fill().map(() => Array(101).fill(-1));

function dfs(s, idx, cnt) {
    if (idx >= s.length) return cnt === 0;
    if (cnt < 0) return false;

    if (dp[idx][cnt] !== -1) return dp[idx][cnt] === 1;

    let ans = false;

    if (s[idx] === "(") ans = dfs(s, idx + 1, cnt + 1);
    else if (s[idx] === ")") ans = dfs(s, idx + 1, cnt - 1);
    else if (s[idx] === "*") {
        ans =
            dfs(s, idx + 1, cnt + 1) ||
            dfs(s, idx + 1, cnt) ||
            dfs(s, idx + 1, cnt - 1);
    }

    dp[idx][cnt] = ans ? 1 : 0;
    return ans;
}

function checkValidString(s) {
     dp = Array(101).fill().map(() => Array(101).fill(-1));
    return dfs(s, 0, 0);
}

async function main() {
    let str = await cwr.get("Enter a string: ");
    let result = checkValidString(str);
    console.log( result);
    cwr.close();
}

main();
