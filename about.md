
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meet the Team</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
      background:rgb(255, 220, 250);
      color: #000000;
    }

    .team-section {
      text-align: center;
      padding: 4rem 2rem;
    }

    .team-section h1 {
      font-size: 3rem;
      margin-bottom: 1rem;
      color: #007c11;
      text-transform: uppercase;
      letter-spacing: 5px;
    }

    .team-section p {
      font-size: 1.2rem;
      margin-bottom: 3rem;
      color: #000000;
    }

    .team-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 2rem;
    }

    .card-container {
      perspective: 1000px;
    }

    .team-card {
      width: 300px;
      height: 400px;
      position: relative;
      transform-style: preserve-3d;
      transition: transform 0.8s;
      cursor: pointer;
    }

    .team-card .card-side {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      border-radius: 15px;
      overflow: hidden;
    }

    .team-card .card-front {
      background:rgb(174, 255, 149);;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      box-shadow: 0 4px 8px rgba(72, 255, 0, 0.38);
      padding: 20px;
      text-align: center;
      color: rgb(225, 0, 255);
    }

    .team-card .card-front img {
      width: 200px;
      height: 200px;
      border-radius: 10%;
      margin-bottom: 5px;
    }

    .team-card .card-front h3 {
      font-size: 1.5rem;
      color: #333;
      margin-bottom: 10px;
    }

    .team-card .card-front p {
      font-size: 1rem;
      color: rgb(0, 0, 0);
    }

    .team-card .card-back {
      background:rgb(255, 104, 222);
      color:rgb(255, 255, 255);
      transform: rotateY(180deg);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 20px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .team-card .card-back p {
      font-size: 1rem;
      line-height: 1.5;
    }
  </style>
</head>
<body>

  <section class="team-section">
    <h1>Our Story</h1>
    <p>Our FTC Team, BRB Robotics, 26502, started in 2024 with the support of Blue Ridge Boost. Our goal is to expand both our team and FIRST by educating and engaging with our community through demonstrations. Through these events, we hope to connect with potential teammates and sponsors who can help support our efforts.</p>
    <h3>The Teammates</h3>
    <div class="team-container">
      <!-- Team Member 1 -->
      <div class="card-container">
        <div class="team-card" onclick="flipCard(this)">
          <div class="card-side card-front">
            <img src="/Images/Dorina.jpg" alt="Dorina Evans">
            <h3>Dorina Evans</h3>
            <p>Software Developer</p>
          </div>
          <div class="card-side card-back">
            <p>I have been part of FIRST for seven years, starting with FLL Explore and progressing to FTC last year. These competitions have fueled my passion for coding and engineering. We won the Control Award last year. I focus on Computer Aided Design (CAD) for our robot and will also handle the coding for both our teleop and autonomous modes.</p>
          </div>
        </div>
      </div>
      <!-- Team Member 2 -->      
      <div class="card-container">
        <div class="team-card" onclick="flipCard(this)">
          <div class="card-side card-front">
            <img src="/Images/Ananya.jpg" alt="Raven Steele">
            <h3>Ananya Singla</h3>
            <p>Outreach Specialist</p>
          </div>
          <div class="card-side card-back">
            <p>This year is my third year of FIRST and I have completed two seasons of FLL Challenge and this will be my second year of FTC. Through FIRST and similar competitions alike, I have gained a passion for engineering, coding, and sharing robotics with my community. This year, I am our team's outreach coordinator, co-captain with Dorina, driving coach, and a builder.</p>
          </div>
        </div>
      </div>
      <!-- Team Member 3 -->
      <div class="card-container">
        <div class="team-card" onclick="flipCard(this)">
          <div class="card-side card-front">
            <img src="/Images/Arnie.jpg" alt="Arnie Singla">
            <h3>Arnie Singla</h3>
            <p>Mechanical Engineer</p>
          </div>
          <div class="card-side card-back">
            <p>This is my third year in the FIRST community. I participated in FLL Challenge for two years, starting in third grade, where my teams earned the Innovation and Robot Design Awards at regionals qualifiers.  I’m excited to continue my journey with FIRST for the next seven years and explore new opportunities to grow and contribute.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    function flipCard(card) {
      if (card.style.transform === 'rotateY(180deg)') {
        card.style.transform = 'rotateY(0deg)';
      } else {
        card.style.transform = 'rotateY(180deg)';
      }
    }
  </script>

</body>
</html>