<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fundraising</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
      background: rgb(255, 220, 250);
      color: #000000;
    }

    .fundraising-section {
      text-align: center;
      padding: 4rem 2rem;
    }

    .fundraising-section h1 {
      font-size: 3.5rem;
      margin-bottom: 1rem;
      color: #007c11;
      text-transform: uppercase;
      letter-spacing: 5px;
      text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }

    .fundraising-section p {
      font-size: 1.5rem;
      margin-bottom: 3rem;
      color: #333;
    }

    .donation-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 2rem;
    }

    .donation-card {
      width: 300px;
      padding: 2rem;
      background: rgb(183, 255, 176);
      border: 4px solid rgb(255, 220, 250);
      border-radius: 15px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
      text-align: center;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .donation-card:hover {
      transform: translateY(-10px);
      box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
    }

    .donation-card h2 {
      font-size: 2rem;
      color: rgb(253, 0, 211);
      margin-bottom: 1rem;
    }

    .donation-card p {
      font-size: 1.1rem;
      margin-bottom: 1.5rem;
      color: #000000;
    }

    .donate-button {
      display: inline-block;
      padding: 0.8rem 2rem;
      font-size: 1.2rem;
      font-weight: bold;
      color: white;
      background: linear-gradient(135deg, #007c11, #005f0d);
      border: none;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
    }

    .donate-button:hover {
      background: linear-gradient(135deg, #005f0d, #007c11);
      transform: translateY(-2px);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    .donate-button:active {
      transform: translateY(0);
      box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
    }
  </style>
</head>

<body>
  <section class="fundraising-section">
    <h1>Support Our Team</h1>
    <p>Your contributions help us build robots, participate in competitions, and inspire the next generation of innovators.</p>

    <div class="donation-container">
      <!-- Donation Tier 1 -->
      <div class="donation-card">
        <h2>Bronze Sponsor</h2>
        <p>Donate $50 to help us purchase essential tools and materials for our robot builds.</p>
        <a href="/donate/bronze" class="donate-button">Donate $50</a>
      </div>

      <!-- Donation Tier 2 -->
      <div class="donation-card">
        <h2>Silver Sponsor</h2>
        <p>Donate $100 to support our competition registration fees and travel expenses.</p>
        <a href="/donate/silver" class="donate-button">Donate $100</a>
      </div>

      <!-- Donation Tier 3 -->
      <div class="donation-card">
        <h2>Gold Sponsor</h2>
        <p>Donate $250 or more to become a key supporter. Your logo will be featured on our robot and website.</p>
        <a href="/donate/gold" class="donate-button">Donate $250+</a>
      </div>
    </div>
  </section>
</body>

</html>