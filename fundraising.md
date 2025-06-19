  <section class="fundraising-section">
    <h1>Support Our FTC Team</h1>
    <p>Your contributions help our FIRST Tech Challenge team build robots, participate in competitions, and inspire the next generation of STEM innovators.</p>
    
    

    <div class="custom-donation">
      <h2>Donations</h2>
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
        <p><b>Benefits:</b> Your company's name and logo on our website. </p>
        <a href="#" class="donate-button">Sponsor $100</a>
      </div>

      <!-- Donation Tier 2 -->
      <div class="donation-card">
        <h3>FEATHER FANATICS</h3>
        <p><b>Benefits:</b> All Just Quacking By benefits and a spotlight in our social posts. </p>
        <a href="#" class="donate-button">Sponsor $250</a>
      </div>

      <!-- Donation Tier 3 -->
      <div class="donation-card">
        <h3>POND PROTECTORS</h3>
        <p><b>Benefits:</b> All Feather Fanatics benefits and a logo on our team shirts. </p>
        <a href="#" class="donate-button">Sponsor $500</a>
      </div>

      <!-- Donation Tier 4 -->
      <div class="donation-card">
        <h3>SUPREME SQUEAKERS</h3>
        <p><b>Benefits:</b> All Pond Protectors benefits and a sticker on our robot. </p>
        <a href="#" class="donate-button">Sponsor $1,000</a>
      </div>

      <!-- Donation Tier 5 -->
      <div class="donation-card">
        <h3>MALLARD MAGNATES</h3>
        <p><b>Benefits:</b> All Supreme Squeakers benefits and three posts on our social media. </p>
        <a href="#" class="donate-button">Sponsor $5,000</a>
      </div>

      <!-- Donation Tier 6 -->
      <div class="donation-card">
        <h3>QUACK ATTACK PLATINUM</h3>
        <p><b>Benefits:</b> All Mallard Magnates benefits, 2 more social media posts, and your logo on our 2' x 3' competition pit banner. </p>
        <a href="#" class="donate-button">Sponsor $10,000+</a>
      </div>

      
        <h3><b>ALL POND PROTECTORS, SUPREME SQUEAKERS, MALLARD MAGNATES, AND QUACK ATTACK PLATINUM DONATIONS MUST BE RECEIVED BY 11/1/2025 TO BE PUT ON THE 2025-2026 SEASON TEAM SHIRTS.</b></h3>
      
    
    <p>All sponsorships help our team compete in the FIRST Tech Challenge and inspire future engineers!</p>
  <!-- </section> -->

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

