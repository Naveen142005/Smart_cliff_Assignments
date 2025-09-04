import {addToCart, calculateTotal, applyDiscount, cart} from './cartUtils.js';

let item1 = { name: "Laptop", price: 1000 };
let item2 = { name: "Phone", price: 500 };

console.log(addToCart(item1));
console.log(addToCart(item2));

let total = calculateTotal(cart);
console.log(`Total: $${total}`);
let discountedTotal = applyDiscount(total, 10);
console.log(`Total after discount: $${discountedTotal}`);
