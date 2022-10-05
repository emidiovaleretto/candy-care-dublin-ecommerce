let stripePublicKey = $('#id_stripe_publishable_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret_key').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

let style = {
    base: {
        background: '#FFF',
        color: '#000',
        fontFamily: 'Roboto, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        },
        fontWeight: '400',
        lineHeight: '1.5',
        padding: '16px',
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

let card = elements.create('card', {
    style: style
});

card.mount('#card-element');