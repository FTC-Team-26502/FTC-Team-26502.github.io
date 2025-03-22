---
layout: default
title: Events
permalink: /fundraising/
---

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
      font-size: 3rem;
      margin-bottom: 1rem;
      color: #007c11;
      text-transform: uppercase;
      letter-spacing: 5px;
    }

    .events-section p {
      font-size: 1.2rem;
      margin-bottom: 3rem;
      color: #000000;
    }

    .events-list {
      max-width: 800px;
      margin: 0 auto;
      padding: 1rem;
      background: rgb(183, 255, 176);
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .event-item {
      border-bottom: 1px solid #ccc;
      padding: 1rem 0;
      text-align: center;
    }

    .event-item:last-child {
      border-bottom: none;
    }

    .event-image {
      width: 100%;
      max-width: 300px;
      height: auto;
      border-radius: 10px;
      margin-bottom: 1rem;
    }

    .event-item h3 {
      font-size: 1.5rem;
      color: rgb(253, 0, 211);
      margin-bottom: 0.5rem;
    }

    .event-item p {
      margin: 0.5rem 0;
      color: #000000;
    }

    .event-button {
      display: inline-block;
      margin-top: 1rem;
      padding: 0.5rem 1rem;
      font-size: 1rem;
      color: #fff;
      background-color: #007c11;
      border: none;
      border-radius: 5px;
      text-decoration: none;
      transition: background-color 0.3s ease;
    }

    .event-button:hover {
      background-color: #005f0d;
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
        <p>Join us in celebrating the remarkable work of our participating teams this season, and explore their amazing ocean-themed creations.</p>
        <a href="/FLLExpo" class="event-button">Learn More</a>
      </div>

      <!-- Event 2 -->
      <div class="event-item">
        <h3>Fundraising Gala</h3>
        <p><strong>Date:</strong> May 15, 2025</p>
        <p><strong>Time:</strong> 6:00 PM - 9:00 PM</p>
        <p><strong>Location:</strong> Grand Ballroom, City Hall</p>
        <p>An evening of fun, networking, and support for our robotics initiatives. Dinner and entertainment included!</p>
        <a href="/events/fundraising-gala" class="event-button">Learn More</a>
      </div>

      <!-- Event 3 -->
      <div class="event-item">
        <h3>Community Outreach Workshop</h3>
        <p><strong>Date:</strong> June 10, 2025</p>
        <p><strong>Time:</strong> 1:00 PM - 4:00 PM</p>
        <p><strong>Location:</strong> Local Library, Room 101</p>
        <p>We’re hosting a hands-on robotics workshop for kids and families. Learn how robots work and how to build your own!</p>
        <a href="/events/community-outreach-workshop" class="event-button">Learn More</a>
      </div>
    </div>
  </section>
</body>

</html>