<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FTC Fundraising</title>
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
      margin-bottom: 2rem;
      color: #333;
    }

    .venmo-button {
      display: inline-block;
      padding: 1rem 2rem;
      font-size: 1.5rem;
      font-weight: bold;
      color: white;
      background: linear-gradient(135deg, #007c11, #005f0d);
      border: none;
      border-radius: 8px;
      text-decoration: none;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
      cursor: pointer;
      margin-bottom: 2rem;
    }

    .venmo-button:hover {
      background: linear-gradient(135deg, #005f0d, #007c11);
      transform: translateY(-2px);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    .donation-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 2rem;
      margin-bottom: 3rem;
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

    .donation-card h3 {
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
      cursor: pointer;
      margin-bottom: 0.8rem;
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

    .learn-more {
      display: block;
      color: #007c11;
      cursor: pointer;
      text-decoration: underline;
      font-weight: bold;
      margin-top: 0.5rem;
    }

    .learn-more:hover {
      color: rgb(253, 0, 211);
    }

    .more-info {
      display: none;
      margin-top: 1rem;
      padding: 1rem;
      background-color: rgba(255, 255, 255, 0.7);
      border-radius: 10px;
      text-align: left;
    }

    .more-info ul {
      margin-left: 1rem;
      padding-left: 1rem;
    }

    .more-info li {
      margin-bottom: 0.5rem;
    }

    .more-info p {
      margin-top: 1rem;
      font-style: italic;
    }
  </style>
</head>

<body>
  <section class="fundraising-section">
    <h1>Support Our FTC Team</h1>
    <p>Your contributions help our FIRST Tech Challenge team build robots, participate in competitions, and inspire the next generation of STEM innovators.</p>

    <a href="https://venmo.com/u/Burton" class="venmo-button" target="_blank">
      Use Our Venmo: @Team up for STEM
    </a>
  </section>

  <section class="fundraising-section">
    <h2>Our Sponsorship Levels</h2>
    <div class="donation-container">
      <div class="donation-card">
        <h3>Just Quacking By</h3>
        <p>$25 - Entry-level supporters who keep our duckies afloat!</p>
        <p><b>Benefits:</b> Name on our website and a thank-you note.</p>
        <a href="#" class="donate-button">Donate $25</a>
        <div class="learn-more" onclick="toggleInfo('info-1', this)">Learn More ▼</div>
        <div class="more-info" id="info-1">
          <p>As a <b>Just Quacking By</b> sponsor, you'll receive:</p>
          <ul>
            <li>Recognition on our team website</li>
            <li>Personalized thank-you note</li>
          </ul>
          <p>Your $25 contribution helps us purchase basic materials and tools for our robot!</p>
        </div>
      </div>

      <div class="donation-card">
        <h3>Bill Benefactors</h3>
        <p>$50 - A bigger splash with extra perks!</p>
        <p><b>Benefits:</b> Name and photo on website plus thank-you note.</p>
        <a href="#" class="donate-button">Donate $50</a>
        <div class="learn-more" onclick="toggleInfo('info-2', this)">Learn More ▼</div>
        <div class="more-info" id="info-2">
          <p>As a <b>Bill Benefactors</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Just Quacking By benefits</li>
            <li>Signed team photo</li>
          </ul>
          <p>Your $50 contribution helps us purchase electronic components and sensors for our robot!</p>
        </div>
      </div>

      <div class="donation-card">
        <h3>Waddle Warriors</h3>
        <p>$100 - Earn your webbed badge of honor!</p>
        <p><b>Benefits:</b> All previous benefits plus name in our competition pit display.</p>
        <a href="#" class="donate-button">Donate $100</a>
        <div class="learn-more" onclick="toggleInfo('info-3', this)">Learn More ▼</div>
        <div class="more-info" id="info-3">
          <p>As a <b>Waddle Warriors</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Bill Benefactors benefits</li>
            <li>Name featured in our competition pit display</li>
          </ul>
          <p>Your $100 contribution helps us purchase drivetrain components for the robot!</p>
        </div>
      </div>
    </div>
  </section>

  <script>
    function toggleInfo(id, button) {
      const infoDiv = document.getElementById(id);
      if (infoDiv.style.display === "block") {
        infoDiv.style.display = "none";
        button.innerHTML = "Learn More ▼";
      } else {
        infoDiv.style.display = "block";
        button.innerHTML = "Show Less ▲";
      }
    }
  </script>
</body>

</html>