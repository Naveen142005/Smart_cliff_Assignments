function data() {
    let st = 1;

    return {
        next() {
            let temp = st + 10;
            let arr = []
            while (st < temp)
                arr.push(st++)
            return {
                value: arr
            };
        }
    }

}
const fun = data()

console.log(fun.next().value);
console.log(fun.next().value);
console.log(fun.next().value);
console.log(fun.next().value);
