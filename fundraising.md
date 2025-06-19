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

    .fundraising-section h2 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
      color: #007c11;
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
      position: relative;
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
      margin-top: 1.5rem;
      padding: 1rem;
      background-color: rgba(255, 255, 255, 0.7);
      border-radius: 10px;
      text-align: left;
    }

    .more-info ul {
      margin-left: 1rem;
      padding-left: 1rem;
      text-align: left;
    }

    .more-info li {
      margin-bottom: 0.5rem;
    }

    .more-info p {
      margin-top: 1rem;
      font-style: italic;
    }

    .custom-donation {
      max-width: 600px;
      margin: 0 auto 4rem auto;
      padding: 2rem;
      background: rgb(183, 255, 176);
      border: 4px solid rgb(255, 220, 250);
      border-radius: 15px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    
    .custom-donation h2 {
      font-size: 2.2rem;
      color: rgb(253, 0, 211);
      margin-bottom: 1.5rem;
    }

    .custom-donation p {
      font-size: 1.3rem;
      margin-bottom: 1.5rem;
    }

    .donation-form {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
      gap: 1rem;
    }
    
    .donation-input {
      display: flex;
      align-items: center;
      position: relative;
    }
    
    .dollar-sign {
      position: absolute;
      left: 10px;
      font-size: 1.2rem;
      font-weight: bold;
      color: #007c11;
    }
    
    #customAmount {
      padding: 0.8rem 0.8rem 0.8rem 30px;
      font-size: 1.2rem;
      border-radius: 8px;
      border: 2px solid #007c11;
      width: 150px;
    }
    
    #customAmount:focus {
      outline: none;
      border-color: rgb(253, 0, 211);
      box-shadow: 0 0 5px rgba(253, 0, 211, 0.5);
    }
    
    @media (max-width: 600px) {
      .donation-form {
        flex-direction: column;
      }
      
      #customAmount {
        width: 100%;
        margin-bottom: 1rem;
      }
    }
  </style>
</head>

