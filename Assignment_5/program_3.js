const { consoleRW } = require("./consoleRW");
const cwr = new consoleRW();

async function main() {
    let s = await cwr.get("Enter a string: ");
    let fq = new Array(256).fill(0);
    let p = 0;
    let mx = 0;
    let i = 0;
    
    while (i < s.length) {
        let ci = s.charCodeAt(i);
        if (fq[ci]) {
            mx = Math.max(mx, i - p);
            let cp = s.charCodeAt(p);
            fq[cp] -= 1;
            p += 1;
        } else {
            fq[ci] += 1;
            i += 1;
        }
    }
    console.log(Math.max(mx, i - p));

    cwr.close();
}

main();
