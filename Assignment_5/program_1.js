const { consoleRW } = require ("./consoleRW");
const cwr = new consoleRW();

async function main(){
    let str = await cwr.get("Enter a string: ")
    let flag = 1;
    for (let i = 1; i < str.length; i += 1) {
        if (str[i - 1] == str[i]) {
            flag = 0;
            break;
        }
    }
    if (flag) {
        console.log(str)
        cwr.close()
        return;
    }
    let temp = "", ans = "";

    for (let i = 0; i < str.length; i += 1) {
        if (!temp.length) {
            temp += str[i];
            continue;
        }
        else if (temp[temp.length - 1] == str[i]) temp += str[i];
        else {
            ans += temp[0]
            ans += (temp.length).toString()
            temp = str[i];
        }
    }
    ans += temp[0]
    ans += (temp.length)
    console.log(ans);

    cwr.close()
}

main()
