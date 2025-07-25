---
title: "Meet the Team"
date: 2019-04-10T09:51:57+06:00
short_description: "Cupidatat non proident sunt culpa qui officia deserunt mollit <br> anim idest laborum sed ut perspiciatis."
page_header_image: "images/background/about.jpg"
description : "this is meta description"
# layout: "search"
draft: false
---
 
 
  <section class="team-section">
    <h1>Our Story</h1>
    <p>Our FTC Team, BRB Robotics, 26502, started in 2024 with the support of Blue Ridge Boost. Our goal is to expand both our team and FIRST by educating and engaging with our community through demonstrations. Through these events, we hope to connect with potential teammates and sponsors who can help support our efforts.</p>
    <h3>The Teammates</h3>
    <div class="team-container">
      <!-- Team Member 1 -->
      <div class="card-container">
        <div class="team-card" onclick="flipCard(this)">
          <div class="card-side card-front">
            <img src="images/team/team-member-1.jpg" alt="Dorina Evans">
            <h3>Dorina Evans</h3>
            <p>Engineering and Coding Lead</p>
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
            <p>Team Operations Lead</p>
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
            <img src="/Images/Arnie.JPG" alt="Arnie Singla">
            <h3>Arnie Singla</h3>
            <p>Builder</p>
          </div>
          <div class="card-side card-back">
            <p>This is my third year in the FIRST community. I participated in FLL Challenge for two years, starting in third grade, where my teams earned the Innovation and Robot Design Awards at regionals qualifiers.  I’m excited to continue my journey with FIRST for the next seven years and explore new opportunities to grow and contribute.</p>
          </div>
        </div>
      </div>
      <!-- Team Member 4 -->
      <div class="card-container">
        <div class="team-card" onclick="flipCard(this)">
          <div class="card-side card-front">
            <img src="/Images/IMG_2701.jpg" alt="Sagnik Biswas">
            <h3>Sagnik Biswas</h3>
            <p>Builder</p>
          </div>
          <div class="card-side card-back">
            <p>Sagnik</p>
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