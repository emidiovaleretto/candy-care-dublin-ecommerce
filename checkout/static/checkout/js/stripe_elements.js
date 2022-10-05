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

// The function below handles realtime validation errors on the card element

card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

let form = document.getElementById('payment-form');

// The function below handles the form submition

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
