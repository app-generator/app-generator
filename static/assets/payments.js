// Get Stripe publishable key
fetch("/payments/config/")
  .then((result) => { return result.json(); })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);
    // Event handler for all Buy Now buttons
    document.querySelectorAll(".buy-now-btn").forEach((button) => {
      button.addEventListener("click", () => {
        var product = button.dataset.productId;

        // Get Checkout Session ID
        fetch("/payments/create-checkout-session/" + product)
          .then((result) => { return result.json(); })
          .then((data) => {
            console.log(data);
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({ sessionId: data.sessionId })
          })
          .then((res) => {
            console.log(res);
          });
      });
    });
  });
