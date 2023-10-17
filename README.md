# Flask Web application and stripe
```markdown
# Flask Stripe Checkout Example

A basic web application built with Flask and Stripe to demonstrate a simple payment integration using Stripe Checkout.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3
- Flask (`pip install Flask`)
- Stripe Python library (`pip install stripe`)

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/flask-stripe-checkout.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-stripe-checkout
   ```

3. Set your Stripe API keys as environment variables. You'll need to set both your publishable and secret keys.

   ```bash
   export STRIPE_PUBLISHABLE_KEY=your_publishable_key
   export STRIPE_SECRET_KEY=your_secret_key
   ```

4. Run the Flask application:

   ```bash
   flask run
   ```

5. Open a web browser and visit `http://127.0.0.1:5000` to access the application.

## Usage

- The homepage displays a simple payment form with a "Pay $5.00" button.
- Click the button to initiate a payment using Stripe Checkout.
- You'll be redirected to a Stripe-hosted payment page to complete the transaction.
- After successful payment, you'll be redirected to a confirmation page.

## Project Structure

- `app.py`: The main Flask application file that defines routes and integrates with Stripe.
- `templates/`: This directory contains HTML templates for rendering pages.
- `layout.html`: The base HTML template that provides the structure for all pages.
- `index.html`: The template for the payment form.
- `charge.html`: The template for displaying a payment confirmation message.

## Customization

You can customize this application to fit your specific needs. For example, you can change the payment amount, add more features, or style the templates to match your branding.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Stripe](https://stripe.com) for providing a secure and reliable payment processing service.
- [Flask](https://flask.palletsprojects.com/) for creating a lightweight and flexible web application framework.

## Author

[Kenneth] [Mburu]

Feel free to contact me at [your@email.com] if you have any questions or need assistance.
```

