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
      background-color: rgb(255, 220, 250);
      color: #000;
      text-align: center;
      padding: 2rem;
    }

    h1 {
      color: white;
      margin-bottom: 1rem;
      font-size: 3.5rem;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    h2 {
      color: rgb(253, 0, 211);
      margin-bottom: 1rem;
    }

    .header-subtitle {
      font-size: 1.5rem;
      margin-bottom: 2rem;
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }

    p {
      margin-top: 1rem;
      font-size: 1.2rem;
      color: #333;
      line-height: 1.6;
    }

    .team-info {
      background-color: white;
      border-radius: 10px;
      padding: 2rem;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      margin-bottom: 2rem;
    }

    .featured-section {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      margin: 3rem 0;
      background-color: white;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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

    .button-group {
      margin-top: 2rem;
    }

    .button {
      display: inline-block;
      margin: 0.5rem;
      padding: 0.7rem 1.5rem;
      font-size: 1rem;
      font-weight: bold;
      color: #fff;
      background-color: #007c11;
      text-decoration: none;
      border-radius: 5px;
      transition: background-color 0.3s ease;
    }

    .button:hover {
      background-color: #005a0d;
    }

    .season-banner {
      background-image: linear-gradient(rgba(0, 124, 17, 0.8), rgba(0, 124, 17, 0.8)), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300"><rect fill="%23007c11" width="1200" height="300"/><circle fill="%2300a316" cx="300" cy="150" r="100"/><circle fill="%2300a316" cx="900" cy="150" r="100"/></svg>');
      background-size: cover;
      color: white;
      padding: 3rem 2rem;
      margin: 3rem 0;
      border-radius: 10px;
    }

    .season-banner h2 {
      color: white;
      margin-bottom: 1rem;
      font-size: 2.5rem;
    }

    .stats-section {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin: 3rem 0;
    }

    .stat-box {
      background-color: white;
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .stat-number {
      font-size: 3rem;
      font-weight: bold;
      color: rgb(253, 0, 211);
      margin-bottom: 0.5rem;
    }

    .stat-label {
      font-size: 1.2rem;
      color: #333;
    }

    .back-link {
      display: block;
      margin-top: 2rem;
      font-size: 1rem;
      text-decoration: underline;
      color: #007c11;
    }

    .back-link:hover {
      color: #005a0d;
    }

    footer {
      background-color: #007c11;
      color: white;
      text-align: center;
      padding: 2rem;
      margin: 3rem -2rem -2rem -2rem;
      border-radius: 20px 20px 0 0;
    }

    .main-content{
        max-width: 80rem;
    }

    @media (max-width: 1000px) {
      h1 {
        font-size: 2.5rem;
      }
      
      .header-subtitle {
        font-size: 1.2rem;
      }
      
      .featured-image, .featured-text {
        flex: 100%;
      }
      
      .stats-section {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>

<body>
  <div class="team-info" id="about">
    <h2>Welcome to Team 26502</h2>
    <p>We are a FIRST Tech Challenge robotics team dedicated to learning, innovation, and community outreach. Our team brings together passionate students interested in science, technology, engineering, and mathematics (STEM).</p>
  </div>

  <!-- Our Team Section -->
  <div class="featured-section">
    <div class="featured-image">
      <img src="/Images/TeamPhoto.JPG" width='700' height='700' alt="Team Photo">
    </div>
    <div class="featured-text">
      <h2>Our Team</h2>
      <p>We're not just about building robots — we're building future leaders in STEM.</p>
    </div>
  </div>

  <!-- Robot Design Section -->
  <div class="featured-section">
    <div class="featured-text">
      <h2>Meet Our Robot</h2>
      <p>Last year’s robot featured a compact 13.5” by 15” chassis to maximize maneuverability around the submersible. A smaller chassis improved agility but limited space for additional mechanisms. The drivetrain used miter gearboxes, with one motor mounted horizontally and three vertically, optimizing weight distribution but reducing space for the intake arm. The intake consisted of a 3D-printed claw with a wrist on a rotating arm, attached to a goBILDA 4-stage Viper slide powered by a 188:1 motor and a 3D-printed scissor lift. To accommodate the compact design, we used a high-torque motor for better control over the horizontal slide extension. However, the steel Viper slides added significant weight, limiting ascent capabilities.</p>
    </div>
    <div class="featured-image">
      <img src="/Images/Robot.jpg" width='400' height='600' alt="Robot Design">
    </div>
  </div>

  <!-- Programming Section -->
  <div class="featured-section">
    <div class="featured-image">
      <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 400 400'><rect fill='%23222222' width='400' height='400'/><text x='50' y='80' font-family='monospace' font-size='14' fill='rgb(253, 0, 211)'>public void autonomousInit() {</text><text x='70' y='110' font-family='monospace' font-size='14' fill='%2300a316'>  robot.drive.resetEncoders();</text><text x='70' y='140' font-family='monospace' font-size='14' fill='%2300a316'>  robot.arm.setPosition(0);</text><text x='70' y='170' font-family='monospace' font-size='14' fill='%2300a316'>  robot.intake.setPower(0.5);</text><text x='50' y='200' font-family='monospace' font-size='14' fill='rgb(253, 0, 211)'>}</text><text x='50' y='250' font-family='monospace' font-size='14' fill='rgb(253, 0, 211)'>public void teleopPeriodic() {</text><text x='70' y='280' font-family='monospace' font-size='14' fill='%2300a316'>  double drive = -gamepad1.left_stick_y;</text><text x='70' y='310' font-family='monospace' font-size='14' fill='%2300a316'>  double turn = gamepad1.right_stick_x;</text><text x='70' y='340' font-family='monospace' font-size='14' fill='%2300a316'>  robot.drive.arcadeDrive(drive, turn);</text><text x='50' y='370' font-family='monospace' font-size='14' fill='rgb(253, 0, 211)'>}</text></svg>" alt="Programming">
    </div>
    <div class="featured-text">
      <h2>Programming & Control</h2>
      <p>Our software team develops sophisticated code to control the robot and enable advanced autonomous capabilities. We primarily use Java with the FTC SDK, implementing modern software development practices like version control and continuous integration.</p>
      <p>Our programming highlights:</p>
      <p>• Computer vision for detecting game elements<br>
         • PID control for precise movement<br>
         • Custom autonomous pathing<br>
         • Telemetry dashboard for real-time debugging<br>
         • Driver assistance features</p>
      <p>We believe that great hardware requires equally great software to reach its full potential.</p>
    </div>
  </div>

  <!-- Season Banner -->
  <div class="season-banner" id="season">
    <h2>INTO THE DEEP 2024-2025</h2>
    <p>This season, FTC teams dive INTO THE DEEP℠ presented by Qualcomm. Robots must navigate simulated underwater challenges, collect marine samples, deploy research equipment, and map the ocean floor, pushing teams to develop innovative solutions for exploring Earth's final frontier.</p>
    <div class="button-group">
      <a href="https://info.firstinspires.org/first-tech-challenge" target="_blank" class="button">Learn More About FTC</a>
    </div>
  </div>

  <!-- Competition History -->
  <div class="featured-section">
    <div class="featured-text">
      <h2>Competition History</h2>
      <p>We first began competiting last year in ther 2024-2025 submerged season</p>
      <p>Recent achievements:</p>
      <p>• Control award </p>
      <p>Each competition is an opportunity to showcase our hard work, learn from other teams, and embrace the spirit of "Coopertition" that makes FIRST unique.</p>
    </div>
    <div class="featured-image">
      <img src="/Images/ControlAward.jpg" width='400' height='400' alt="Competition History">
    </div>
  </div>

  <!-- Outreach & Community -->
  <div class="featured-section">
    <div class="featured-image">
      <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 400 400'><rect fill='%23007c11' width='400' height='400'/><circle fill='%2300a316' cx='200' cy='200' r='150'/><circle fill='%2300cc1c' cx='200' cy='200' r='100'/></svg>" alt="Community Outreach">
    </div>
    <div class="featured-text">
      <h2>Outreach & Community</h2>
      <p>Team 26502 is dedicated to spreading STEM education throughout our community. We participate in demonstrations at local schools, community events, and STEM fairs to inspire younger students to pursue their interests in science and technology.</p>
      <p>Our outreach initiatives include:</p>
      <p>• Robotics demonstrations at elementary schools<br>
         • Mentoring FLL teams<br>
         • Hosting community STEM workshops<br>
         • Participating in local tech events</p>
      <p>Through these efforts, we aim to share our passion for STEM and encourage the next generation of innovators.</p>
    </div>
  </div>

  <!-- Team Stats -->
  <div class="stats-section">
    <div class="stat-box">
      <div class="stat-number">3</div>
      <div class="stat-label">Competition Seasons</div>
    </div>
    <div class="stat-box">
      <div class="stat-number">12</div>
      <div class="stat-label">Team Members</div>
    </div>
    <div class="stat-box">
      <div class="stat-number">500+</div>
      <div class="stat-label">Build Hours</div>
    </div>
    <div class="stat-box">
      <div class="stat-number">4</div>
      <div class="stat-label">Awards Won</div>
    </div>
  </div>

  <!-- Sponsors Section -->
  <div class="featured-section">
    <div class="featured-text">
      <h2>Our Sponsors</h2>
      <p>Our team wouldn't be possible without the generous support of our sponsors. Their contributions help us purchase materials, travel to competitions, and continue our outreach programs.</p>
      <p>Sponsorship benefits include:</p>
      <p>• Team recognition and branding opportunities<br>
         • Engagement with talented future engineers<br>
         • Community outreach visibility<br>
         • Tax-deductible contribution to STEM education</p>
      <p>Interested in becoming a sponsor? Contact us to learn about our sponsorship levels and benefits!</p>
    </div>
    <div class="featured-image">
      <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 400 400'><rect fill='%23ffffff' width='400' height='400'/><rect fill='%23eeeeee' x='50' y='50' width='300' height='80'/><text x='200' y='100' font-family='Arial' font-size='24' text-anchor='middle' fill='%23333333'>Sponsor 1</text><circle fill='%23eeeeee' cx='200' cy='200' r='70'/><text x='200' y='210' font-family='Arial' font-size='24' text-anchor='middle' fill='%23333333'>Sponsor 2</text><rect fill='%23eeeeee' x='50' y='270' width='300' height='80'/><text x='200' y='320' font-family='Arial' font-size='24' text-anchor='middle' fill='%23333333'>Sponsor 3</text></svg>" alt="Sponsors">
    </div>
  </div>

  <!-- Contact Section -->
  <div id="contact" class="team-info">
    <h2>Contact Us</h2>
    <p>Interested in learning more about our team? Want to become a sponsor? Have questions about FIRST Tech Challenge?</p>
    <p>Email: ftcteam26502@example.com</p>
    <p>Follow us on social media:</p>
    <div class="button-group">
      <a href="#" class="button">Instagram</a>
      <a href="#" class="button">Twitter</a>
      <a href="#" class="button">YouTube</a>
    </div>
  </div>

  <a href="/teams/" class="back-link">Back to Teams</a>

  <footer>
    <p>&copy; 2025 FTC Team 26502. All Rights Reserved.</p>
    <p>FIRST®, FIRST® Tech Challenge, and CENTERSTAGE℠ are trademarks of FIRST (For Inspiration and Recognition of Science and Technology).</p>
  </footer>
</body>

</html>