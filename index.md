<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FTC Team 26502</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
      background: rgb(255, 220, 250);
      color: #000000;
      text-align: center;
      padding: 2rem;
    }

    h1 {
      color: #007c11;
      margin-bottom: 1rem;
      font-size: 3.5rem;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
      text-transform: uppercase;
      letter-spacing: 5px;
    }

    h2 {
      color: rgb(253, 0, 211);
      margin-bottom: 1rem;
    }

    p {
      margin-top: 1rem;
      font-size: 1.2rem;
      color: #333;
      line-height: 1.6;
    }

    .team-info {
      background: rgb(183, 255, 176); /* Light green box color */
      border: 4px solid rgb(255, 220, 250); /* Pink border color */
      border-radius: 15px;
      padding: 2rem;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
      margin-bottom: 2rem;
    }

    .featured-section {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      margin: 3rem 0;
      background: rgb(183, 255, 176); /* Light green box color */
      border: 4px solid rgb(255, 220, 250); /* Pink border color */
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .featured-image {
      flex: 1;
      min-width: 300px;
      height: 400px;
    }

    .featured-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .featured-text {
      flex: 1;
      min-width: 600px;
      padding: 2rem;
      text-align: left;
    }

    .stats-section {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin: 3rem 0;
    }

    .stat-box {
      background: rgb(183, 255, 176); /* Light green box color */
      border: 4px solid rgb(255, 220, 250); /* Pink border color */
      border-radius: 15px;
      padding: 2rem;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .stat-number {
      font-size: 3rem;
      font-weight: bold;
      color: rgb(253, 0, 211); /* Pink text color */
      margin-bottom: 0.5rem;
    }

    .stat-label {
      font-size: 1.2rem;
      color: #333;
    }

    footer {
      background-color: #007c11;
      color: white;
      text-align: center;
      padding: 2rem;
      margin: 3rem -2rem -2rem -2rem;
      border-radius: 20px 20px 0 0;
    }

    .main-content {
      max-width: 80rem;
    }

    @media (max-width: 1000px) {
      h1 {
        font-size: 2.5rem;
      }

      .featured-image,
      .featured-text {
        flex: 100%;
      }

      .stats-section {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>

<body>
  <!-- Team Information Section -->
  <div class="team-info" id="about">
    <h1>Wicked Smart; Quacking Up Innovation</h1>
  </div>

  <!-- Our Team Section -->
  <div class="featured-section">
    <div class="featured-image">
      <img src="/Images/TeamPhoto.jpg" alt="Team Photo">
    </div>
    <div class="featured-text">
      <h2>Our Team</h2>
      <p>We’re a girl-powered FIRST Tech Challenge (FTC) team from Charlottesville, Virginia, and this is our second year in the program! Our motto is “Wicked Smart; Quacking Up Innovation,” and we’re all about inspiring and empowering people in our community through spreading STEM and FIRST (For Inspiration and Recognition of Science and Technology). We love hosting workshops, mentoring other teams, and working with local organizations to make STEM fun and easy to learn. Our goal is to get more girls into robotics and share how awesome innovation and teamwork can be.</p>
    </div>
  </div>

  <!-- Robot Design Section -->
  <div class="featured-section">
    <div class="featured-text">
      <h2>Meet Our Robot</h2>
      <p>Chassis: Compact 13.5” x 15” for agility; limited space for mechanisms.<br>
        Drivetrain: Miter gearboxes optimized weight but reduced intake space.<br>
        Intake: 3D-printed claw on a rotating arm with Viper slide and scissor lift.<br>
        Motor: A high-torque motor improved the slide control.<br>
        Challenge: Steel slides added weight, limiting ascent.</p>
    </div>
    <div class="featured-image">
      <img src="/Images/Robot.jpg" alt="Robot Design">
    </div>
  </div>

  <!-- Competition History Section -->
  <div class="featured-section">
    <div class="featured-text">
      <h2>Last Year</h2>
      <p>Last year, we won the Control Award by enhancing our robot with innovative color sensors and indicator lights. We added a color sensor to our claw, programmed to detect red, blue, and yellow blocks, ensuring it only closes on the correct colors. This feature enables effective collaboration with our alliance partners, whether scoring samples in the high basket or specimens in high chambers. After expert feedback at the Collaborative Robotics Lab at UVa, we shifted to a pose detection approach to determine servo commands based on block orientation.</p>
    </div>
    <div class="featured-image">
      <img src="/Images/ControlAward.jpg" alt="Competition History">
    </div>
  </div>

  <!-- Team Stats -->
  <div class="stats-section">
    <div class="stat-box">
      <div class="stat-number">2</div>
      <div class="stat-label">Competition Seasons</div>
    </div>
    <div class="stat-box">
      <div class="stat-number">4</div>
      <div class="stat-label">Team Members</div>
    </div>
    <div class="stat-box">
      <div class="stat-number">17</div>
      <div class="stat-label">Events</div>
    </div>
    <div class="stat-box">
      <div class="stat-number">1</div>
      <div class="stat-label">Awards Won</div>
    </div>
  </div>

  <!-- Contact Section -->
  <div class="team-info" id="contact">
    <h2>Contact Us</h2>
    <p>Interested in learning more about our team? Want to become a sponsor? Have questions about FIRST Tech Challenge?</p>
    <p>Email: ftcteam26502@example.com</p>
    <a href="#" class="button">YouTube</a>
  </div>

  <!-- Footer -->
  <footer>
    <p>&copy; 2025 FTC Team 26502. All Rights Reserved.</p>
    <p>FIRST®, FIRST® Tech Challenge, and CENTERSTAGE℠ are trademarks of FIRST (For Inspiration and Recognition of Science and Technology).</p>
  </footer>
</body>

</html>