<body>
  <section class="fundraising-section">
    <h1>Support Our FTC Team</h1>
    <p>Your contributions help our FIRST Tech Challenge team build robots, participate in competitions, and inspire the next generation of STEM innovators.</p>
    
    

    <div class="custom-donation">
      <h2>Custom Donation Amount</h2>
      <p>Enter your preferred donation amount to support our FTC robotics team!</p>
      <form class="donation-form" id="customDonationForm">
        <div class="donation-input">
          <span class="dollar-sign">$</span>
          <input type="number" id="customAmount" min="1" placeholder="Amount" required>
        </div>
        <button type="submit" class="donate-button">Donate Now</button>
      </form>
    </div>

    <h2>Our Rubber Duck Sponsorship Levels</h2>
    <p>Join our team of supporters with these duck-tastic sponsorship options!</p>

    <div class="donation-container">
      <!-- Donation Tier 1 -->
      <div class="donation-card">
        <h3>JUST QUACKING BY</h3>
        <p>$25 - Our entry-level supporters who keep our little duckies afloat!</p>
        <p><b>Benefits:</b> Name on our website and a team thank-you note</p>
        <a href="#" class="donate-button">Sponsor $25</a>
        <div class="learn-more" onclick="toggleInfo('info-1', this)">Learn More ▼</div>
        <div class="more-info" id="info-1">
          <p>As a <b>Just Quacking By</b> sponsor, you'll receive:</p>
          <ul>
            <li>Recognition on our team website</li>
            <li>Personalized thank-you note</li>
            <li>Updates about our team's progress</li>
          </ul>
          <p>Your $25 contribution helps us purchase basic materials and tools for our robot!</p>
        </div>
      </div>

      <!-- Donation Tier 2 -->
      <div class="donation-card">
        <h3>BILL BENEFACTORS</h3>
        <p>$50 - A bigger splash with extra waterproof perks!</p>
        <p><b>Benefits:</b> Name on website, thank-you note, and team photo</p>
        <a href="#" class="donate-button">Sponsor $50</a>
        <div class="learn-more" onclick="toggleInfo('info-2', this)">Learn More ▼</div>
        <div class="more-info" id="info-2">
          <p>As a <b>Bill Benefactors</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Just Quacking By benefits</li>
            <li>Signed team photo</li>
            <li>Special mention in our engineering notebook</li>
          </ul>
          <p>Your $50 contribution helps us purchase electronic components and sensors for our robot!</p>
        </div>
      </div>

      <!-- Donation Tier 3 -->
      <div class="donation-card">
        <h3>WADDLE WARRIORS</h3>
        <p>$100 - These champions have earned their webbed badge of honor!</p>
        <p><b>Benefits:</b> All previous benefits plus name in our competition pit display</p>
        <a href="#" class="donate-button">Sponsor $100</a>
        <div class="learn-more" onclick="toggleInfo('info-3', this)">Learn More ▼</div>
        <div class="more-info" id="info-3">
          <p>As a <b>Waddle Warriors</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Bill Benefactors benefits</li>
            <li>Name featured in our competition pit display</li>
            <li>3D printed rubber duck with our team number</li>
            <li>Invitation to a team practice session</li>
          </ul>
          <p>Your $100 contribution helps us purchase motors, gears, and drivetrain components!</p>
        </div>
      </div>

      <!-- Donation Tier 4 -->
      <div class="donation-card">
        <h3>FEATHER FANATICS</h3>
        <p>$250 - Seriously committed to our squeaky yellow friends!</p>
        <p><b>Benefits:</b> All previous benefits plus small logo on team t-shirts</p>
        <a href="#" class="donate-button">Sponsor $250</a>
        <div class="learn-more" onclick="toggleInfo('info-4', this)">Learn More ▼</div>
        <div class="more-info" id="info-4">
          <p>As a <b>Feather Fanatics</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Waddle Warriors benefits</li>
            <li>Small logo on our team t-shirts</li>
            <li>Team t-shirt for yourself</li>
            <li>Invitation to demonstration events</li>
          </ul>
          <p>Your $250 contribution helps us pay for competition registration fees and custom parts!</p>
        </div>
      </div>

      <!-- Donation Tier 5 -->
      <div class="donation-card">
        <h3>POND PROTECTORS</h3>
        <p>$500 - The guardians of all things bath-time related!</p>
        <p><b>Benefits:</b> All previous benefits plus medium logo on robot and pit display</p>
        <a href="#" class="donate-button">Sponsor $500</a>
        <div class="learn-more" onclick="toggleInfo('info-5', this)">Learn More ▼</div>
        <div class="more-info" id="info-5">
          <p>As a <b>Pond Protectors</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Feather Fanatics benefits</li>
            <li>Medium-sized logo on our robot</li>
            <li>Medium-sized logo on our pit display</li>
            <li>Special recognition at competitions</li>
            <li>Invitation to team dinner</li>
          </ul>
          <p>Your $500 contribution helps us cover travel expenses and advanced robot components!</p>
        </div>
      </div>

      <!-- Donation Tier 6 -->
      <div class="donation-card">
        <h3>SUPREME SQUEAKERS</h3>
        <p>$1,000 - Our elite rubber duck enthusiasts who never duck their responsibilities!</p>
        <p><b>Benefits:</b> All previous benefits plus large logo on robot and team banner</p>
        <a href="#" class="donate-button">Sponsor $1,000</a>
        <div class="learn-more" onclick="toggleInfo('info-6', this)">Learn More ▼</div>
        <div class="more-info" id="info-6">
          <p>As a <b>Supreme Squeakers</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Pond Protectors benefits</li>
            <li>Large logo on our robot</li>
            <li>Large logo on our team banner</li>
            <li>Private robot demonstration</li>
            <li>Framed team photo with certificate</li>
          </ul>
          <p>Your $1,000 contribution helps us purchase high-end electronics and sophisticated sensors!</p>
        </div>
      </div>

      <!-- Donation Tier 7 -->
      <div class="donation-card">
        <h3>MALLARD MAGNATES</h3>
        <p>$5,000 - The big bills behind our entire bathtub empire!</p>
        <p><b>Benefits:</b> All previous benefits plus social media shoutouts and robot naming rights</p>
        <a href="#" class="donate-button">Sponsor $5,000</a>
        <div class="learn-more" onclick="toggleInfo('info-7', this)">Learn More ▼</div>
        <div class="more-info" id="info-7">
          <p>As a <b>Mallard Magnates</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Supreme Squeakers benefits</li>
            <li>Monthly social media shoutouts</li>
            <li>Robot naming rights for the season</li>
            <li>VIP access to competitions</li>
            <li>Personalized video updates</li>
            <li>Honorary team membership with team jacket</li>
          </ul>
          <p>Your $5,000 contribution helps us attend championship events and establish advanced manufacturing capabilities!</p>
        </div>
      </div>

      <!-- Donation Tier 8 -->
      <div class="donation-card">
        <h3>QUACK ATTACK PLATINUM</h3>
        <p>$10,000+ - Legends of the lavatory whose generosity makes waves everywhere!</p>
        <p><b>Benefits:</b> All previous benefits plus special team demonstration at your location</p>
        <a href="#" class="donate-button">Sponsor $10,000+</a>
        <div class="learn-more" onclick="toggleInfo('info-8', this)">Learn More ▼</div>
        <div class="more-info" id="info-8">
          <p>As a <b>Quack Attack Platinum</b> sponsor, you'll receive:</p>
          <ul>
            <li>All Mallard Magnates benefits</li>
            <li>Premium placement of your logo on all materials</li>
            <li>Exclusive team workshops at your location</li>
            <li>Opportunity to participate in robot unveiling</li>
            <li>Permanent recognition plaque in our workshop</li>
            <li>Custom STEM presentation for your organization</li>
          </ul>
          <p>Your $10,000+ contribution is transformational for our team, enabling us to purchase top-tier equipment and establish long-term sustainability!</p>
          <p>Our current Quack Attack Platinum sponsors are:</p>
            <li>Blue Ridge Boost</li>
        </div>
      </div>
    </div>
    
    <p>All sponsorships help our team compete in the FIRST Tech Challenge and inspire future engineers!</p>
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

    document.getElementById('customDonationForm').addEventListener('submit', function(e) {
      e.preventDefault();
      const amount = document.getElementById('customAmount').value;
      
      if (!amount || amount <= 0) {
        alert('Please enter a valid donation amount');
        return;
      }
      
      alert(`Thank you for your generous donation of $${amount} to our FTC team! Your support means so much to us.`);
      document.getElementById('customAmount').value = '';
    });
    
    // Add event listeners to the individual sponsorship tier buttons
    document.querySelectorAll('.donation-card .donate-button').forEach(button => {
      button.addEventListener('click', function(e) {
        e.preventDefault();
        const amount = this.textContent.match(/\$(\d+(?:,\d+)*(?:\+)?)/)[1].replace(',', '');
        alert(`Thank you for your generous FTC team sponsorship of $${amount}! We'll contact you about your sponsorship benefits and logo placement.`);
      });
    });
  </script>
</body>

</html>
