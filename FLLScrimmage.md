<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FLL Scrimmage Schedule</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
      background: rgb(255, 220, 250);
      color: #000000;
    }

    .schedule-section {
      text-align: center;
      padding: 4rem 2rem;
    }

    .schedule-section h1 {
      font-size: 3rem;
      margin-bottom: 1rem;
      color: #007c11;
      text-transform: uppercase;
      letter-spacing: 5px;
    }

    .description {
      font-size: 1.2rem;
      margin-bottom: 3rem;
      color: #000000;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.6;
    }

    .schedule-container {
      max-width: 800px;
      margin: 0 auto 2rem auto;
      background-color: white;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      overflow: hidden;
    }

    .schedule-item {
      display: flex;
      border-bottom: 1px solid #eee;
      transition: background-color 0.3s;
      position: relative;
      text-align: left;
    }

    .schedule-item:last-child {
      border-bottom: none;
    }

    .schedule-item:hover {
      background-color: rgba(0, 124, 17, 0.1);
    }

    .time {
      flex: 0 0 120px;
      font-weight: bold;
      padding: 15px;
      background-color: #007c11;
      color: white;
    }

    .event {
      flex: 1;
      padding: 15px;
      display: flex;
      align-items: center;
    }

    .break {
      background-color: rgba(255, 150, 220, 0.3);
    }

    .break .time {
      background-color: #ff75c3;
    }

    .signup-button {
      display: inline-block;
      background-color: #007c11;
      color: white;
      font-size: 1.3rem;
      font-weight: bold;
      text-decoration: none;
      padding: 1rem 2.5rem;
      border-radius: 8px;
      margin-top: 1rem;
      transition: all 0.3s ease;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .signup-button:hover {
      background-color: #005a0d;
      transform: translateY(-2px);
      box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    .signup-button:active {
      transform: translateY(1px);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    @media (max-width: 480px) {
      .time {
        flex: 0 0 90px;
        font-size: 0.9em;
      }
      
      .event {
        font-size: 0.9em;
      }

      .schedule-section h1 {
        font-size: 2rem;
      }
      
      .signup-button {
        font-size: 1.1rem;
        padding: 0.8rem 2rem;
      }
    }
  </style>
</head>

<body>
  <section class="schedule-section">
    <h1>FLL Scrimmage Schedule</h1>
    
    <div class="description">
      Welcome to the post-tournament FIRST LEGO League (FLL) scrimmage at Blue Ridge Boost! This friendly competition is hosted by FTC Team 26502 BRB Robotics, giving teams additional robot game practice now that the official tournament season has concluded. This scrimmage focuses exclusively on robot performance rounds, allowing teams to experiment with new strategies, test improvements, and continue developing their skills in a relaxed environment. Join us for a fun day of robot matches and friendly competition!
    </div>
    
    <div class="schedule-container" id="schedule-container">
      <div class="schedule-item">
        <div class="time">9:00 - 9:20</div>
        <div class="event">Check in and pit setup</div>
      </div>
      <div class="schedule-item">
        <div class="time">9:20 - 9:40</div>
        <div class="event">Practice Round</div>
      </div>
      <div class="schedule-item">
        <div class="time">9:40 - 10:00</div>
        <div class="event">First Round</div>
      </div>
      <div class="schedule-item break">
        <div class="time">10:00 - 10:20</div>
        <div class="event">Break</div>
      </div>
      <div class="schedule-item">
        <div class="time">10:20 - 10:40</div>
        <div class="event">Second Round</div>
      </div>
      <div class="schedule-item">
        <div class="time">10:40 - 11:00</div>
        <div class="event">Third Round</div>
      </div>
      <div class="schedule-item">
        <div class="time">11:00 - 11:20</div>
        <div class="event">Fourth Round</div>
      </div>
      <div class="schedule-item break">
        <div class="time">11:20 - 11:30</div>
        <div class="event">Break</div>
      </div>
      <div class="schedule-item">
        <div class="time">11:30 - 12:00</div>
        <div class="event">Closing Ceremony</div>
      </div>
    </div>
    
    <a href="https://docs.google.com/forms/d/1bsSN8mdh6VqruJ5QOmfHF8hESWcL7UHkDae4Q9_Khrk/edit" class="signup-button">SIGN UP NOW</a>
  </section>
</body>
</html>