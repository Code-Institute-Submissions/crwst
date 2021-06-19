/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
      color: "#32325d",
      fontFamily: 'Roboto Mono, monospace',
      fontSmoothing: "antialiased",
      fontSize: "16px",
      "::placeholder": {
        color: "#32325d"
      }
    },
    invalid: {
      fontFamily: 'Roboto Mono, monospace',
      fontSmoothing: "antialiased",
      fontSize: "16px",
      color: "#dc5345",
      iconColor: "#dc5345"
    }
};

var card = elements.create('card', {style: style});

card.mount('#card-element');




