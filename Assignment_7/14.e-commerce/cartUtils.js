export let cart = [];

export function addToCart(item) {
    cart.push(item);
    return `Success fully added`
}

export function calculateTotal(cart) {
    let sum = 0;
    cart.forEach(element => {
        sum += element.price;
    });

    return sum;
}

export function applyDiscount(total, discount) {
    return total - (total * (discount / 100));
}
