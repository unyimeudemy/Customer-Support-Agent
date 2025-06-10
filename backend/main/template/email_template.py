html_template = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <style>
    .container {
    max-width: 600px;
    margin: auto;
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 30px;
    font-family: Arial, sans-serif;
    }
    .header {
    background-color: #4CAF50;
    padding: 20px;
    color: white;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    text-align: center;
    }
    .content {
    margin-top: 20px;
    }
    .footer {
    margin-top: 30px;
    font-size: 12px;
    color: #888;
    text-align: center;
    }
    </style>
    </head>
    <body style="background-color: #f5f5f5; padding: 20px;">
    <div class="container">
    <div class="header">
    <h1>Welcome, {{ name }}!</h1>
    </div>
    <div class="content">
    <p>Thank you for signing up for our service. We’re excited to have you onboard.</p>
    <p>Feel free to explore and reach out if you have any questions.</p>
    </div>
    <div class="footer">
    &copy; 2025 YourCompany. All rights reserved.
    </div>
    </div>
    </body>
    </html>
    """


order_mail_template = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Order Confirmation</title>
  <style>
    body {{
      background-color: #f4f4f4;
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 0;
    }}
    .container {{
      max-width: 600px;
      margin: 30px auto;
      background-color: #ffffff;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      padding: 30px;
    }}
    .header {{
      background-color: #4CAF50;
      color: #ffffff;
      padding: 20px;
      text-align: center;
      border-radius: 8px 8px 0 0;
    }}
    .content {{
      padding: 20px;
      color: #333;
    }}
    .order-details {{
      margin-top: 20px;
      border-top: 1px solid #e0e0e0;
      padding-top: 15px;
    }}
    .footer {{
      text-align: center;
      font-size: 12px;
      color: #999;
      margin-top: 40px;
    }}
    .button {{
      display: inline-block;
      background-color: #4CAF50;
      color: #fff;
      padding: 10px 20px;
      text-decoration: none;
      border-radius: 4px;
      margin-top: 20px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>Order Confirmation</h1>
    </div>
    <div class="content">
      <p>Hi Unyime,</p>
      <p>Thank you for shopping with us! We're happy to let you know that your order <strong>#1001</strong> has been confirmed and is now being processed.</p>
      
      <div class="order-details">
        <h3>Order Summary</h3>
        <p><strong>Order Number:</strong> 1001</p>
        <p><strong>Status:</strong> Shipped</p>
        <p><strong>Order Date:</strong> April 1, 2025</p>
        <p><strong>Total:</strong> $149.99</p>
        <p><strong>Shipping Address:</strong> 123 Elm St, Springfield</p>
        <p><strong>Billing Address:</strong> 123 Elm St, Springfield</p>
        <p><strong>Tracking Number:</strong> TRK1234567890</p>
      </div>

      <a href="https://www.yourshop.com/track-order/1001" class="button">Track Your Order</a>

      <p>If you have any questions or concerns, feel free to reply to this email or contact our support team at support@shop.com.</p>

      <p>Best regards,<br>The YourShop Team</p>
    </div>
    <div class="footer">
      &copy; 2025 YourShop, Inc. All rights reserved.
    </div>
  </div>
</body>
</html>
"""
