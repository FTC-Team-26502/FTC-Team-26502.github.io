<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Our Events</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
      background: rgb(255, 220, 250);
      color: #000000;
    }

    .events-section {
      text-align: center;
      padding: 4rem 2rem;
    }

    .events-section h1 {
      font-size: 3.5rem;
      margin-bottom: 1rem;
      color: #007c11;
      text-transform: uppercase;
      letter-spacing: 5px;
      text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }

    .events-section p {
      font-size: 1.2rem;
      margin-bottom: 3rem;
      color: #333;
    }

    .events-list {
      max-width: 900px;
      margin: 0 auto;
      padding: 1rem;
    }

    .event-item {
      padding: 2rem;
      text-align: center;
      margin: 2rem 0;
      border: 4px solid rgb(255, 220, 250);
      border-radius: 15px;
      background-color: rgb(183, 255, 176);
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .event-item:hover {
      transform: translateY(-10px);
      box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
    }

    .event-item h3 {
      font-size: 2rem;
      color: rgb(253, 0, 211);
      margin-bottom: 0.5rem;
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
    }

    .event-item p {
      margin: 0.5rem 0;
      color: #000000;
      padding: 0 1rem;
    }

    .event-item p strong {
      color: #000000;
    }

    .event-button {
      display: inline-block;
      margin-top: 1rem;
      padding: 0.75rem 1.5rem;
      font-size: 1rem;
      color: #fff;
      background: linear-gradient(135deg, #007c11, #005f0d);
      border: none;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
      transition: background 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
    }

    .event-button:hover {
      background: linear-gradient(135deg, #005f0d, #007c11);
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
      transform: scale(1.05);
    }
  </style>
</head>

<body>
  <section class="events-section">
    <h1>Our Events</h1>
    <p>Check out details of our past and upcoming events below!</p>

    <!-- Events List -->
    <div class="events-list">
      <!-- Event 1 -->
      <div class="event-item">
        <h3>FLL Explore Expo</h3>
        <p><strong>Date:</strong> May 4, 2025</p>
        <p><strong>Time:</strong> 2:00 PM - 4:00 PM</p>
        <p><strong>Location:</strong> 2172, Ivy Road, Charlottesville VA</p>
        <p align="left">Join us in celebrating the remarkable work of our participating teams this season, and explore their amazing ocean-themed creations.</p>
        <a href="/FLLExpo" class="event-button">Learn More</a>
      </div>

      <!-- Event 2 -->
      <div class="event-item">
        <h3>FLL Scrimmage</h3>
        <p><strong>Date:</strong> May 10, 2025</p>
        <p><strong>Time:</strong> 9:00 AM - 12:00 Noon</p>
        <p><strong>Location:</strong> Blue Ridge Boost, 2171 Ivy Road Charlottesville VA</p>
        <p align="left">Come check out our local FIRST Lego League (FLL) scrimmage, where teams will battle it out in an exciting robot game! Watch as they put their creativity and engineering skills to the test on the field.</p>
        <a href="/FLLScrimmage" class="event-button">Learn More</a>
      </div>

      <!-- Event 3 -->
      <div class="event-item">
        <h3>Community Outreach Workshop</h3>
        <p><strong>Date:</strong> June 10, 2025</p>
        <p><strong>Time:</strong> 1:00 PM - 4:00 PM</p>
        <p><strong>Location:</strong> Local Library, Room 101</p>
        <p align="left">We're hosting a hands-on robotics workshop for kids and families. Learn how robots work and how to build your own!</p>
        <a href="/events/community-outreach-workshop" class="event-button">Learn More</a>
      </div>
    </div>
  </section>
</body>

</html>